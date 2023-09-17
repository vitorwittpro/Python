favorite_numbers = {
    'robert': [5, 45, 81],
    'david':  [89, 32, 67, 90],
    'marie': [80, 1, 68, 54],
}

for name, numbers, in favorite_numbers.items():
    print(f"Favorite number of {name.title()}:")
    for number in sorted(numbers):
        print(f"\t{number}")
