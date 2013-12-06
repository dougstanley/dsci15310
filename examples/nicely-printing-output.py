###########################################
# Nicely print some output
#
#  This program simply prints some
#  data in a nice way to make it
#  easy to read.
#  This is for demonstration purposes
#  only, to give an idea to the students.
#
#  Author: Doug Stanley
#    Date: 12/6/13
# Version: 0.1
############################################

idnumber = 500

# Start with an empty dictionary to put some data in
data = {}

# Create a key, set to the value stored in the variable
# idnumber, and assign it a value that is
# another empty dictionary
data[idnumber] = {}

# In this new dictionary, add some values
# for some typical keys about people like name, age, etc
data[idnumber]["name"] = "Tom"
data[idnumber]["age"]  = 28
data[idnumber]["phone"] = "216-999-1111"
data[idnumber]["rank"] = "junior"


#Now lets nicely print out this data:
print "Name:", data[idnumber]["name"]
print "Age:", data[idnumber]["age"]
print "Class Rank:", data[idnumber]["rank"]
print "Phone Number:", data[idnumber]["phone"]
