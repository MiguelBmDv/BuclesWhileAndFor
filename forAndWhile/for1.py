n = int(input("Enter your number: "))
total = 0

for numbers in range(1, n + 1):
    total += numbers
print(f"The sum of the first {n} numbers is {total}")
