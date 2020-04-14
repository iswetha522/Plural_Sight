a = [[1, 2], [3, 4]]
b = a[:]
print(a is b)
print( a == b)
print("------------")
print(a[0])
print(b[0])
print(a[0] is b[0])
print("----------")
a[0] = [8, 9]
print(a[0])
print(b[0])
print("----------")
a[1].append(5)
print(a[1])
print(b[1])

print("------")
print(a)
print(b)
print('-------')
