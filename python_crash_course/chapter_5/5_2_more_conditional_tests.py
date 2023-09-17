name = "marie"

if name == "marie":
    print(f"\n{name} == 'marie'")
    print(name == 'marie')

if name != "john":
    print(f"\n{name} != 'john'")
    print(name != 'john')


number = 89

if number <= 100:
    print(f"\n{number} <= 100")
    print(number <= 100)

if number == 89:
    print(f"\n{number} == 100")
    print(number == 100)

if number != 100:
    print(f"\n{number} != 100")
    print(number != 100)

if not number >= 100:
    print(f"\nnot {number} >= 100")
    print(not number >= 100)



list = ['item1', 'item2', 'item3']

print(list)

for item in list:
    if item == 'item2':
        print(f"Item '{item}' is in list, using 'for'")

if 'item2' in list:
    print(f"Item 'item2' is in list, using 'in'")

if not 'item4' in list:
    print(f"Item 'item4' is not in list")