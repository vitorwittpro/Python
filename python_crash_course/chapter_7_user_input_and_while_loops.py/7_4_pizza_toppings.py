message = "Enter a pizza topping."
message += "\nType 'quit' to exit.\n"

while True:
    pizza_topping = input(message)

    if pizza_topping == "quit":
        break
    else:
        print(f"{pizza_topping.title()} was added to your pizza.")