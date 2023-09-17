message = "\nEnter your age."
message += "\nType 'quit' to exit.\n"

while True:
    age = input(message)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("The ticket is free")
    elif age < 12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")

