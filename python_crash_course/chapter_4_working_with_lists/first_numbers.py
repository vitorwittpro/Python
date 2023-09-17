print("Starting 1, stop 4, but it isn't printed. Let's fix that.")
for value in range(1, 4):
    print(value)


print("\nStarting 1, stop 5, to print 4")
for value in range(1, 5):
    print(value)



print("\nPrinting from 0 to 3, passing only one argument, 4 in this case.")
for value in range(4):
    print(value)

# creating a list of numbers
numbers = list(range(1, 10))
print(numbers)