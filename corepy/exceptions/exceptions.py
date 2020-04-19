# exception handling:
# mechanism for interrupting normal program flow and continuing in surrounding 
# context or code block.

# Key concepts:
# Raise the exception
# Handling the exception
# Unhandled exceptions
# Exception object
import sys
from math import log

def convert(s):
    """Convert a string to an integer"""
    # x = -1
    try: # In Try block exception is raised
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        # x = int(number)
        return int(number)
        #print(f"Conversion succeeded! x = {x}")
    # Accessing Exception objects
    except (KeyError, TypeError) as e: # In except block exception is handled
        #print("Conversion failed!")
        # pass # Pass keyword is a no-op that is semantically empty
    # return x
        print(f"Conversion error: {e!r}", file = sys.stderr)
        raise # Re-raise an exception

def string_log(s):
    v = convert(s)
    return log(v)

DIGIT_MAP = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}


# str_convert = convert("one two three four".split())
# convert(391) # TypeError
# convert("Elephant".split()) # KeyError

# print(str_convert)

# Exceptions resulting from programmer errors:
# IndentationError
# SyntaxError
# NameError

logging = string_log("one two three".split())
print(logging)
string_log("ooch".split())
string_log(271)
