# like any good intro book al has us make a program that says hello world and asks for our name
# this program is similar but a bit more special

from time import sleep

class Bear:
    """A bear that chases you, run."""
    
    def __init__(self, species):
        """Initialize bear parameters."""
        self.species = species

    def roar(self):
        """The bear roars while chasing you."""
        print(f"The {self.species} bear roars!")
        print("ROAR!")

    def bite(self):
        """The bear tries to bite you."""
        print(f"The {self.species} is trying to bite you!")
        sleep(2)
        print("CHOMP")

kodiak = Bear('kodiak')

print("Hello, World!")
name = input("What is your name? ")
if name != 'exit':
    bear_attack = True

print(f"Hello {name}! It is nice to meet you!")

while bear_attack:
    print("Oh god why! ITS A BEAR!!")
    sleep(2)
    kodiak.roar()
    sleep(2)
    print("AHHHH")
    kodiak.bite()
    bear_attack = False