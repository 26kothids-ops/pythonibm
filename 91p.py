a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("LCM:", lcm)

input("Press enter to exit...")
