squares = []

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

print('Minimun', min(squares))
print('Maximun', max(squares))
print('Sum', sum(squares))