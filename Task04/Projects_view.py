from tabulate import tabulate

from Projects_load import load_projects


def view_all_projects():
    projects = load_projects()
    headers = ["id","Title", "Details", "Total Target", "Start Time", "End Time"]
    data = [[p["id"],p["title"], p["details"], p["total_target"], p["start_time"], p["end_time"]] for p in projects]
    print(tabulate(data, headers=headers))
    return True