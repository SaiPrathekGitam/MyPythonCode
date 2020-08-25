s = input()
n = int(input())
string = ''

for i in range(len(s)):
    string += s[i]
    if (i + 1) % 2 == 0:
        print(string, end=' ')
        string = ''

print(string, end=' ')
