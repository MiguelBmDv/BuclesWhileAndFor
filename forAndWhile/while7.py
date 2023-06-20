sum = 0
number = int(input("Enter an integer number (0 to finish): "))

while number != 0:
    sum += number
    number = int(input("Enter an integer number (0 to finish): "))

print(f"The sum of the entered numbers is {sum}")
