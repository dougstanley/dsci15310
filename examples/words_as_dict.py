word_file = open("c:\Users\student\Desktop\words.txt")
all_words = {}

for word in word_file:
    all_words[word.strip()] = ''

word_file.close()


                 
