from Projects_load import load_projects
from register import Register


def login():
    try:
        email=str(input("Enter your Email:"))
        password_Entered=str(input("Enter Password:"))
        
        fileobj=open("user.txt","r")
        for line in fileobj:
            first_name_txt,last_name_txt,email_txt,password_txt,phone_txt =line.strip().split(',')
            if email == email_txt and password_Entered== password_txt:
                print("Logged in successfully")
                return email


        print("Invaild Email or Password")
        new_account = input("Do you want to register a new account? (yes/no): ")
        if new_account.lower() == 'yes':
            Register()
        else:
            print("Sorry invaild char")

    except ValueError as e:
        print(f"Enter Correct Date,Error: {e} ")