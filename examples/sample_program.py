#############################################################
# Sample Program (Title or one line description goes here)
#
#  This sample program is solely to give
#  an example of how a python file should
#  be formatted before submission.
#  (Generally, this is where you would put a  longer
#   description of what the program does)
#
#  Author: Doug Stanley <dostanle AT cs DOT kent DOT edu>
#    Date: 11/11/11
# Version: 1.0
#
############################################################

# I prefer to put all of my import statements at the very
# top if possible
import random
import math


#We ask the user for some input
name = raw_input("What's your name? ")

#Now we loop through ever leter of their name
# and print it out for no reason
for letter in name:
    print letter

#now lets print out a goodbye message
print "Thanks for playing"

