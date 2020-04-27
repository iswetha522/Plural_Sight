# Objects that behave like files
# A semi - formal protocol
# File behaviours are too varied for a fully - specified protocol
# Use an EAFP approach with file-like objects when necessary.

def words_per_line(flo):
    return[len(line.split()) for line in flo.readlines()]


with open('wasteland.txt', mode = 'rt', encoding='utf-8') as real_file:
    wpl = words_per_line(real_file)


print(wpl) # [9, 7, 5, 4, 9]
print(type(real_file)) # <class '_io.TextIOWrapper'>

from urllib.request import urlopen
with urlopen("http://sixty-north.com/c/t.txt") as web_file:
    wpl = words_per_line(web_file)


print(wpl) # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 7, 8, 14, 12, 8]
print(type(wpl)) # <class 'list'>
print(type(web_file)) # <class 'http.client.HTTPResponse'>