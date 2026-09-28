numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    num = float(input("Enter number: "))
    numbers.append(num)

total = 0
for num in numbers:
    total = total + num

print("Sum of list elements:", total)

input("Press enter to exit...")
