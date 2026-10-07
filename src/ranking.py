from src.database import employees, activities, projects, relevance_reasons,role_desscriptions,project_roles
from datetime import datetime, timedelta

import numpy as np


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def find_employee_by_id(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            return employee

def find_activity_by_id(activity_id):
    for activity in activities:
        if activity['id'] == activity_id:
            return activity

def find_projects_by_id(project_id):
    for project in projects:
        if project['id'] == project_id:
            return project

def transformer(employees_text, activities_text):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')

    role_names = list(employees_text.keys())
    role_texts = list(employees_text.values())
    role_embeddings_array = model.encode(role_texts)

    activities_embeddings = model.encode(activities_text)

    employees_embeddings = dict(zip(role_names, role_embeddings_array))
    return employees_embeddings, activities_embeddings

def get_semantic_similarity(a,b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    similarity = dot_product / (norm_a * norm_b)

    return similarity

def get_top_activities_for_all_employees(i):

    role_embeddings, activities_embeddings = transformer(role_desscriptions,[i['description'] for i in activities])

    ranking_results = []
    top3_dic = {}
    for em in range(len(employees)):
        top3 = []
        for ac in range(len(activities)):
            relevance = 0
            if employees[em]['id'] == activities[ac]['creator_id']:
                continue

            created_at = activities[ac]['created_at'].date()

            today = datetime.today().date()
            reasons = []

            employee_role = employees[em]['role']
            cosine = get_semantic_similarity(activities_embeddings[ac] , role_embeddings[employee_role])
            semantic_score = max(cosine, 0) * 1


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

            ranking_results.append(
                {
                    'employee_id': employees[em]['id'],
                    'activity_id': activities[ac]['id'],
                    'score': relevance,
                    'reasons': reasons,
                }
            )

            if len(top3) < 3:
                if relevance > 0 and not (
                        len(reasons) == 1 and reasons[0] == relevance_reasons[0]):
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
