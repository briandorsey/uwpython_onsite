letters = 'Python '

# awkward and error prone
i = 0
while i < len(letters):
    print letters[i]
    i += 1

for i in range(len(letters)):
    c = letters[i]
    print c

# more Pythonic
for c in letters:
    print c

# when you really do need the index
for i, c in enumerate(letters):
    print i, c
