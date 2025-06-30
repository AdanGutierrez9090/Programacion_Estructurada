'''Crear un proyecto que permita gestionar(administrar)peliculas, colocar un menu de opciones para colocar, 
eliminar, modificar y consultar peliculas

Notas
1-Usar funciones y mandar llamar desde otro archivo
2-Usar listas para almacenar los nombres de peliculas
'''
import peliculas

Peliculas=["Sharknado","La toalla del mojado","Shrek 2"]
opcion=True
while opcion:
    peliculas.borrarPantalla()
    opc=int(input("Seleccione la opcion que desea realizar:" \
    "\n 1.-Agregar " \
    "\n 2.-Modificar " \
    "\n 3.-Consultar " \
    "\n 4.-Eliminar" 
    "\n 5.- Salir " )    
            )

    match opc:
        case 1:
            Peliculas.append(peliculas.agregarPelicula())
            print(Peliculas)
            peliculas.espereTecla()
            opcion=False

        case 2:
            ind,mod=peliculas.modificar()
            Peliculas[ind]=mod
            print(Peliculas)
            peliculas.espereTecla()
            opcion=False

        case 3:
            buscar=peliculas.consultar()
            resp= buscar in Peliculas
            if resp:
                print(f"Si se encontro {buscar}")
            else:
                print("No se encontro")
            peliculas.espereTecla()
            opcion=False

        case 4:
            borrar=peliculas.eliminar()
            Peliculas.pop(borrar)
            print(Peliculas)  
            peliculas.espereTecla()
            opcion=False
        case 5:
            opcion=False

        case _:
            print("Opcion no valida verifique de nuevo")
            opcion=False


