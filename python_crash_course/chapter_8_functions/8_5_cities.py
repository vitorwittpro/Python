def describe_cities(city, country='Japan'):
    print(f"{city.title()}, {country.title()}")

describe_cities('Osake')
describe_cities('Paris', 'France')
describe_cities(country='germany', city='berlin')