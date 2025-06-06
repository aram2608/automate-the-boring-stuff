exp = 1 + 2
exp_2 = 1 * 2

print(exp, exp_2)

# Expressions are the most basic type of programming instruction in pretty much any lang
# These consist of values (ie numbers, floats) and operators (ie +, -, /, %)
# Evaluation leads to reducing down to a single value

# list of common operators and in order of their precendence
operators = ['**', '%', '//', '/', '*', '-', '+']
operations = ['exponents', 'modulo', 'floor division', 'division', 'multiplication', 'subtraction', 'addition']

expressions = {}

while operators and operations:
    operator = operators.pop()
    operation = operations.pop()
    expressions[operation] = operator

print(expressions)

# zip() is a handy function that pairs two items from a list into a tuple
operators = ['**', '%', '//', '/', '*', '-', '+']
operations = ['exponents', 'modulo', 'floor division', 'division', 'multiplication', 'subtraction', 'addition']
zipped = zip(operators, operations)
print(list(zipped))

# makes building dictionaries much easier
expressions = dict(zip(operators, operations))
print(expressions)

# the biggest flex is to use enumerate() and zip() together

operators = ['**', '%', '//', '/', '*', '-', '+']
operations = ['exponents', 'modulo', 'floor division', 'division', 'multiplication', 'subtraction', 'addition']

for i, (op, meaning) in enumerate(zip(operators, operations)):
    print(f"{i}: {op} means {meaning}")

# enumerate returns an item and its index, it can make tables like say a csv, or tsv