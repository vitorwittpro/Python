responses = {}

active = True

while active:
    name = input("What is your name? ")
    response = input("What mountain would you like to climb? ")

    responses[name] = response

    repeat = input("Would you like to let someone else respond? ")

    if repeat == 'no':
        active = False

print("--- Poll results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")