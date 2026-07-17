while True:
    edad = float(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    elif edad > 0:
        print("Eres menor de edad")
        print(f"Te faltan: {18 - edad} años para ser mayor de edad")    
    print("Verificar otro? ")
    res = input("s/otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")