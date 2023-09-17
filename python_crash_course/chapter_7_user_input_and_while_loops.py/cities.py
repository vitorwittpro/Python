prompt = "Please enter the name of the city that you have visited."
prompt += "\nType 'quit' to exit of the program\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")