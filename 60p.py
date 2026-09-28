numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    num = int(input("Enter number: "))
    numbers.append(num)

odd_count = 0
for num in numbers:
    if num % 2 != 0:
        odd_count = odd_count + 1

print("Count of odd numbers:", odd_count)

input("Press enter to exit...")
