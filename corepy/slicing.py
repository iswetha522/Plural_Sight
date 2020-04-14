s = [3, 186, 4431, 74400, 1048443]
print(s[1:3])
print(s[1:-1])
print(s[2:])
print(s[:2])
print(s[:])
t = s
print(t is s)

r = s[:]
print(r is s)

print(r == s)

u = s.copy()
print(u is s)
print(u == s)

v = list(s)
print(v is s)
print(v == s)