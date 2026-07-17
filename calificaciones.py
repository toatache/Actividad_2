while True:
    parcial = float(input("Ingrese la calif. de las actividades: "))
    examen = float(input("La calif. del examen: "))
    proyecto = float(input("Y la calif. del proyecto: "))
    if (parcial < 0 or parcial > 100) or (examen < 0 or examen > 100) or (proyecto < 0 or proyecto > 100):
        print("Ingrese valores entre 0-100")
    else:
        cal_f = (parcial * 0.4) + (examen * 0.3) + (proyecto * 0.3)
        print("La calificacion final del parcial es de: ", cal_f)    
    print("Calcular otras calificaciones? ")
    res = input("s/otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")