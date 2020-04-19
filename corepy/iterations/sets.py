# SETS: Unordered collection of unique items
# sets are mutable
# Elements in a set must be immutable
# Sets removes duplicate objects from the list
# set uses shallow copy method

p = {6, 28, 496, 8128, 33550336}
print(p)
print(type(p))

d = {}
print(type(d)) # dictionay

e = set()
print(e)

s = set([2, 4, 16, 64, 4096, 65536, 262144])
print(s)

t = [1, 4, 2, 1, 7, 9, 9]
print(set(t))

# Iterating through a set but the result is unordered
for x in {1, 2, 4, 8, 16, 32}:
    print(x)


# membership operators in sets
q = {2, 9, 6, 4}
print(3 in q)
print(3 not in q)

k = {81, 108}
print(k)

# for adding an item in set we use add method
k.add(54)
print(k)
k.add(12)
print(k)

# if we try to add the duplicate value it won't show any error
k.add(108)
print(k)

# we can update many items in a set
k.update([37, 128, 97])
print(k)

# remove an item form the set
k.remove(97)
print(k)

# tring to remove an item which is not in the set
# k.remove(98)
# print(k) #KeyError: 98

# we can use discard method instead of remove 
k.discard(98)
print(k)

# copy of sets can be done in two ways:
j = k.copy()
print(j)

m = set(j)
print(m)