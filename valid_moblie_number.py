# Program to check whether given mobile number is valid or not

n = input("Enter The Mobile Number : ")

if n.isdigit() is True and len(n) == 10:
    print("Valid Mobile Number")
else:
    print("Not A Valid Mobile Number")
