invites = ['Tiberon', 'Alan', 'Marcelo']

def invite():
    for invite in invites:
        print(f"Come on {invite}, let's DINNER")

invite()

guest_cant_make = 'Tiberon'

new_guest = 'Jhonathan'

invites.remove(guest_cant_make)
invites.append(new_guest)

invite()