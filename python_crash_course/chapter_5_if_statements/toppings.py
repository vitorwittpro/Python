available_toppings = ["mushrooms", "green peppers", "extra cheese", "olives", "pineapple", "pepperoni"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
# requested_toppings = []

if requested_toppings:

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding the {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}")
 
    print("\nFinished making your pizza.\n")
else:
    print("Are you sure you want a plain pizza?")