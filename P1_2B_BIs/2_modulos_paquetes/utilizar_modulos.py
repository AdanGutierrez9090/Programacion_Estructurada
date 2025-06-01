import modulos
#1er forma de utilizar modulos
modulos.borrarPantalla
print(modulos.saludar("Maximo Gamon"))

#2da forma de utilizar modulos
from modulos import saludar,borrarPantalla

#borrarPantalla()
print(saludar("Daniel Contreras Renecio"))

nombre=input("Ingrese el nombre de contacto: ")
telefono=input("Ingrese su numero de telefono con clave lada: ")
nom,tel=modulos.solicitarDatos4(nombre,telefono)
print(f"\t Nombre completo: {nom}\n\t Telefono: {tel}")

