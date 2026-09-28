numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    num = float(input("Enter number: "))
    numbers.append(num)

print("Original list:", numbers)

numbers.reverse()

print("Reversed list:", numbers)

input("Press enter to exit...")
