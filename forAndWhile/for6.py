num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 < num2:
    for i in range(num1, num2+1):
        print(i)
elif num2 < num1:
    for i in range(num2, num1+1):
        print(i)
else:
    print("Your numbers are equal or not valid.")
