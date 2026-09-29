n = int(input("Enter the number: "))
original = n
total = 0

while n > 0:
    digit = n % 10
    factorial = 1

    for i in range(1, digit + 1):
        factorial *= i

    total += factorial
    n //= 10

if total == original:
    print("Strong number")
else:
    print("Not a strong number")

input("Press enter to exit...")
