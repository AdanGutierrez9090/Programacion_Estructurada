#Utilizar e implementar una base de datos para gestionar las peliculas

import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Modificar \n\t\t 5.- Buscar peliculas \n\t\t 6.-SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            print(".:: Agregar Peliculas ::.")
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            print(".:: Eliminar Peliculas ::.") 
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            print(".:: Modificar Peliculas ::.") 
            peliculas.esperarTecla() 
        case "4":
            peliculas.modificarPelicula()
            print(".:: Consultar Peliculas ::.")
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            print(".:: Buscar Peliculas ::.") 
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
            print(".:: Vacias Peliculas ::.") 
            peliculas.esperarTecla()
        case "7":
            
            opcion=False   
            peliculas.borrarPantalla() 
            print("\n\tTerminaste la ejecucion del SW")
        case _:
             
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")