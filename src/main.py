from src.data import *
from src.digest import *
from random import *
from datetime import date


reference_date = date.today()
top_of = get_top_activities_for_all_employees(semantic_weight = 1,reference_date = reference_date)
for emp, his_top in top_of.items():
    generate_digest(emp, his_top, reference_date)
    print(emp, [i['activity_id'] for i in his_top])
