def build_user_message(employee,activities):
    text = f'Employee:\nName : {employee["name"]}\nRole : {employee["role"]}\n\nActivities :\n'
    # тут обробляється масив а може бути таке що потрібно буде обробляти словник
    for index, activity in enumerate(activities,start=1):
        text += f'{index}. {activity}\n'
    return text

employee = {
    "name": "Bob",
    "role": "frontend-developer"
}

activities = [
    "Fixed layout problems on mobile screens.",
    "Found a bug in the registration form.",
    "Updated the navigation menu."
]

print(build_user_message(employee, activities))