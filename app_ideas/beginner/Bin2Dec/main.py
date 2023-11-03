import re

def bin_to_dec(bin: str):
    valid = re.search("[^0-1]", bin)

    if bool(valid):
        return "Invalid"
    
    bin = bin[::-1]

    decimal = 0

    for i, bit in enumerate(bin):
        decimal += ((2 ** i) * int(bit))

    return decimal


while True:
   
    binary = input("Type a binary: ")

    if binary == 'q':
     break

    print(bin_to_dec(binary))