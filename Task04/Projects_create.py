from Projects_load import load_projects
from Projects_save import save_projects


def create_project(title, details, total_target, start_time, end_time):
    projects = load_projects()
    project_id_counter = max(project['id'] for project in projects) + 1 if projects else 1
    project = {
        "id": project_id_counter,
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_time": start_time,
        "end_time": end_time
    }
    projects.append(project)
    save_projects(projects)
    
