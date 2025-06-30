def borrarPantalla():
    import os
    os.system("cls")

def espereTecla ():
    input("Presione una tecla para continuar...")

def agregarPelicula():
    borrarPantalla()
    pelicula=input("Ingrese el elemento a agregar: ")
    return pelicula
    
def modificar():
    borrarPantalla()
    ind=int(input("Ingrese el indice de la pelicula a modificar: "))
    mod=input("Ingrese el nuevo valor que cambiara por en el indice que proporciono: ")
    return ind, mod

def consultar():
    borrarPantalla()
    buscar=input("Ingrese la pelicula que desea consultar: ")
    return buscar

def eliminar():
    borrarPantalla()
    borrar=int(input("Ingrese el indice del elemento que quiere eliminar: "))
    return borrar