# These are cross between comprehensions and generator functions.
# Similar to comprehensions syntax:
# (expr(item) for item in iterable)

million_squares = (x*x for x in range(1, 1000001))
print(million_squares)
print(list(million_squares)[-10:])
print(list(million_squares)) # [] Generators are single use objects.


# By using list comprehension it takes 400mb memory
# but using generators it won't take any memory and
# gives the output in seconds.
print(sum(x*x for x in range(1, 10000001)))#333333383333335000000


# we can use IF clause at the end of generator expressions;
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print(sum(x for x in range(1001) if is_prime(x)))# 76127