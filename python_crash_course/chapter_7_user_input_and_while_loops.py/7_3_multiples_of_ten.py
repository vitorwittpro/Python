number = input("Type a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple of ten.")
else:
    print(f"{number} is NOT multiple of ten.")