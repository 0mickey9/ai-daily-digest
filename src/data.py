employees_names = ['Alice', 'Bob', 'Carl', 'Denny', 'Faride']

roles = ['backend-developer', 'frontend-developer', 'data-scientist', 'qa-tester', 'product-manager']

teams = ['web_creators','web_creators','data_analyst','web_creators','data_analyst']

employees = []

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


project_names = ['data-processing','web-service']
project_description = [ 'observing data to increase profit','creating web platform']
projects = []
relevance_reasons = ['- recent activity','- same team']

for i in range(1,len(employees_names)  + 1):
    employees.append(
        {
            'id' : i,
            'name' : employees_names[i - 1],
            'role' : roles[i - 1],
            'team' : teams[i - 1],
        }
    )


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


for i in range(1,len(project_description) + 1):
    projects.append(
        {
            'id'          : i,
            'name'        : project_names[i - 1],
            'description' : project_description[i - 1],
        }
    )

