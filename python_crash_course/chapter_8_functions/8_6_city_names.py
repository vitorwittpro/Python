def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'

cities_list = {'japan': 'nagasaki', 'brasil': 'curitiba','south korea': 'seoul'}

def print_cities(cities):
    for country, city in cities.items():
        print(city_country(city, country))

print_cities(cities_list)