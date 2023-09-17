words = ['homme', 'femme', 'canard', 'cheval', 'pappilon', 'fille', 'parfait', 'mouche', 'pomme', 'noir', 'chat', 'chien']

print('original\n', words)


# adding in the end
words.append('citron')
print('\nadding\n', words)

# inserting in any position
words.insert(0, 'ours')
print("\ninsert\n", words)

# removing
del words[3]
print('\nremoving\n', words)

# popping the last item and showing
last = words.pop()
print(f"\npop last '{last}'\n", words)

# popping item in any position
indexed = words.pop(5)
print(f"\npop '{indexed}'\n", words)

# removing by value
words.remove('homme')
print(f"\nremoved\n", words)


# sorting temporarily
print('\nsorted\n', sorted(words))

# sorting reversed temporarily
print('\nsorted reverse-alphabetical\n', sorted(words, reverse=True))

# sorting permanently
# sorting temporarily
words.sort()
print('\nsort permanently\n', words)

# sorting reversed permanently
words.sort(reverse=True)
print('\nsort permanently reverse-alphabetical\n', words)