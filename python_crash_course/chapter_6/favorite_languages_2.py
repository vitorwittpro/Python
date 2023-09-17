favorite_languages = {
    'jen': ['python', 'javascript'],
    'sarah': ['c'],
    'edward': ['rust', 'c++'],
    'phil': ['python', 'c#'],
}

for names, languages in favorite_languages.items():
    print(f"{names.title()}")
    for language in languages:
        if len(language) == 1:
            print(f"\t{names.title()} favorite language is {language.title()}")
        else:
            print(f"\t{language.title()}")

