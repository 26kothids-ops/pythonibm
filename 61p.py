numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    num = float(input("Enter number: "))
    numbers.append(num)

target = float(input("Enter the number to search: "))

if target in numbers:
    print(target, "is present in the list")
else:
    print(target, "is not present in the list")

input("Press enter to exit...")
