def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# positional arguments
describe_pet('hamster', 'edi')
describe_pet('bob')

# error positional arguments
describe_pet('edi', 'hamster')

# key word argsments
describe_pet(pet_name='sophia')
describe_pet(pet_name='twelves', animal_type='monkey')