pet_0 = {
    'kind': 'dog',
    'owner': 'robert',
}

pet_1 = {
    'kind': 'cat',
    'owner': 'marie',
}

pet_2 = {
    'kind': 'bird',
    'owner': 'luci',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"Kind: {pet['kind'].title()}")
    print(f"Owner: {pet['owner'].title()}")
