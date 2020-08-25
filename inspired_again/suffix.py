s = input()

string = []

for i in range(int(input())):
    string.append(input())

for i in string:
    if i[-len(s):] == s:
        print(i)
