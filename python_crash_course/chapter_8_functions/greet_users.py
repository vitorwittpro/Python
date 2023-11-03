def greet_users(names):
    print("""Print a simple greeting to each user in the list.""")
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

# list
usernames = ['macduffy', 'guilty', 'percy']

greet_users(usernames)