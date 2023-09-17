dimensions = (200, 100)

print(dimensions[0])
print(dimensions[1])

# error, tuples are immutable
# dimensions[0] = 300

# create a one element tuple, it doesn't make sense
one_el = (3,)
print(one_el[0], "\n")

print("Writing over a tuple")
print("Original dimensions:")
# looping
for dimension in dimensions:
    print(dimension)

# writing over a tuple
dimensions = (400, 500)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)