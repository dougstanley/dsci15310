############################################
# Create a cipher dictionary, where the
# mapping is randomly jumbled.
#
# Author: Doug Stanley
#   Date: 11/18/13
# 
#############################################

#import random and string code
import random
import string

# Start with an alphabet of all printable characters
alphabet = string.printable

# Convert the string of our alphabet into
# a list of characters, and then have the
# random module randomly jumble the characters
jumbled = list(alphabet)
random.shuffle(jumbled)

# Create a map from the original alphabet to
# the new randomly jumbled alphabet
cipher = dict( zip( alphabet, jumbled ) )

# Create the reverse of the map above, which maps
# jumbled character to it's original version
reverse = dict( zip( jumbled, alphabet ) )

