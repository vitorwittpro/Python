cities = {
    'tokyo': {
        'country': 'japan',
        'population': '39100000',
        'fact': 'largest city by population'
    },
    'chongqing': {
        'country': 'replublic of china',
        'population': '31020000',
        'fact': 'biggest city by area. 82.339 km²'
    },
    'new york': {
        'country': 'United States',
        'population': '846800',
        'fact': 'wealthiest city, with the highest number of millionaires in 2023 at 340000.'
    }
}

for name, city_info in cities.items():
    print(name.title())
    for key, value in city_info.items():
        print(f"\t{key.title()}: {value.title()}")