# range(stop)
# range(start, stop)
# range(start, stop, step)

# we cannot use range() in this scenario
s = [0, 1, 4, 6, 13]
for i in range(len(s)):
    print(s[i])

# we can use the above code as 
v = [0, 1, 4, 6, 13]
for i in v:
    print(i)

# Enumerate:
# It constructes an iterable of (index, value) tuples around another iterable object
t = [6, 372, 8862, 148800, 2096886]
for p in enumerate(t):
    print(p)


# output:
# (0, 6)  (index, value)
# (1, 372)
# (2, 8862)
# (3, 148800)
# (4, 2096886)


for i, v in enumerate(t):
    print(f"i = {i}, v = {v}")    

# output:
# i = 0, v = 6
# i = 1, v = 372
# i = 2, v = 8862
# i = 3, v = 148800
# i = 4, v = 2096886