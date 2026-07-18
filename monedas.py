while True:
    opcion = int(input("MENU\n 1)USD 2)EUR 3)THB 4)JPY 5)KRW\n 6)AUD 7)PEN 8)CAD 9)VES 10)ARS\n Opcion: "))
    if opcion >= 1 and opcion <= 10:
        monto = float(input("Cantidad a convertir? "))
    match opcion:
        case 1: 
            monto /= 16.5 
            mon = "USD"
        case 2:
            monto /= 18.0
            mon = "EUR"
        case 3:
            monto /= 0.45
            mon = "THB"
        case 4: 
            monto /= 0.12 
            mon = "JPY"
        case 5: 
            monto /= 0.013
            mon = "KRW"
        case 6: 
            monto /= 11.5
            mon = "AUD"
        case 7: 
            monto /= 2.8
            mon = "PEN"
        case 8: 
            monto /= 8.2 
            mon = "CAD"
        case 9: 
            monto /= 0.0023
            mon = "VES"
        case 10: 
            monto /= 0.046 
            mon = "ARS"
        case _:
            monto = 0
            mon = ""
            print("No se ingreso una opcion valida")
    print("Eso equivalen a ", monto, mon)
    print("Convertir otra cantidad?")
    res = input("s/otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")