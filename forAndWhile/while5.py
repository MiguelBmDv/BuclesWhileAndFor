n = int(input("Enter the number of invoices (0 to finish): "))
total = 0
counter = 1

while counter <= n:
    amount = float(input("Enter the amount of invoice {} (0 to finish): ".format(counter)))
    total += amount
    counter += 1

    if amount == 0:
        print("Process finished")
        break

if total >= 1 and total <= 999:
    print("Total to pay:", total)
elif total > 1000:
    discount = total * 0.1
    total -= discount
    print("Total to pay:", total)
else:
    if n == 0:
        print("Process finished")
