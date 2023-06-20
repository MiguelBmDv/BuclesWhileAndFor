n = int(input("Enter the number of students: "))

maxGrade = None
minGrade = None
totalGrade = 0

i = 0
while i < n:
    print("Student", i + 1)
    totalStudentGrade = 0
    l = 1

    while l < 3+1:
        grade = float(input("Enter the {} grade: ".format(l)))

        totalStudentGrade += grade

        if maxGrade is None or grade > maxGrade:
            maxGrade = grade

        if minGrade is None or grade < minGrade:
            minGrade = grade

        l += 1

    studentAverage = totalStudentGrade / 3
    totalGrade += totalStudentGrade
    print(f"\nThe individual average is: {studentAverage}")

    i += 1

classAverage = totalGrade / (n * 3)
print("\n Within the class, the following averages are: ")
print(f"The highest grade is: {maxGrade}")
print(f"The lowest grade is: {minGrade}")
print(f"The overall average is: {classAverage}")
