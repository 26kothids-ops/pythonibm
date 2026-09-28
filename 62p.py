items = []
count = int(input("Enter the number of items: "))

for i in range(count):
    val = input("Enter item: ")
    items.append(val)

print("Current list:", items)
item_to_remove = input("Enter the item to remove: ")

if item_to_remove in items:
    items.remove(item_to_remove)
    print("Updated list:", items)
else:
    print("Item not found in list")

input("Press enter to exit...")
