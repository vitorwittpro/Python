players = ['charles', 'martina', 'michael', 'florence', 'eli']


# player from 0 to 2
print("\nplayers[0:3]\n", players[0:3])
print(players, "\n")

# players from 1 to 3
print("\nplayers[1:4]\n", players[1:4])
print(players, "\n")

# staring from beginning
print("\nplayers[:4]\n", players[:4])
print(players, "\n")

# from middle to end
print("\nplayers[3:]\n", players[3:])
print(players, "\n")

# from end to to middle
print("\nplayers[-2:]\n", players[-2:])
print(players, "\n")

# from middle to beginnig
print("\nplayers[:-2]\n", players[:-2])
print(players, "\n")

# print one item each 5 items
numbers = list(value for value in range(1, 50))
print(numbers[:50:5]) # [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]

# loop through a slice
print("\nHere's my team")
for player in players[:3]:
    print(player.title())