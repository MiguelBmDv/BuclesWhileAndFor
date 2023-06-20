n = int(input("Enter the number of grades: "))
sum_grades = 0
counter = 1

while counter <= n:
    grade = float(input("Enter grade {}:".format(counter)))
    sum_grades += grade
    counter += 1

average = sum_grades / n
print("The average grade is:", average)
