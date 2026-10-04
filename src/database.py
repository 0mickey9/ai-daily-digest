import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# from psycopg2.extras import DictCursor
conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    port=DB_PORT,
    password=DB_PASSWORD
)

# cursor_factory = DictCursor
cursor = conn.cursor()
cursor.execute('select * from employees')
result = cursor.fetchall()
cursor.close()
employees = []
for employee in result:
    employees.append({
        'id': employee[0],
        'name': employee[1],
        'role': employee[2],
        'team': employee[3],
    })
# print(employees)
# sql = f"insert into employees values (%s, %s)"
# cursor.execute(sql, "some result")
#conn.commit()

cursor = conn.cursor()
cursor.execute('select * from teams')
result = cursor.fetchall()
cursor.close()
teams = []
for team in result:
    teams.append({
        'id': team[0],
        'name': team[1],
    })
# print(teams)

cursor = conn.cursor()
cursor.execute('select * from activities')
result = cursor.fetchall()
cursor.close()
activities = []
for activity in result:
    activities.append({
        'id': activity[0],
        'creator_id': activity[1],
        'project_id': activity[2],
        'description': activity[3],
        'created_at': activity[4],
    })
# print(activities)

cursor = conn.cursor()
cursor.execute('select * from projects')
result = cursor.fetchall()
cursor.close()
projects = []
for project in result:
    projects.append({
        'id': project[0],
        'name': project[1],
        'description': project[2],
    })
# print(projects)

conn.close()

relevance_reasons = ['- recent activity','- same team', '-relevant project']

import datetime
