# Program to check whether the given string is a valid car number

import re

while True:
    num = input("Enter The Number [end to stop] : ")
    if num == "end":
        break
    if re.fullmatch("[A-Za-z]{2}\s[0-9]{1,2}\s[A-Za-z]\s[0-9]{4}", num):
        print("Valid")
    else:
        print("Invalid")

# \s[0-9]{1-2}\s[A-Z]\s[0-9]{4}
