
### employees
employees = []

employees_names = ['Alice', 'Bob', 'Carl', 'Denny', 'Faride']

roles = ['backend-developer', 'frontend-developer', 'data-scientist', 'qa-tester', 'product-manager']

teams = ['web_creators','web_creators','data_analyst','web_creators','data_analyst']
for i in range(1,len(employees_names)  + 1):
    employees.append(
        {
            'id' : i,
            'name' : employees_names[i - 1],
            'role' : roles[i - 1],
            'team' : teams[i - 1],
        }
    )
print(employees)

### activities

activities = []

creators_id = [1, 2, 2, 3, 4, 1, 3, 5, 4, 5]


project_id = [2, 2, 2, 1, 2, 2, 1, 1, 2, 1]

activity_description = ['fixed an error in user login',
               'updated the navigation menu on the website',
               'fixed layout problems on mobile screens',
               'cleaned duplicate customer records from the dataset',
               'tested the new login functionality',
               'improved validation of user registration data',
               'analyzed customer activity data',
               'reviewed results of customer activity analysis',
               'found a bug in the registration form',
               'prepared requirements for the next analytics task']

created_at = [
    '2026-10-02 09:15',
    '2026-10-03 09:40',
    '2026-10-02 10:25',
    '2026-10-03 10:50',
    '2026-10-02 11:30',
    '2026-10-03 12:10',
    '2026-10-02 13:20',
    '2026-10-03 14:00',
    '2026-10-02 15:10',
    '2026-10-03 16:00',]

for i in range(1,len(activity_description) + 1):
    activities.append(
        {
            'id' : i,
            'creator_id' : creators_id[i - 1],
            'project_id' : project_id[i - 1],
            'description': activity_description[i - 1],
            'created_at' : created_at[i - 1],

        }
    )


print(activities)


### Projects
project_names = ['data-processing','web-service']
project_description = [ 'observing data to increase profit','creating web platform']
projects = []
for i in range(1,len(project_description) + 1):
    projects.append(
        {
            'id'          : i,
            'name'        : project_names[i - 1],
            'description' : project_description[i - 1],
        }
    )
print(projects)


#ranking_results

ranking_results = []

# revelance for each emlpoyer

from datetime import datetime

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

relevance_reasons = ['- recent activity','- same team']
top3_dic = {}
for em in range(len(employees)):
    top3 = []
    for ac in range(len(activities)):
        relevance = 0
        if employees[em]['id'] == activities[ac]['creator_id']:
            continue

        created_at = activities[ac]['created_at'].split(' ')[0]


        today = str(datetime.today()).split(' ')[0]
        diff = days_between(created_at, str(today))
        reasons = []
        if diff == 0:
            relevance += 2
            reasons.append(relevance_reasons[0])

        if employees[em]['team'] == find_employee_by_id(activities[ac]['creator_id'])['team']:
            relevance += 3
            reasons.append(relevance_reasons[1])

        ranking_results.append(
            {
                'employee_id' : employees[em]['id'],
                'activity_id' : activities[ac]['id'],
                'score'       : relevance,
                'reasons'     : reasons,
            }
        )


        if len(top3) < 3:
            if relevance > 2 :
                top3.append([activities[ac]['id'], relevance])
        else :
            mn = min(top3, key=lambda x: x[1])
            if relevance > mn[1]:
                top3[top3.index(mn)] = [activities[ac]['id'], relevance]

    top3.sort(key=lambda x: x[1], reverse=True)

    print(employees[em]['name'],':')
    for i in range(len(top3)):
        print(find_activity_by_id(top3[i][0])['description'],'| score :', top3[i][1])
    print()


    top3_dic[employees[em]['name']] = top3

print(top3_dic)

print(ranking_results)


def generate_digest(employee_id):
    emp = find_employee_by_id(employee_id)
    name_of_file ='output/' + emp['name'].lower() + '_digest.md'
    with open(name_of_file, 'w', encoding='utf-8') as fp:
        fp.write('## ' f'{emp['name']}' ' Digest\n\n')
        fp.write('### Daily digest \n\n')
        fp.write(today + '\n\n')


        for i in top3_dic[emp['name']]:
            emp_act = find_activity_by_id(i[0])
            string = '- '+ emp_act['description'] + ' | score: ' + str(i[1])  + '\n'
            fp.write(string)

for employee in employees:
    generate_digest(employee['id'])


