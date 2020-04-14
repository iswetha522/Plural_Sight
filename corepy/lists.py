
c = [21,37]
d = (c * 4)
print(d)
print([0] * 9)

s = [[-1, +1]] * 5
print(s)
s[2].append(7)
print(s)

w = "The quick brown fox jumps over the lazy dog".split()
print(w)

i = w.index('fox')
print(i)
print(w[i])

# print(w.index('unicorn'))
print(w.count('the'))
print(37 in [1, 78, 9, 37, 34, 53])
print(78 not in [1, 78, 9, 37, 34, 53])

u = "jackdaws love my big sphinx of quartz".split()
print(u)
del u[3]
print(u)
u.remove('jackdaws')
print(u)
del u[u.index("quartz")]
print(u)
# u.remove('pyramid')
# print(u)

a = "I accidently the whole universe".split()
print(a)
a.insert(2, "destroyed")
print(a)
print(" ".join(a))

m = [2, 1, 3]
n = [4, 7, 11]
k = m + n
print(k)

k += [18, 29, 47]
print(k)

k.extend([76, 129, 199])
print(k)

g = [1, 11, 21]
g.reverse()
print(g)

d = [17, 41, 29]
d.sort()
print(d)

d.sort(reverse = True)
print(d)

h = "not perplexing do handwriting family where I illegibly know doctors".split()
print(h)

h.sort(key = len)
print(h)

print(" ".join(h))

x = [4, 9, 2, 1]
y = sorted(x)
print(y)
print(x)

p = [9, 3, 1, 0]
q = reversed(p)
print(q)
print(list(q))