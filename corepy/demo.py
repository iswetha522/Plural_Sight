from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    # The content is in byte codes so we have to decode it to get it in strings
    # line_words = line.split() 
    line_words = line.decode('utf8').split() 
    for word in line_words:
        story_words.append(word)


story.close()
print(story_words)


# output without decoding:
# [b'It', b'was', b'the', b'best', b'of', b'times', b'it', b'was', b'the', 
# b'worst', b'of', b'times', b'it', b'was', b'the', b'age', b'of', b'wisdom',
#  b'it', b'was', b'the', b'age', b'of', b'foolishness', b'it', b'was', b'the',
#  b'epoch', b'of', b'belief', b'it', b'was', b'the', b'epoch', b'of',
#  b'incredulity', b'it', b'was', b'the', b'season', b'of', b'Light', 
# b'it', b'was', b'the', b'season', b'of', b'Darkness', b'it', b'was', b'the',
#  b'spring', b'of', b'hope', b'it', b'was', b'the', b'winter', b'of', 
# b'despair', b'we', b'had', b'everything', b'before', b'us', b'we', b'had', 
# b'nothing', b'before', b'us', b'we', b'were', b'all', b'going', b'direct',
#  b'to', b'Heaven', b'we', b'were', b'all', b'going', b'direct', b'the',
#  b'other', b'way', b'in', b'short', b'the', b'period', b'was', b'so', b'far', 
# b'like', b'the', b'present', b'period', b'that', b'some', b'of', b'its',
#  b'noisiest', b'authorities', b'insisted', b'on', b'its', b'being', 
# b'received', b'for', b'good', b'or', b'for', b'evil', b'in', b'the', 
# b'superlative', b'degree', b'of', b'comparison', b'only']

# output wit decode():
# ['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst',
#  'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 
# 'the', 'age', 'of', 'foolishness', 'it', 'was', 'the', 'epoch', 'of', 
# 'belief', 'it', 'was', 'the', 'epoch', 'of', 'incredulity', 'it', 'was', 
# 'the', 'season', 'of', 'Light', 'it', 'was', 'the', 'season', 'of', 
# 'Darkness', 'it', 'was', 'the', 'spring', 'of', 'hope', 'it', 'was', 'the',
#  'winter', 'of', 'despair', 'we', 'had', 'everything', 'before', 'us', 'we', 
# 'had', 'nothing', 'before', 'us', 'we', 'were', 'all', 'going', 'direct',
#  'to', 'Heaven', 'we', 'were', 'all', 'going', 'direct', 'the', 'other', 
# 'way', 'in', 'short', 'the', 'period', 'was', 'so', 'far', 'like', 'the',
#  'present', 'period', 'that', 'some', 'of', 'its', 'noisiest', 'authorities', 
# 'insisted', 'on', 'its', 'being', 'received', 'for', 'good', 'or', 'for', 
# 'evil', 'in', 'the', 'superlative', 'degree', 'of', 'comparison', 'only']