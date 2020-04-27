# open()
# Open a file for reading or writing
# file: the path to the file(required)
# mode: read, write, or append, plus binary or text
# encoding: encoding to use in text mode


# read() ---> decode()
# write() -------> encode()

import sys
print(sys.getdefaultencoding())

# open() Modes:
# Modes - Meaning
# 'r' - open for reading
# 'w' - open for writing
# 'a' - oprn for appending
# Selector - Meaning
# 'b' - binary mode
# 't' - text mode

# Writing a file:
# write() returns the number of codepoints written.
# Don't sum these values to determine file length.
# f = open('wasteland.txt', mode='wt', encoding='utf-8')
# # print(help(f))
# f.write("What are the roots that clutch, ")
# f.write("whta branches grow\n")
# f.write('Out of this stony rubbish?')
# f.close()
# exit()

# Reading a file:
g = open('wasteland.txt', mode = 'rt', encoding='utf-8')
print(g.read(32))
print(g.read())
print(g.read())
print(g.seek(0))

# Seek cannot move to arbitrary offset.
# Only 0 and values from tell() are allowed.
# Other values result in undefined behavior.

print(g.readline())
print(g.readline())
print(g.readline())
print(g.seek(0))
print(g.readlines())
g.close()


# Appending a file:
h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['Son of man, \n',
    'You cannot say, or guess, \n',
    'for you know only, \n',
    'A heap of broken images, ',
    'where the sun beats\n'])
h.close()