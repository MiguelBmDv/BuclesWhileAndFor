n = int(input("Enter a number: "))
total = 0
impares = 0

for i in range(1, n+1, 2):
    total += i
    impares += 1

print(f"The sum of your odd numbers is {total}")
print(f"The number of odd numbers summed is: {impares}")
