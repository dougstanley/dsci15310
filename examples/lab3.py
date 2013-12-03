####################################################
#  LAB 3
#
# This is the sample code we went over 
# in class as part of Lab 3.
# It is meant to be used as a reference
# as to how to implement things like
# saving the student database to a file.
#
#  Author: Doug Stanley <dmstanle AT kent DOT edu>
# Version: 1.0
#    Date: 12/2/13
#
####################################################

#We need the pickle module to save our
#student roster to disk.
import pickle

try:
    dbfile = open('abcd.db','r')
    students = pickle.load(dbfile)
    dbfile.close()
except:
    students = {}

def add_student():
    #Lastname, Firstname
    name = raw_input("Enter student's name: ")
    #ID Number
    idnum = raw_input("Enter student's id: ")
    #D.O.B.
    bday = raw_input("Enter student's Date of Birth: ")

    students[idnum] = { 'name':name, 'bday':bday }
    

def delete_student():
    idnum = raw_input("Delete which student: ")
    del students[idnum]

def find_student():
    idnum = raw_input("Find which student: ")
    print students[idnum]
    
menu = {}
menu['1'] = "Add student."
menu['2'] = "Delete student."
menu['3'] = "Find student."
menu['4'] = 'Exit'

while True:
    options = menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]

    selection = raw_input("Please select: ")
    if selection == '1':
        add_student()
    elif selection == '2':
        delete_student()
    elif selection == '3':
        find_student()
    elif selection == '4':
        break
    else:
        print "Unknown option selected!"

try:
    dbfile = open('abcd.db', 'w')
    pickle.dump(students, dbfile)
    dbfile.close()
except Exception, e:
    print "Sorry, an error occurred, all your hard work was not saved!"
    print str(e)

#Copypasta trap
import sys
sys.exit()
x = 5
if x is 5:
    print "We're Done!"
# And that's it, we're done.
