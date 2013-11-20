#10/14/13
# Chapter 9
#  Word Play examples
wordfile = open("c:/Users/student/Desktop/words.txt")
line_count = 0


#for line in wordfile:
#    print line.strip()
#    line_count = line_count + 1
#    if line_count == 5:
#        break

#while line_count < 10:
#    print wordfile.readline().strip()
#    line_count = line_count + 1
    
word = raw_input("What word are you looking for?").lower()

for line in wordfile:
    line_count = line_count + 1
    if word == line.strip():
        print "Found it @", line_count
        break
