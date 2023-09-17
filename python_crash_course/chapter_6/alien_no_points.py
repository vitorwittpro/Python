alien = {'color': 'red'}

# print(alien['points']) # KeyError: 'points'

point_value = alien.get('points', 'No point value assigned.')
print(point_value)