requested_seats = input("How many people are in their dinner group? ")
requested_seats = int(requested_seats)

if requested_seats > 8:
    print("Sorry, you will have to wait for a table.")
else:
    print("Your table is ready.")