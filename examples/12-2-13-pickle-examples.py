#First, we need to import pickle
import pickle

#Create a tupple with some numbers
numbers = (1,45,5463,8632,445)

#open a file, dump the numbers tupple
#using pickle to that file, then close
#it to make sure it's written
datafile = open('test.pickle','w')
pickle.dump(numbers, datafile)
datafile.close()

#delete these variables to show nothing is
#still around
del datafile
del numbers

#now lets do the reverse, and load
# our tupple back in

#open the file back up for reading
#read the data back in and "un-pickle"
#it, then close the file back up
newfile = open('test.pickle','r')
numbers = pickle.load(newfile)
newfile.close()

#at this point, numbers should exist again
print numbers
