import sys
f = open(sys.argv[1], mode = 'rt', encoding='utf-8')
for line in f:
    # using sys.stdout.write() instead of print.
    # This won't add newlines like print().
    # print(line)
    sys.stdout.write(line)
f.close()

