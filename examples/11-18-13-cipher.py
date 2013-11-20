###########################################
# DSCI15310 Sec. 003
# 
# Author: Doug Stanley
#   Date: 11/18/13
#
# Class examples, where we worked through
# how to convert a message string into a
# "encrypted" message, using a simple 
# cipher (a character map, where each
# character maps to a different one).
#
#############################################
import string

# need mapping of characters
#start with an alphabet of all the printable characters
#which should include letters, numbers, punctuation, etc.
alphabet = string.printable

# Create a simple cipher map, where we map a character
# in our alphabet, to a character in the reverse of our alphabet.
# we use the string slice syntax, to reverse our string easily.
cipher = dict( zip(alphabet, alphabet[::-1]) )

# here we create basically the opposite map, by swapping the
# the position of our two strings.
reverse = dict( zip(alphabet[::-1], alphabet) )

# This function takes the original message,
# loops through it, and creates a new string
# with characters replaced with the cipher version
def encode(message):
    # loop through the message, replacing characters
    trans = ""
    for char in message:
        trans = trans + cipher[char]
    return trans

# This function does the exact oposite of our
# encode function.
def decode(trans):
    clear = ""
    for char in trans:
        clear = clear + reverse[char]
    return clear

# need message
message = "Stuck between a rock and a hard place, we found pickles!"

# Now we test by translating our message to cipher version
# print out the cipher, then translate the cipher back and print
# it out. We should get the same message as we started with if
# all went well.
trans = encode(message)
print trans

print decode(trans)
