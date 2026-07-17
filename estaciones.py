while True:
    mes = int(input("Ingrese el numero del mes: "))
    match mes:
        case 12 | 1 | 2: 
            estacion = "Invierno"
        case 3 | 4 | 5:
            estacion = "Primavera"
        case 6 | 7 | 8:
            estacion = "Verano"
        case 9 | 10 | 11:
            estacion = "Otoño"
        case _:
            estacion = None
    if estacion != None:
        print("La estacion de este momento es: " + estacion)
    else:
        print("No se ingreso el numero de un mes")
    print("Comprobar de nuevo?")
    res = input("s/otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")