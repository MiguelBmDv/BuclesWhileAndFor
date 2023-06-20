n = int(input("Enter the number of students: "))

notaMaxima = None
notaMinima = None  
sumaNotas = 0  

for i in range(n):
    print("Student", i + 1)
    sumaEstudiante = 0 

    for j in range(4):
        nota = float(input("Enter the grade: "))  

        sumaEstudiante += nota  

        if notaMaxima is None or nota > notaMaxima: 
            notaMaxima = nota

        if notaMinima is None or nota < notaMinima:  
            notaMinima = nota

    promedioEstudiante = sumaEstudiante / 4  
    sumaNotas += sumaEstudiante  
    print(f"The individual average is: {promedioEstudiante}\n")

promedioTotal = sumaNotas / (n * 4) 
print("Within the course, the following averages are:\n ")
print(f"The highest grade is: {notaMaxima}")
print(f"The lowest grade is: {notaMinima}")
print(f"The overall average is: {promedioTotal}")
