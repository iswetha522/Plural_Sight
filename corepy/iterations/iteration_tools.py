# Python provides a powerful vocabulary for working with iterators
# These include enumerate() and sum()
# the itertools module provide many more
# itertools.islice() - perform lazy slicing of an iterator
# itertools.count() - an unbounded arthimetic sequence of integers.

from itertools import count, islice
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousand_primes)# <itertools.islice object at 0x109e75a40>
print(list(thousand_primes)[-10:])
# print(sum((x for x in count() if is_prime(x)), 1000)) # 3682913

# any : Determines if any elements in a series are true.
# all : Determines if all elements in a series are true.

print(any([False, False, True])) # True
print(all([False, False, True])) # False
print(any(is_prime(x) for x in range(1328, 1361))) # False
print(all(name == name.title() for name in ['London',
    'Paris', 'Tokyo', 'New York', 'Sydney', 'Kuala Lumpur'])) # True


# Zip(): Synchronize iteration across two or more iterables.

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
for item in zip(sunday, monday):
    print(item) 

# (12, 13)
# (14, 14)
# (15, 14)
# (15, 14)
# (17, 16)
# (21, 20)
# (22, 21)
# (22, 22)
# (23, 22)
# (22, 21)
# (20, 19)
# (18, 17)

for sun, mon in zip(sunday, monday):
    print("average = ", (sun + mon) / 2)

# average =  12.5
# average =  14.0
# average =  14.5
# average =  14.5
# average =  16.5
# average =  20.5
# average =  21.5
# average =  22.0
# average =  22.5
# average =  21.5
# average =  19.5
# average =  17.5

tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]
for temps in zip(sunday, monday, tuesday):
    print(f"min = {min(temps):4.1f}, max = {max(temps):4.1f}, average = {sum(temps)/len(temps):4.1f}")

# min =  2.0, max = 13.0, average =  9.0
# min =  2.0, max = 14.0, average = 10.0
# min =  3.0, max = 15.0, average = 10.7
# min =  7.0, max = 15.0, average = 12.0
# min =  9.0, max = 17.0, average = 14.0
# min = 10.0, max = 21.0, average = 17.0
# min = 11.0, max = 22.0, average = 18.0
# min = 12.0, max = 22.0, average = 18.7
# min = 10.0, max = 23.0, average = 18.3
# min =  9.0, max = 22.0, average = 17.3
# min =  8.0, max = 20.0, average = 15.7
# min =  8.0, max = 18.0, average = 14.3


from itertools import chain
temperatures = chain(sunday, monday,tuesday)
print(all(t > 0 for t in temperatures)) # True

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b



for x in (p for p in lucas() if is_prime(p)):
    print(x)