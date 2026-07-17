while True:
    precio = float(input("Ingresa el precio del articulo : "))
    if precio >= 800:
        descuento = .25
    elif precio >= 500:
        descuento = .20
    elif precio >= 200:
        descuento = .10
    elif precio >= 100:
        descuento = .05
    else:
        descuento = 0
    precio_f = precio - (precio * descuento)
    print("El precio final del articulo es de: ", precio_f)
    print("Checar otro articulo?")
    res = input("s/otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")