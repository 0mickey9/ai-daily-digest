from src.database import employees, activities, projects, relevance_reasons,role_descriptions,project_roles
from datetime import datetime
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')


import numpy as np

def find_employee_by_id(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            return employee
    raise ValueError('id is not found')

def find_projects_by_id(project_id):
    for project in projects:
        if project['id'] == project_id:
            return project
    raise ValueError('id is not found')

def create_embeddings(employees_text, activities_text):


    role_names = list(employees_text.keys())
    role_texts = list(employees_text.values())
    role_embeddings_array = model.encode(role_texts)

    local_activities_embeddings = model.encode(activities_text)

    employees_embeddings = dict(zip(role_names, role_embeddings_array))
    return employees_embeddings, local_activities_embeddings

role_embeddings, activities_embeddings = create_embeddings(
    role_descriptions,
    [activity['description'] for activity in activities]
)

def get_semantic_similarity(a,b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    similarity = dot_product / (norm_a * norm_b)

    return similarity


def get_top_activities_for_all_employees():
    today = datetime.today().date()
    top3_dic = {}
    for em in range(len(employees)):
        top3 = []
        for ac in range(len(activities)):
            relevance = 0
            if employees[em]['id'] == activities[ac]['creator_id']:
                continue

            created_at = activities[ac]['created_at'].date()


            reasons = []

            employee_role = employees[em]['role']
            cosine = get_semantic_similarity(activities_embeddings[ac] , role_embeddings[employee_role])
            semantic_score = max(cosine, 0)


            if created_at == today:
                relevance += 2
                reasons.append(relevance_reasons[0])

            if employees[em]['team'] == find_employee_by_id(activities[ac]['creator_id'])['team']:
                relevance += 3
                reasons.append(relevance_reasons[1])

            project = find_projects_by_id(activities[ac]['project_id'])

            if employees[em]['role'] in project_roles[project['name']]:
                relevance += 2
                reasons.append(relevance_reasons[2])

            if relevance == 0 or (len(reasons) == 1 and reasons[0] == relevance_reasons[0]):
                continue

            relevance += semantic_score

            if len(top3) < 3:
                top3.append(
                    {
                        'activity_id' : activities[ac]['id'],
                        'description' : activities[ac]['description'],
                        'score'       : relevance,
                        'reasons'     : reasons
                    }
                )
            else:
                mn = min(top3, key=lambda x: x['score'])
                if relevance > mn['score']:
                    top3[top3.index(mn)] = {
                        'activity_id': activities[ac]['id'],
                        'description': activities[ac]['description'],
                        'score'      : relevance,
                        'reasons'    : reasons
                    }

        top3.sort(key=lambda x: x['score'], reverse=True)

        # print(employees[em]['name'], ':')
        # for i in range(len(top3)):
        #     print(top3[i]['description'], '| score :', top3[i]['score'])
        # print()

        top3_dic[employees[em]['name']] = top3

    return top3_dic
