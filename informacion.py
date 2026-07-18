while True:
    print(".blasphemous\n.Lies of p\n.BFMV\n.Carlos Viola\n.Dark souls")
    opc = input("Ingrese el nombre de la opcion de la cual quiera saber informacion: ").lower()
    match opc:
        case "blasphemous": 
            print("Blasphemous es un videojuego de Metroidvania desarrollado por el estudio español The Game Kitchen, ​ y publicado por Team17. El juego fue lanzado para Nintendo Switch, Microsoft Windows, PlayStation 4 y Xbox One el 10 de septiembre de 2019.")
        case "lies of p":
            print("Lies of P es un videojuego soulslike desarrollado por Round8 Studio y publicado por Neowiz Games, ambas compañías de Corea del Sur. El juego se lanzó el 18 de septiembre de 2023 para PlayStation 4, PlayStation 5, Windows, Xbox One y Xbox Series X/S.")
        case "bfmv":
            print("Bullet For My Valentine es una banda galesa de metalcore procedente de Bridgend, Gales. El grupo se constituyó originalmente bajo el nombre de 'Jeff Killed John' en 1998, versionando canciones de Metallica y Nirvana." )
        case "carlos viola":
            print("Carlos Viola (Sevilla) es un veterano desarrollador de videojuegos, cuya trayectoria en la industria del videojuego comenzó en 2007. Actualmente es Director de Audio en The Game Kitchen desde enero de 2010 y Compositor en Nivel21 Entertainment desde enero de 2007.Como desarrollador su rol más habitual es el de Compositor. Ha participado en un total de doce videojuegos españoles, entre los que destacan Blasphemous 2 (The Game Kitchen, 2023), donde participó como Compositor, Blasphemous (The Game Kitchen, 2019), donde también participó como Compositor o Pharaonic (Milkstone Studios, 2016), donde participó como Músico.")
        case "dark souls":
            print("Dark Souls es una serie de juegos de rol de acción creada por Hidetaka Miyazaki de FromSoftware y publicada por Bandai Namco Entertainment. La serie comenzó con el lanzamiento de Dark Souls en 2011 y ha visto dos secuelas, Dark Souls II en 2014 y Dark Souls III en 2016.")
        case _:
            print("No hay informacion")
    print("Mostrar otra informacion?")
    res = input("s/otra tecla: ").lower()
    if res == "s":
        print("De acuerdo")
    else:
        break
print("ADIOS")