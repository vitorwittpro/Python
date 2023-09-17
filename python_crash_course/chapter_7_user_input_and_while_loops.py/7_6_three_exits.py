message = "\nEnter your age."
message += "\nType 'quit' to exit.\n"

active = True

while active:
    age = input(message)

    if age == 'quit':
        active = False

    age = int(age)

    if age < 3:
        print("The ticket is free")
    elif age < 12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")

