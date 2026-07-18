while True:
    var = None
    opcion = int(input("MENU\n 1)Celsius a Fahrenheit\n 2)Celsius a Kelvin\n 3)Salir\n Opcion: "))
    if opcion != 3:
        temp = float(input("Temperatura a convertir ej.(15): "))
    match opcion:
        case 1: 
            temp = temp * 1.8 + 32
            print("El resultado de la conversion es: ", temp)
        case 2:
            temp += 273.15
            print("El resultado de la conversion es: ", temp)
        case 3:
            var = 1
        case _:
            print("No se ingreso una opcion valida")
    if var == 1:
        break
print("ADIOS")