#------------------1
myfirstname='Tasneem'
mylastname='Samy'
myemail='tasnemsam562@gmail.com'
myaddress='Alex,BabSharq,24street'
myintake='Q3'

print('My First name is:',myfirstname,
      '\nMy Last name is:',mylastname,
      '\nMy Email is:',myemail,
      '\nMy Address is:',myaddress,
      '\nintake ',myintake)

#---------------------2
myparagraph= """My name is Tasneem
I live in Al
I'm a fresh graduate from Faculty of Engineering 
I'm a student at ITI
I love programing """

print(myparagraph)

#---------------------3
Grade=int(input("Enter your grade please:"))
if Grade >=85:
    print("Excellant")
elif Grade>=75:
    print("Very Good")
elif Grade>=65:
    print("Good")
elif Grade>=60:
    print("Passed")
else :
    print("Failed")
#---------------------4
temperature=int(input("Enter Temperature please:"))
if temperature >25:
    print('The Weather is hot')
elif temperature<25:
    print('The Weather is cold')
else:
    print('The Weather is fine')

#---------------------5
getnumber=int(input('Enter Number please:'))
if getnumber>0:
    print("Number is Positive")
else :
    print("Number is Negative")

#----------------------6
print (type(myfirstname),type(mylastname),
       type(myaddress),type(myemail),type(myintake),
       type(getnumber),type(temperature),type(Grade)
       )

#---------------------7
Num1=10
Num2=20
print("The sum is ",Num1+Num2)
print("The difference is ",Num1-Num2)
print("The multiplying is ",Num1*Num2)
print("The divesion of two numbers is ",Num1/Num2)