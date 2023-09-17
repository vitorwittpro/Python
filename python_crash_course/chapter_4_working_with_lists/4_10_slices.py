a_million = [value for value in range(1, 1000001)]

print("The first three items in the list are ([0:3]): ", a_million[0:3])
print("The first three items in the list are ([:3]): ", a_million[:3])

middle = int(len(a_million)/2)
print("The first three items in the list are ([(middle-2):(middle+1)]): ", a_million[(middle-2):(middle+1)])

print("The first three items in the list are ([0:3]): ", a_million[-3:])