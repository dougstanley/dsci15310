count = []
for x in range(26):
    count.append(0)
    
word = 'tumble'

for letter in word:
    i = ord(letter.lower()) - 97
    count[i] = count[i] + 1


print count
