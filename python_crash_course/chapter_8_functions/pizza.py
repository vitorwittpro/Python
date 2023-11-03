# the asterisk tell python to make make a tuple called <variable-name>
# *args

def make_pizza_toppings(*toppings):
    """Print the list of the toppings that have been requested."""
    print("Make a pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

# mixing positional and arbitraries arguments
# first POSITIONALS, for the last ARBITRARY
def make_pizza(size, *toppings):
    print("Pizza")
    print(f"Size: {size}")
    make_pizza_toppings(*toppings)