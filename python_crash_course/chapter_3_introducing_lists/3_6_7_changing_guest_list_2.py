invites = ['Tiberon', 'Alan', 'Marcelo']

def invite():
    for invite in invites:
        print(f"Come on {invite}, let's DINNER")

guest_cant_make = 'Tiberon'

invites.remove(guest_cant_make)
invites.append('Jhonathan')

invite()

print("\nbigger table = more people\n")

middle = int(len(invites)/2)

invites.insert(0, 'Felipe')
invites.insert(middle, 'Henrique')
invites.insert(len(invites), 'Leo')

invite()

print("\nOnly two guests\n")

while len(invites) > 2:
    invites.pop()
    print(f"Sorry, you're out")

invite()

del invites[0]
del invites[0]

print(invites)