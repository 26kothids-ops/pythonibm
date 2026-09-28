numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    num = float(input("Enter number: "))
    numbers.append(num)

print("Elements of the list:")
for item in numbers:
    print(item)

input("Press enter to exit...")
