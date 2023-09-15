locations = ['France, PA', 'Edinburg, GB-SCT', 'Tokyo, JP', 'Toronto, CA', 'Seattle, US']

print('sorted', sorted(locations))

print('original', locations)

print('sorted reverse', sorted(locations, reverse=True))

print('original', locations)

locations.reverse()
print('reverse', locations)

locations.reverse()
print('reverse again', locations)

locations.sort()
print('sort', locations)

locations.sort(reverse=True)
print('sort reverse', locations)


