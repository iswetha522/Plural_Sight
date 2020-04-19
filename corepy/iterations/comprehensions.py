# List comprehension syntax: 
# [expr(item) for item in iterable]

# Concise syntax for describing lists, sets and dictionaries.
# Readable and expressive
# close to natural language.

words = """Why sometimes I have believed as many as six impossible things
"before breakfast""".split()
print(words)
# List comprehension
print([len(word) for word in words])

# Equivalent syntax
lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)

from math import factorial
f = [len(str(factorial(x))) for x in range(20)]
print(f)
print(type(f))
f = [factorial(x) for x in range(20)]
print(f)


# Set comprehensions
from math import factorial
f = {len(str(factorial(x))) for x in range(20)}
print(f)
print(type(f))


# Dict Comprehensions
# {
#     key_expr(item) : value_expr(item)
#     for item in iterable
# }

country_to_capital = {
                        'United Kingdom' : 'London',
                        'Brazil' : 'Brasilia',
                        'Morocco' : 'Rabat',
                        'Sweden' : 'Stockholm'
}
capital_to_country = { capital : country for country, capital in 
                        country_to_capital.items()
                     }

from pprint import pprint as pp
pp(capital_to_country)


# Complex Expressions
import os
import glob
file_sizes = {os.path.realpath(p) : os.stat(p).st_size for 
                p in glob.glob('*.py')}
pp(file_sizes)