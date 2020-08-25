string = input('Enter The String :')
words = string.split(' ')
for i in range(len(words)):
    rep = ''
    if words[i][::-1] == words[i]:
        for j in range(len(words[i])):
            rep += '*'
        words[i] = rep
words = ' '.join(words)
print(words)

