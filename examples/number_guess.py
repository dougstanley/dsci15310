import math
import random

name = raw_input("What is your name?")

print "Hello,", name

rng = int(random.random() * 10)

guess = raw_input("Give me a number (0-10):")
guess = int(guess)

if guess > 10 or guess < 0:
    print "Can't you follow directions!"    
elif guess == rng:
    print "You win 1,000,000 money"
else:
    print "Awe poor thing"

print "The winning number was", rng
