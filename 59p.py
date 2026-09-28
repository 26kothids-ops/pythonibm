numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    num = float(input("Enter number: "))
    numbers.append(num)

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)

input("Press enter to exit...")
