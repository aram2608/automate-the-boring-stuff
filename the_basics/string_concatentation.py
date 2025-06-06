# A data type is a category for a value in python
# Examples include integers, floating points, and strings

#string can be concatenated together

first = 'alice'
last = '\twonderland' # the \t tells python to include a tab, this make the format more standard
full_name = first + last
print(full_name)

# a strange behavior python allows is using * with a string and a number

spam = 'spam'
print(spam * 3) # ---> should evaluate to spamspamspam

# why it does this is a mystery to me but just role with it.