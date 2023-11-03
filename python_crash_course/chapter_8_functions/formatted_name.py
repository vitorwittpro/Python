def formatted_name(first, last, middle_name=''):

    full_name = f"{first} {middle_name} {last}"

    return full_name.title()

person = formatted_name('vitor', 'witt', 'hugo')

print(person)

person = formatted_name('carlos', 'santana')

print(person)