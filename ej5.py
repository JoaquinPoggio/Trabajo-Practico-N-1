def romano_decimal(romano):
    numeros_romanos = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    if len(romano) == 1:
        return numeros_romanos[romano]
    
    if numeros_romanos[romano[0]] < numeros_romanos[romano[1]]:
        return numeros_romanos[romano[1]] - numeros_romanos[romano[0]] + romano_decimal(romano[2:])
    else:
        return numeros_romanos[romano[0]] + romano_decimal(romano[1:])

numero_romano = input("Ingrese un numero romano cualquiera: ") 
print("El número romano ingresado", numero_romano, "es el numero", romano_decimal(numero_romano), "en decimal.")
