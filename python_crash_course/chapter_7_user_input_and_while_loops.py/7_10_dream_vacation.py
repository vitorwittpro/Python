users_dream = {}

active = True

while active:
    name = input("Name: ")
    dream = input("Dream: ")

    users_dream[name] = dream

    continueAsking = input("Continue? ")

    if continueAsking == 'no':
        active = False

for name, dream in users_dream.items():
    print(f"\t{name.title()}: {dream.title()}")
