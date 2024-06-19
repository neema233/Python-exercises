from datetime import datetime
from Projects_create import create_project
from Projects_delete import delete_project
from Projects_edit import edit_project
from Projects_search import search_projects_by_date
from Projects_view import view_all_projects
from login import login
from register import Register


def main():
    try:
        choose_register_or_login =int(input("Press 1 for register, 0 for login: "))
        if choose_register_or_login == 1:
            Register()
            login()
        elif choose_register_or_login == 0:
            user_logged_in = login()
            if user_logged_in:
                while True:
                    print("\n1. Create a project")
                    print("2. View all projects")
                    print("3. Edit a project")
                    print("4. Delete a project")
                    print("5. Search projects by date")
                    print("6. Exit")
                    try:
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            title = str(input("Enter project title: "))
                            details = str(input("Enter project details: "))
                            if " " not in title and details.strip():
                                total_target = float(input("Enter total target: "))
                                if total_target > 0:
                                    try:
                                        start_time = input("Enter start time (YYYY-MM-DD): ")
                                        end_time = input("Enter end time (YYYY-MM-DD): ")
                                        start_date_obj = datetime.strptime(start_time, "%Y-%m-%d")
                                        end_date_obj = datetime.strptime(end_time, "%Y-%m-%d")
                                        if start_date_obj > end_date_obj:
                                            print("Start date cannot be after end date.")
                                            continue
                                        else:
                                            create_project(title, details, total_target, start_time, end_time)
                                    except ValueError:
                                          print("Invalid date format. Please use YYYY-MM-DD.") 
                                else:      
                                    print("Invalid total target. Please enter a positive number.")
                                    continue 
                            else:
                                print("Enter Valid title and details")
                                continue
                        elif choice == 2:
                            view_all_projects()
                        elif choice == 3:
                            index = int(input("Enter project index to edit: "))
                            new_title = str(input("Enter new title: "))
                            new_details = str(input("Enter new details: "))
                            if " " not in new_title and new_details.strip():
                                new_total_target = float(input("Enter new total target: "))
                                if new_total_target > 0:
                                    try:
                                      new_start_time = input("Enter new start time (YYYY-MM-DD): ")
                                      new_end_time = input("Enter new end time (YYYY-MM-DD): ")
                                      start_date_obj_new = datetime.strptime(new_start_time, "%Y-%m-%d")
                                      end_date_obj_new = datetime.strptime(new_end_time, "%Y-%m-%d")
                                      if start_date_obj_new > end_date_obj_new:
                                             print("Start date cannot be after end date.")
                                             continue
                                      else:
                                          edit_project(index, new_title, new_details, new_total_target, new_start_time, new_end_time)
                                    except Exception as e:
                                        print(f"Error: {e}")
                                else:
                                    print("Invalid total target. Please enter a positive number.")
                                    continue
                            else:
                                print("Enter Correct new title and new details") 
                        elif choice == 4:
                            index = int(input("Enter project index to delete: "))
                            delete_project(index)
                        elif choice == 5:
                            search_projects_by_date()
                        elif choice == 6:
                            print("Exiting...")
                            break
                        else:
                            print("Invalid choice")

                    except Exception as e:
                        print("Error:",e)
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()