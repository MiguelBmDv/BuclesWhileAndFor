n = int(input("Enter the number of grades: ")) 
total_sum = 0   

for i in range(1, n+1):
    grade = float(input("Enter grade {}: ".format(i))) #pd: el format es para agregar un valor cambiante dentro de un string 
    total_sum += grade  

average = total_sum / n 

print("The average is:", average)
