#-------------1-------------
vowels='aioueAEIOU'
counter=0
String_Entered=input('please Enter String:')
if String_Entered.isalpha():
    String_Entered=str(String_Entered)
else:
    print('please Enter correct string')
for i in String_Entered:
    if i in vowels:
        counter+=1
print(f'numbers of vowels is {counter}')
#--------------------2---------------
List_of_Numbers=[]
for i in range(5):
    getElement=input("Please Enter Element: ")
    getElement=getElement
    List_of_Numbers.append(getElement)

print(List_of_Numbers)
ListSortedAsc=sorted(List_of_Numbers)
ListSortedDesc=sorted(List_of_Numbers,reverse=True)
print(ListSortedAsc)
print(ListSortedDesc)
#---------------3------------------ 
Text_entered='we study in iti'
num_of_iti_occures=Text_entered.lower().count('iti')
print(num_of_iti_occures)
#---------------4------------------
text=input("Please Enter Text:")
text_wo_vowels=''

if text.isalpha():
    text=str(text)
else:
    print('please Enter correct string')
for i in text:
    if i not in vowels:
        text_wo_vowels+=i
print(text_wo_vowels)

#------------5------------
Text2 = input("please Enter a string: ")
if Text2.isalpha():
    Text2=str(Text2)
else:
    print('please Enter correct string')
i_locations = []

for i, char in enumerate(Text2):
  if char.lower() == 'i':
    i_locations.append(i)

print(f'{i_locations}')

#-------------6-------------
getNum=input("Please Enter Num:")
if getNum.isdigit():
    getNum=int(getNum)    
else:
    print('Enter Correct number ')
element=[]
for i in range(1, getNum + 1):
    num=[]
    for j in range(1, i + 1):
      product = i * j
      num.append(product)
    element.append(num)
print(element)

#------------7------------
height_of_pyriamed=input('Enter integer num')
if height_of_pyriamed.isdigit():
    height_of_pyriamed=int(height_of_pyriamed)
else:
    print("please enter num")
for i in range(1,height_of_pyriamed+1):
    print(" "*(height_of_pyriamed-i)+"*"*(i))