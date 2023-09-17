my_foods = ['pizza', 'falafel', 'carrot cake']

# copying a list using slice, here slice generate a new list
# so friend_foods assign the new list, not the pointer 'my_foods'
friend_foods = my_foods[:]

# copying a list without using slice
thirds_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# my_foods and thirds_foods point to the same list
print("\nThirds favorite foods are:")
print(thirds_foods)