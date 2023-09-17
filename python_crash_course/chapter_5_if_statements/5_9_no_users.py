# usernames = ['mary', 'paul', 'admin', 'robet', 'bob']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Welcome back, {username}, would you like to see your reports?")
        else:
            print(f"Welcome back, {username}")
else:
    print("We need to find some users!")