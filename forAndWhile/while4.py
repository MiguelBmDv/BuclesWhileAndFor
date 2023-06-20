num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 < num2:
    i = num1
    while i <= num2:
        print(i)
        i += 1
elif num2 < num1:
    i = num2
    while i <= num1:
        print(i)
        i += 1
else:
    print("Your numbers are equal or not valid")
