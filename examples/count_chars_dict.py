count = {}

word = 'bumblebee'

for letter in word:
    letter = letter.lower()
    if letter in count:
        count[letter] = count[letter] + 1
    else:
        count[letter] = 1


print count
