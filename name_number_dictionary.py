# Program to display given names and numbers in sorted order

data = {}
name = input("Enter The Name ('end' to stop) : ")
no = int(input("Enter The Mobile Number : "))
data[name] = no

while True:
    name = input("Enter The Name : ")
    if name == "end":
        break
    no = int(input("Enter The Mobile Number : "))
    data[name] = no

print(sorted(data.items()))
