# Program to create two lists and print them together side by side

sno = []
sname = []
name = input("Enter The Name : ")
no = int(input("Enter The Number : "))
sname.append(name)
sno.append(no)

while True:
    name = input("Enter The Name : ")
    if name == "end":
        break
    no = int(input("Enter The Mobile Number : "))
    sname.append(name)
    sno.append(no)

for i, j in zip(sname, sno):
    print(i, j)
