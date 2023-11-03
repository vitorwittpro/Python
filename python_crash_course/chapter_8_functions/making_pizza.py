# importing an entire module
# import pizza

# pizza.make_pizza(12, 'Cheese')


# importing specific functions, adding alias
# from pizza import make_pizza as mp

# mp(16, 'Cheese', 'Chicken')


# module alias
# import pizza as p

# p.make_pizza(12, 'Cheese', 'Pepperoni')


# Importing all functions in a module
from pizza import *

make_pizza(12, 'Cheese', 'Pepperoni')
make_pizza_toppings('Ice cream')