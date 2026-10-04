from database import employees, activities, projects, relevance_reasons
from datetime import datetime, timedelta

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

def get_top_activities_for_all_employees():
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
            if created_at == today:
                relevance += 2
                reasons.append(relevance_reasons[0])

            if employees[em]['team'] == find_employee_by_id(activities[ac]['creator_id'])['team']:
                relevance += 3
                reasons.append(relevance_reasons[1])

            ranking_results.append(
                {
                    'employee_id': employees[em]['id'],
                    'activity_id': activities[ac]['id'],
                    'score': relevance,
                    'reasons': reasons,
                }
            )

            if len(top3) < 3:
                if relevance > 2:
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
