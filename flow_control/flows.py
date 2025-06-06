# Normally programs do not run line by line, usually you will have flow control statements to regulate what is happening

# For example lets take the following snippet

eggs = 20

# We start off with a number of eggs we have

def eat_egg(eggs):
    eggs -= 1
    return eggs

print(eat_egg(eggs)) # ----> should return 19

# The previous function simulates us getting hungry and munching on an egg.