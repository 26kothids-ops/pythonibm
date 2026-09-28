numbers = []
count = int(input("Enter initial number of elements: "))

for i in range(count):
    num = float(input("Enter number: "))
    numbers.append(num)

print("Current list:", numbers)
new_num = float(input("Enter the number to insert: "))
index = int(input("Enter the position index: "))

numbers.insert(index, new_num)

print("Updated list:", numbers)

input("Press enter to exit...")
