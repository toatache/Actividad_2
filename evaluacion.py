while True:
    calif = float(input("Ingresa la calif. final : "))
    if calif >= 90 and calif <= 100:
        print("Calificacion: A")
    elif calif >= 80 and calif <= 90:
        print("Calificacion: B")
    elif calif >= 70 and calif <= 80:
        print("Calificacion: C")
    elif calif >= 60 and calif <= 70:
        print("Calificacion: D")
    elif calif > 0 and calif <= 60:
        print("Calificacion: F")
    else:
        print("Valor no aceptado")
    print("Comprobar otra calif.? ")
    res = input("s/otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")