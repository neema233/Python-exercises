from datetime import datetime
from tabulate import tabulate
from Projects_load import load_projects

def search_projects_by_date():
    projects = load_projects()
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except Exception as e:
        print(f"Error: {e}")
        return
    
    for project in projects:
        project["start_time"] = datetime.strptime(project["start_time"], "%Y-%m-%d")
        project["end_time"] = datetime.strptime(project["end_time"], "%Y-%m-%d")

    matched_projects = [p for p in projects if p["start_time"] <=date<=p["end_time"]]
    headers = ["ID", "Title", "Details", "Total Target", "Start Time", "End Time"]
    data = [[p["id"], p["title"], p["details"], p["total_target"], p["start_time"], p["end_time"]] for p in matched_projects]
    print(tabulate(data, headers=headers))
