import json
def save_projects(projects):
    with open('projects.json', "w") as file:
        json.dump(projects, file, indent=4)