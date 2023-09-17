current_users = ['mary', 'paul', 'Bob', 'david']
new_users = ['bob', 'PAUL', 'mary']

for new_user in new_users:
    if new_user in current_users:
        current_users.append(new_user)
        print(f"Username '{new_user}' available.")
    else:
        print(f"username '{new_user}', unavailable")