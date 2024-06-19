import json

def load_projects():
    try:
        projects_file='projects.json'
        with open(projects_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading projects: {e}")
        return None