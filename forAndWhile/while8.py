n = int(input("Enter an integer greater than zero: "))
divisor = 1

while divisor <= n:
    if n % divisor == 0:
        print(divisor)
    divisor += 1

if n <= 0:
    print("Please enter a number greater than 0")
