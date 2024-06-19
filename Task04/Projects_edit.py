from Projects_load import load_projects
from Projects_save import save_projects


def edit_project(index, new_title, new_details, new_total_target, new_start_time, new_end_time):
    projects=load_projects()
    for project in projects:
        if project['id'] == index:
            project['title'] = new_title
            project['details'] = new_details
            project['total_target'] = new_total_target
            project['start_time'] = new_start_time
            project['end_time'] = new_end_time
            print("Project edited successfully!")
            save_projects(projects)
        
    print("Invalid project index")