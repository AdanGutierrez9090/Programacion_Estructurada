#Un modulo es simplemente un archivo con estension .py
# que contiene codigo de python(funciones,clases,variables,etc.)

#Un paquete es una carpeta que contiene varios modulos(archivos .py)
#  y un archivo especial llamado __init__.py, que le indica a python
#  que esa carpeta debe tratarse como un paquete

#1.-  1.- Funcion que no recibe parametros y no regresa valor

import os

def solicitarDatos1():
    nombre=input("Nombre:")
    tel=input("Telefono:")
    print(f"Soy funcion 1 El nombre es:{nombre} y su telefono es:{tel}")

# 3.- Funcion que recibe parametros y no regresa valor
def solicitarDatos3(nombre,tel):
    nom=nombre
    telefono=tel
    print(f"Soy funcion 3 El nombre es:{nom} y su telefono es:{telefono}")

    

#2.- Funcion que no recibe parametros y regresa valor
def solicitarDatos2():
    nombre=input("Nombre:")
    tel=input("Telefono:")
    
    return nombre,tel


#4.- Funcion que recibe parametros y regresa valor
def solicitarDatos4(nombre,tel):
    nom=nombre
    telefono=tel
    return nom,telefono

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("..Oprima una tecla para continuar...")


def saludar(nombre):
    nom=nombre
    return f"Hola, bienvenido: {nom}"

