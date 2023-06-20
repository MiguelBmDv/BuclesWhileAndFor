table = int(input("Enter the number of a multiplication table you want (1 to 10): "))

for i in range(1, 11):
    result = table * i
    print(f"{table} x {i} = {result}")
