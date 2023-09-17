cities = {
    'tokyo': {
        'population': 39100000,
    },
    'chongqing': {
        'population': 31020000,
    },
    'new york': {
        'population': 8468000,
    }
}

print("\n\n\n")


scale = ''
for i in range(101):
    if str(i)[-1] == '0':
        scale += '|'
    else:
        scale += '-'
        
scaleBackground = ''

for i in range(101):
    if str(i)[-1] == '0':
        scaleBackground += '|'
    else:
        scaleBackground += ' '

scaleNumbers = ''
count = 0

for i in range(101):
    if str(i)[-1] == '0':
        rng = len(str(i))-1
        for j in range(rng):
            scaleNumbers = scaleNumbers[:-1]
        
        count = count + 1
        scaleNumbers += f"{i}"
    else:
        scaleNumbers += ' '
        
print(scale)

for name, city_info in cities.items():
    print(scaleBackground)
    cityName = f"{name}"
    cityNameLength = len(cityName) + 1

    print(f"|\033[31m{cityName.title()}\033[0m" f"{scaleBackground[cityNameLength:]}")
    list = ''
    n = int(city_info['population']/1000000)
    for star in range(n):
        list += '|'
        if star == (n-1):
            list += f" {city_info['population']}"
    population = f"{list}"
    populationLength = len(population) + 2

    print(f"|\033[32m{population.title()}\033[0m", scaleBackground[populationLength:])

print(scaleBackground)
print(scale)
print(f"\033[32m{scaleNumbers}\033[0m")


print("")
print("Scale:\033[32m Millions\033[0m")


print("\n\n\n")

