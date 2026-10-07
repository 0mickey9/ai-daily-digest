# from src.data import activity_description
#
#
# activity_description = activity_description
# employee_description =

from sentence_transformers import SentenceTransformer
import numpy as np
from src.database import activities
from src.ranking import find_activity_by_id,find_employee_by_id
from src.database import employees


model = SentenceTransformer('all-MiniLM-L6-v2')

employee_text = ['data-scientist analyzes datasets, customer behavior, metrics and business data',
'frontend-developer builds user interfaces, layouts, navigation and web pages',
'backend-developer manages server logic, databases, APIs, authentication and validation',
'qa-tester tests features, checks functionality, finds bugs and writes tests',
'product-manager defines requirements, plans features and aligns user and business needs']

activities_desc = [i['description'] for i in activities]
print(activities_desc)

employee_embedding = model.encode(employee_text)
activity_embeddings = model.encode(activities_desc)
print(type(activity_embeddings))
print(activity_embeddings.shape)


def cosine_similarity(a,b):
    dot_product = np.dot(a,b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    similarity = dot_product / (norm_a * norm_b)

    return similarity

# for ac in range(len(activities)):
#     print(activities[ac]['description'])
#     for desc in range(len(employee_text)):
#         print(cosine_similarity(activity_embeddings[ac], employee_embedding[desc]))

expected_relevance = {
    'Alice': [5, 9],
    'Bob': [1, 5, 9],
    'Carl': [8, 10],
    'Denny': [1, 3, 6],
    'Faride': [4, 7],
}

def find_employee_by_role(x) :
    for i in employees:
        if i['role'] == x:
            return i

for desc in range(len(employee_text)):
    # print(employee_text[desc])
    burmalda = [(0,-1)] * 3
    current_employee = find_employee_by_role(
        employee_text[desc].split(' ')[0])
    for ac in range(len(activities)):
        if activities[ac]['creator_id'] == current_employee['id']:
            continue
        cosine = cosine_similarity(activity_embeddings[ac], employee_embedding[desc])
        if cosine > min(burmalda,key=lambda x:x[1])[1]:
            burmalda[burmalda.index(min(burmalda,key=lambda x:x[1]))] = (activities[ac]['id'], cosine)
    # print()
    s = 0
    print(list(map(lambda x: x[0],sorted(burmalda, key=lambda x:x[0]) )))
    for i in range(len(burmalda)):
        if burmalda[i][0] in expected_relevance[current_employee['name']]:
            s += 1

    print(f'precision for {current_employee['name']}: {s} / {3} = {s / 3}')
    #
    # print('\n\n')





