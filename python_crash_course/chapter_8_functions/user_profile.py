# keywords arguments **kwargs

def build_profile(first, last, **user_info):
    """Build a dictionary that contains everythong we know about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('Vitor', 'Witt', location='Camboriú', job='developer-web')

print(user_profile)