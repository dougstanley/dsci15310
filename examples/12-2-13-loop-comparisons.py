#for loop running 5 times
for i in range(5):
    print i

#while loop version of above for loop
i = 0
while i < 5:
    print i
    i = i + 1

#looping through items in a sequence
sequence = (1,2,5,6,8,32,6)
for item in sequence:
    print item

#One version of a while loop version
#of above for loop
i = 0
while i < len(sequence):
    item = sequence[i] 
    i = i + 1
    print item
