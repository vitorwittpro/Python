ages = [1, 3, 12, 19, 64, 98]

for age in ages:
    if age < 2:
        print("baby")
    elif age < 4:
        print("toddler")
    elif age < 13:
        print("kid")
    elif age < 20:
        print("teenager")
    elif age < 65:
        print("adult")
    else:
        print("elder")
