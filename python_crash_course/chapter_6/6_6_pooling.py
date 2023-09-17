favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['sarah', 'phil', 'edgar']

for name in favorite_languages:
    if name in friends:
        print(f"    Hello {name.title()}, Thank you for that.")
    else:
        print(f"    Hello {name.title()}, please take our pool!")
