n = int(input("Enter the number: "))
original = n
digits = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** digits
    n //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

input("Press enter to exit...")
