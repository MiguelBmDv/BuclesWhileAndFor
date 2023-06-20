n = int(input("Enter a number: "))

if n >= 10:
    total = 1
    multi = 1
    while multi <= n:
        total *= multi
        multi += 1
    print(f"The multiplication of the first {n} numbers is: {total}")

elif 0 < n < 10:
    total = 0
    suma = 1
    while suma <= n:
        total += suma
        suma += 1
    print(f"The sum of the first {n} numbers is: {total}")
else:
    print("Enter a positive number greater than zero")
