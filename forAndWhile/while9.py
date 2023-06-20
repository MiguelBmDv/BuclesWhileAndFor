n = int(input("Enter how many temperatures you will input: "))
sumaTemperaturas = 0
temperaturaMaxima = None
temperaturaMinima = None

i = 1
while i < n+1:
    temperatura = float(input("Enter temperature {}: ".format(i)))
    
    sumaTemperaturas += temperatura

    if temperaturaMaxima is None or temperatura > temperaturaMaxima:  
        temperaturaMaxima = temperatura

    if temperaturaMinima is None or temperatura < temperaturaMinima:  
        temperaturaMinima = temperatura

    i += 1

temperaturaPromedio = sumaTemperaturas / n

print(f"The highest temperature is: {temperaturaMaxima}")
print(f"The lowest temperature is: {temperaturaMinima}")
print(f"The average temperature is: {temperaturaPromedio}")
