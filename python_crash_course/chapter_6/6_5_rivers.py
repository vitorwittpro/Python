rivers = {
    'nile': 'Egypt',
    'amazonas': 'Brasil',
    'yangtze': 'China',
}

for river, country in rivers.items():
    print(f"{river.title()} river runs through {country.title()}")

for river in rivers:
    print(f"{river.title()} river")

for country in rivers.values():
    print(f"{country.title()}")