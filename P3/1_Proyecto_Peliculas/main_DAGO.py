'''
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menú de opciones para agregar, eliminar, modificar y consultar peliculas

NOTAS: 
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar diccionarios para almacenar los siguientes atributos: (nombre, categoria, clasificación, género, idioma) de las peliculas.
3.- Utilizar e implementar una BD para gestionar las peliculas
'''


import peliculas_DAGO

opcion=True
while opcion:
    peliculas_DAGO.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar  \n\t\t 4.- Modificar caracteristicas  \n\t\t 5.- Buscar \n\t\t 6.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_DAGO.crearPeliculas()
            print(".:: Agregar Peliculas ::.")
            peliculas_DAGO.esperarTecla()
        case "2":
            peliculas_DAGO.borrarPeliculas()
            print(".:: Eliminar Peliculas ::.") 
            peliculas_DAGO.esperarTecla()
        case "3":
            peliculas_DAGO.mostrarPeliculas()
            print(".:: Modificar Peliculas ::.") 
            peliculas_DAGO.esperarTecla()
                
        case "4":
            peliculas_DAGO.modificarCaracteristicaPeliculas()
            print(".:: Consultar Peliculas ::.")
            peliculas_DAGO.esperarTecla()
        
        case "5":
            peliculas_DAGO.buscarPeliculas()
            peliculas_DAGO.esperarTecla()

        case "6":
            
            opcion=False   
            peliculas_DAGO.borrarPantalla() 
            print("\n\tTerminaste la ejecucion del SW")
        case _:
             
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")