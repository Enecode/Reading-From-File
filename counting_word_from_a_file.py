
name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigcount = None
for word.count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = word
        bigcount = counts
