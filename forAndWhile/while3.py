n = int(input("Enter a number: "))
total = 0
impares = 0
i = 1

while i <= n:
    total += i
    impares += 1
    i += 2

print(f"The sum of your odd numbers is {total}")
print(f"The number of odd numbers summed is: {impares}")
