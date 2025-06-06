# These are some useful functions for working with variables

string = "29"

# we can do something called typecasting, which is changing a data type
number = int(string)

print(number + 4) # ---> should give us 33

# the same thing can be done with numbers to strings

age = 24
name = 'jeff'
prompt = name + str(age)

print(prompt)

# len() gives us the length of a string or list
prompt = "What is your name?"
prompt += "\n>>>"
name = input(f"{prompt} ")
print(f"Your name is {len(name)} letters long.")