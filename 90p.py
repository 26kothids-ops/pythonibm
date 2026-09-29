a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

while b != 0:
    a, b = b, a % b

print("GCD:", a)

input("Press enter to exit...")
