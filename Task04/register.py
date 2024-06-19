from validate import *


def Register():
    try:
       first_name=str(input("Enter First Name:"))
       if not validate_names(first_name):
           print("Enter Correct First Name:")

       else:
           last_name=str(input("Enter Last Name:"))
           if not validate_names(last_name):
               print("Enter Correct last Name:")
           else:
               email=str(input("Enter Email:"))
               if not validate_email(email):
                 print("Enter Correct email:")

               else:
                   password=str(input("Enter password:"))
                   if not validate_passsword(password):
                       print("Enter Correct Passowrd:")
                   else:    
                       confirm_password=str(input("Confirm your password:"))
                       if confirm_password!=password:
                           print("Not Matched Password")
                       else:
                           phone=str(input("Enter your phone"))
                           if not validate_Phone(phone):
                               print("Not correct phone")
                           else:
                               file_obj=open('user.txt','a')
                               file_obj.write(f"""{first_name},{last_name},{email},{password},{phone}\n""")
                               print("Logged in successfully")
                               
      
    except Exception as e:
        print(f"Enter Correct Data,Error: {e}")