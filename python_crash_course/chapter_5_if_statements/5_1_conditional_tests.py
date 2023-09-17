language = "python"

print(f"\nIs '{language}' == 'python'?, I predict True")
print(language == 'python')

print(f"\nIs '{language}' == 'java'?, I predict False")
print(language == 'java')

print(f"\nIs '{language}' == 'Python'?, I predict False, case sensitive")
print(language == 'Python')

print(f"\nIs '{language}' == 'Python'.lower()'?, I predict True, case sensitive now")
print(language == 'Python'.lower())

print(f"\nIs '{language}'.title() == 'Python'.lower()'?, I predict False")
print(language.title() == 'Python'.lower())

print(f"\nIs '{language}'.title() == 'Python''?, I predict True")
print(language.title() == 'Python')

print(f"\nIs '{language}'.upper() == 'Python'.upper()'?, I predict True")
print(language.upper() == 'Python'.upper())

print(f"\nIs '{language}'[0] == 'nohtyP'[-1]'?, I predict False")
print(language[0] == 'nohtyP'[-1])

print(f"\nIs '{language}'[0] == 'nohtyP'[-1].lower()'?, I predict True")
print(language[0] == 'nohtyP'[-1].lower())

print(f"\nIs '{language}'[:2] == 'py'?, I predict True")
print(language[:2] == 'py')

