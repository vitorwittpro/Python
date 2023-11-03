def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user = build_profile('Vitor', 'Witt', location='SP', job='developer-web', hobby='reading')

for key, value in user.items():
    print(f"\t{key}: {value}")