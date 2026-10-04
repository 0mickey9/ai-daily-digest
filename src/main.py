from data import *
from digest import*
from random import *

top_of =  get_top_activities_for_all_employees()

for emp, his_top in top_of.items():
    generate_digest(emp, his_top)

