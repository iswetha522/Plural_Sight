t = ("Norway", 4.953, 3)
print(t)
print(t[0])
print(t[2])
print(len(t))
for item in t:
    print(item)

print(t + (338186.0, 265e9))
print(t * 3)
a = ((220, 284), (1184,1210), (2620, 2924), (5020, 5564), (6232, 6363))
print(a[2][1])
h = (391)
print(h)
print(type(h))

k = (391,)
print(k)
print(type(k))

e = () # empty tuple
print(e)
print(type(e))

p = 1, 1, 1, 4, 6, 19
print(p)
type(p)

def minmax(items):
    return min(items), max(items)


print(minmax([83, 33, 84, 32, 85, 31, 86]))

lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
print(lower)
print(upper)

(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a)
print(b)
print(c)
print(d)

a = 'jelly'
b = 'bean'
a, b = b, a
print(a)
print(b)

tup = tuple([561, 1105, 1729, 2465])
print(tup)

tupstr = tuple('Carmichael')
print(tupstr)

print(5 in (3, 5, 17, 257, 65537))
print(5 not in (3, 5, 17, 257, 65537))