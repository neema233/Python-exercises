from Projects_load import load_projects
from Projects_save import save_projects


def delete_project(index):
    projects = load_projects()
    index_of_list=index-1
    try:
        if 0 <= index_of_list < len(projects):
            del projects[index_of_list]
            save_projects(projects)
            print("Project deleted successfully!")
        else:
            print("Invalid project index")
    except Exception as e:
        print("An error occurred:", e)