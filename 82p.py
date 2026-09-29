start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for n in range(start, end + 1):
    if n >= 2:
        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            print(n)

input("Press enter to exit...")
