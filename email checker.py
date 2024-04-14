import re #regex

#email validate checker

def validate_email(email):
    email_conditions = "^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    if re.search(email_conditions, email):
        return True
    else:
        return False

user_email = input("Enter email here: ")
if validate_email(user_email):
    print("Valid email id")
else:
    print("Please enter a valid email id")