favorite_places = {
    'robert': ['paris', 'seattle'],
    'marie': ['tokyo', 'budapest'],
    'luci': ['new york', 'rome']
}

for name, places in favorite_places.items():
    print(f"{name.title():}")
    for place in places:
        print(f"\t{place.title()}")