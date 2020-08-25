# Program to sort given dictionary by values

d = {}
d2 = {}

while True:
    name = input("Enter The Name (end to stop) : ")
    if name == 'end':
        break
    number = input("Enter The Number : ")
    d[name] = number

for i in sorted(d, key=d.get):
    print(i, d[i])

# print()
# for i in sorted(d.values()):
#     for j in d:
#         if d[j] == i:
#             d2[j] = d[j]
#
# for j in d2:
#     print(j, d2[j])

