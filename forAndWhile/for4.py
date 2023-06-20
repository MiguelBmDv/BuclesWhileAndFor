n = int(input("Enter a number: "))
total = 0

for i in range(0, n+1, 2):
    total += i

print(f"The sum of your even numbers is {total}")
