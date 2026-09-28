items = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    val = input("Enter item: ")
    items.append(val)

for index in range(len(items)):
    print("Index", index, ":", items[index])

input("Press enter to exit...")
