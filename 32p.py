n = int(input("Enter the number: "))

count = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        count = count + 1

print("Count of odd numbers:", count)

input("Press enter to exit...")
