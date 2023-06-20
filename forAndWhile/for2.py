n = int(input("Enter a number: "))

if n >= 10:
    total = 1
    for multi in range(1, n + 1):
        total *= multi
    print(f"The multiplication of the first {n} numbers is: {total}")

else:
    if n > 0 and n < 10:
        total = 0
        for suma in range(1, n + 1):
            total += suma
        print(f"The sum of the first {n} numbers is: {total}")
    else:
        print("Enter a positive number")
