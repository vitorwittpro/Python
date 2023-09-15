pizzas = ['Cheese', 'Mushroom', 'Pepperoni']

friends_pizzas = pizzas[:]

pizzas.append('Chicken')
friends_pizzas.append('Ice cream')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are: ")
for pizza in friends_pizzas:
    print(pizza)