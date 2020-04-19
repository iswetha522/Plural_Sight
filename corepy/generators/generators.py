# Yield:
# Generator functions must include at least one yield statement.
# They may also include return statements.

def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()
print(g) #<generator object gen123 at 0x100b4a510>
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # end of sequence generates StopIteration exception

for v in gen123():
    print(v)

h = gen123()
i = gen123()

print(h) #<generator object gen123 at 0x102f974a0>
print(i) #<generator object gen123 at 0x102f97580>

print(h is i) # False (different address locations)

print(next(h))
print(next(h))
print(next(i))

