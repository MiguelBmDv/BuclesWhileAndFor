n = int(input("Enter the number of temperatures: "))  
sumaTemperaturas = 0  
temperaturaMaxima = None  
temperaturaMinima = None  

for i in range(n):
    temperatura = float(input("Enter temperature {}: ".format(i+1)))  
    
    sumaTemperaturas += temperatura   

    if temperaturaMaxima is None or temperatura > temperaturaMaxima:  
        temperaturaMaxima = temperatura

    if temperaturaMinima is None or temperatura < temperaturaMinima:  
        temperaturaMinima = temperatura

temperaturaPromedio = sumaTemperaturas / n  

print(f"The highest temperature is: {temperaturaMaxima}")
print(f"The lowest temperature is: {temperaturaMinima}")
print(f"\nThe average temperature is: {temperaturaPromedio}")

