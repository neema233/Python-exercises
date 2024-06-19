import re
pattern = r"^[^@]+@[^@]+\.[a-zA-Z]{2,}$"

def validate_names(name):
    if name.isalpha() and not bool(re.match(pattern,name )):
        return True
    else:
        return False
    
def validate_email(email):
    if bool(re.match(pattern,email)):
        return True
    else:
        return False

def validate_passsword(password):
    if len(password)>=8:
        return True
    else:
        return False
    
def validate_Phone(phone):
    phone_regex = r"^01[0-9]{9}$"
    if bool(re.match(phone_regex,phone)):
        return True
    else:
        return False