aliens = []

for alien_number in range(30):
    new_alien = {'color': 'gray', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'gray':
        alien['color'] = 'green'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
        alien['points'] = 15


for alien in aliens[:5]:
    print(alien)
print("...")

print(f"\nTotal number of aliens: {len(aliens)}")