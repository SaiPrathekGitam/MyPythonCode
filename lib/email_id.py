# Program to print only valid email ids

import re

while True:
    email = input(("Enter The Email ID [end to stop] : "))
    if email == "end":
        break
    if re.fullmatch("\w+@\w+\.com",email):
        print("Valid")
    else:
        print("Invalid")