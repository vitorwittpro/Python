favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['sarah', 'phil']

for name, language in sorted(favorite_languages.items()):
    print(f"Hello {name.title()}.")
    if name in friends:
        print(f"    {name.title()},I see you love {language.title()}.")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our pool!")

print("\nLanguages:")
for language in set(favorite_languages.values()):
    print(language.title())