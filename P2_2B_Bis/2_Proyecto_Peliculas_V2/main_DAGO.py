

import peliculas_DAGO

opcion=True
while opcion:
    peliculas_DAGO.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Agregar Caracteristicas \n\t\t 5.- Modificar caracteristicas \n\t\t 6.- Borrar caracteristias \n\t\t 7.- SALIR ")
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
            peliculas_DAGO.agregarCaracteristicaPeliculas()
            print(".:: Consultar Peliculas ::.")
            peliculas_DAGO.esperarTecla()
        case "5":
            peliculas_DAGO.modificarCaracteristicaPeliculas()
            print(".:: Buscar Peliculas ::.") 
            peliculas_DAGO.esperarTecla()
        case "6":
            peliculas_DAGO.borrarCaracteristicaPeliculas()
            peliculas_DAGO.esperarTecla()
            print(".:: Vacias Peliculas ::.") 
            peliculas_DAGO.esperarTecla()
        case "7":
            
            opcion=False   
            peliculas_DAGO.borrarPantalla() 
            print("\n\tTerminaste la ejecucion del SW")
        case _:
             
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")