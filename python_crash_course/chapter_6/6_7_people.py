person_0 = {
    'first': 'Robert',
    'last': 'Martin',
    'age': 59,
}

person_1 = {
    'first': 'Eric',
    'last': 'Mathew',
    'age': 34,
}

person_2 = {
    'first': 'Adytia',
    'last': 'Bhargava',
    'age': 40,
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\tName: {person['first'].title()} {person['last'].title()}")
    print(f"\tAge: {person['age']}")
    