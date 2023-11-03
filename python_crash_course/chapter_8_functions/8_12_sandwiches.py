# arbitrary arguments *args
def make_sandwiches(*ingredients):
    print("""Preparing your sandwiche...""")
    for ingredient in ingredients:
        print(f"\tAdding {ingredient}")

    print("finished")
    print(f"Ingredients: {ingredients}")

make_sandwiches('Cheese')
make_sandwiches('Cheese', 'Tomato')
make_sandwiches('Cheese', 'Chicken', 'Tomato')