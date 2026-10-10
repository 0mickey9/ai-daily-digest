from src.ranking import get_top_activities_for_all_employees
from datetime import date


import math  as m

def dcg_at_k(predicted,relevant,k):
    dcg = 0
    for i, value in enumerate(predicted[:k]):
        dcg += int(value in relevant) / m.log2(i + 2)
    return dcg

def idcg_at_k(relevant,k):
    idcg = 0
    for i in range(min(len(relevant), k)) :
        idcg += 1 / m.log2(i + 2)
    return idcg

def ndcg_at_k(predicted, relevant, k):
    dcg = dcg_at_k(predicted, relevant, k)
    idcg = idcg_at_k(relevant, k)
    return dcg / idcg if idcg else 0

def precision_at_k(predicted,relevant,k):
    s = 0
    for i in predicted[:k]:
        if i in relevant:
            s += 1
    return s / k if k else 0

import csv
from datetime import datetime
from pathlib import Path
from src.ranking import prepare_activities

def load_test_activities(path):
    activities = []

    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            for key in row:
                if key in ('id', 'creator_id', 'project_id'):
                    if row[key]:
                        row[key] = int(row[key])

                elif key == 'created_at':
                    if row[key]:
                        row[key] = datetime.strptime(row[key], "%Y-%m-%d %H:%M")
            activities.append(row)

    return activities

csv_path = Path(__file__).parent / "test_activities.csv"
test_activities = load_test_activities(csv_path)


def load_ground_truth(path):
    with open(path, newline='', encoding='utf-8') as file:
        ground_truth = []
        reader = csv.DictReader(file)
        for row in reader:
            for key in row:
                if key in ('employee_id','activity_id','relevance'):
                    row[key] = int(row[key])

            ground_truth.append(row)
    return ground_truth

ground_truth = load_ground_truth(r'C:\Users\Admin\OneDrive\Desktop\пр пр шкибиди доп\програмування\my ml github projects\ai-daily-digest\tests\ground_truth_draft.csv')
from src.ranking import find_employee_by_id
expected_relevance = {
        'Alice': [],
        'Bob': [],
        'Carl': [],
        'Denny': [],
        'Faride': []}
for row in ground_truth:
    if row['relevance'] == 1:
        who = find_employee_by_id(row['employee_id'])['name']
        expected_relevance[who].append(row['activity_id'])

for weight in [0,1]:
    print(f'Weight {weight} (Rule-based)')
    predictions = get_top_activities_for_all_employees(semantic_weight=weight,reference_date=date(2026, 10, 4),test_activities=test_activities)

    mean_pr = 0
    mean_ndcg = 0
    k = 3
    print(f"\nWeight = {weight}")

    for employee, ranked in predictions.items():
        print(employee)
        for activity in ranked:
            print(
                activity["activity_id"],
                round(activity["score"], 3)
            )
    for key,value in predictions.items():
        activity_ids = [activity_id['activity_id'] for activity_id in value]
        precision = precision_at_k(activity_ids,expected_relevance[key],k)
        employee_ndcg = ndcg_at_k(activity_ids,expected_relevance[key],k)
        mean_pr += precision
        mean_ndcg += employee_ndcg
        print(f'{key} : precision : {round(precision, 3)} ndcg : {round(employee_ndcg, 3)}')

    print('mean', round(mean_pr/len(predictions), 3))
    print('mean', round(mean_ndcg / len(predictions), 3))












