alien_0 = {'x_position': 0, 'y_position': 0, 'speed': 'medium', 'points': 5 }

print(f"Original position: {alien_0['x_position']}")

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

print(alien_0)

del alien_0['points']

print(alien_0)