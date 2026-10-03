from ranking import *
from data import *
from datetime import datetime
from pathlib import Path
project_root = Path(__file__).parent.parent
top3 = get_top_activities_for_all_employees()

def generate_digest(one_employee,only_his_top3):
    name_of_file = project_root / 'output' / f'{one_employee.lower()}_digest.md'
    with open(name_of_file, 'w', encoding='utf-8') as fp:
        fp.write(f"## {one_employee} Digest\n\n")
        fp.write('### Daily digest \n\n')
        fp.write(str(datetime.today()).split(' ')[0] + '\n\n')


        for activity in only_his_top3:
            string = '- '+ activity['description'] + ' | score: ' + str(activity['score'])  + '\n'
            fp.write(string)

# def find_activity_by_id(activity_id):
#     for activity in activities:
#         if activity['id'] == activity_id:
#             return activity

