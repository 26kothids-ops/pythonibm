numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    num = float(input("Enter number: "))
    numbers.append(num)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)

input("Press enter to exit...")
