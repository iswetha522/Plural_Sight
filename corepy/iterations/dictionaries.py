urls = {'Google' : 'http://google.com',
        'Pluralsight' : 'http://pluralsight.com',
        'Sixty North' : 'http://sixty-north.com',
        'Microsoft' : 'http://microsoft.com'
        }

print(urls['Pluralsight'])

# Dictionary Constructor
names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 3)]
d = dict(names_and_ages)
print(d)

phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo', f='foxtrot')
print(phonetic)

# as with lists, dictionaries are shallow copy
d = dict(goldenrod = 0xDAA520, indigo = 0x4B0082, seashell = 0xFFF5EE)
e = d.copy()
print(e)
f = dict(e)
print(f)

# For updating a dictionary
g = dict(wheat = 0xF5DEB3, khaki = 0xF0E68C, crimson = 0xDC142C)
f.update(g)
print(f)

# While updating the dictionary if we have two keys identical then it 
# it will replace the new value with the older value.
stocks = {'GOOG' : 891, 'AAPL' : 416, 'IBM' : 194 }
stocks.update({'GOOG' : 894, 'YHOO' : 25})
print(stocks)

# Using for loop for iterations in dictionary
colors = dict(aquamarine = '#7FFFD4', burlywood = '#DEB887',
                chartreuse = '#7FFF00', cornflower = '#6495ED',
                firebrick = '#B22222', honeydew = '#F0FFF0',
                maroon = '#B03060', sienna = '#A0522D')

for key in colors:
    print(f"{key} => {colors[key]}")

# To iterate and get only the values
for value in colors.values():
    print(value)

# To iterate the dictionary and get the keys
for key in colors.keys():
    print(key)

# to iterate to the dictionay and get the key and value at tandem
for key, value in colors.items():
    print(f"{key} => {value}")


# in and not in operators are used for the keys not for the values
symbols = dict(usd = '$', nzd = '$', nok = 'kr', ind = 'inr', hhg = 'Pu')
print(symbols)
print('nzd' in symbols)
print('mkd' not in symbols)

# Deleting an item from dictionary
z = {'H' : 1, 'Tc' : 43, 'Xe' : 54, 'Fy' : 137, 'Rf' : 104, 'Fm' : 100}
print(z)
del z['Fy']
print(z)

m = {'H' : [1, 2, 3],
     'He' : [3, 4],
     'Li' : [6, 7],
     'Be' : [7, 9, 10],
     'B' : [10, 11],
     'C' : [11, 12, 13, 14]    
    }

m['H'] += [4, 5, 6, 7]
print(m)
m['N'] = [13, 14, 15]
print(m)


from pprint import pprint as pp
pp(m)