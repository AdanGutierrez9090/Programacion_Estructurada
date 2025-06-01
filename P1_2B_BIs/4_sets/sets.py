'''
Es un tipo de dato para tener una coleccion de valores pero no tiene ni indice ni orden

Set es una coleccion desordenada, inmutable* y no indexada.
No hay miembros duplicados.


'''
import os
os.system("cls")

personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Choche")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

varios={3.12,3,True,"Hola"}
print(varios)


#Ejemplo Crear un programa que solicite los emails de los alumnos de la UTD almacenar en una lista 
# y posteriormente mostrar en pantalla los emails sin duplicados
os.system("cls")
opc="si"
emails=[]
while opc == "si":
    emails.append(input("Dame el emial: "))

    opc=input("¿Deseas solicitar otro email (si/no?)").lower

#Impprimir los emails sin duplicados 

print(emails)


