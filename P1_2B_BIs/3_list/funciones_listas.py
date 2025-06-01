'''
List(Array)
Son colleciones o conjunto de datos/valores bajo
 un mismo nombre, para acceder a los valores se hace un indice numerico

 Nota:sus valores si son modificables

 La lista es una coleccion ordenada y modificable.
 Permite miembros duplicados
'''
import os
os.system("cls")

#Funciones mas comunes en las listas

paises=["Mexico","Brsasil","España","Canada"]

numeros=[23,12,100,34]

#Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)

print(paises)
paises.sort()
print(paises)

#añadir o ingresar o insertar elementos a una listaa

#1er Forma
paises.append("Honduras")
print(paises)
#2da Forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o borrar o quitar elementos de una lista

#1er Forma con el indice
paises.pop(1)
print(paises)

#2da Forma con el valor
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista

print("Brasil" in paises)
#1er Forma
resp="Brasil" in paises
if resp:
    print("Si encontre el pais")
else:
    print("No se encontro el pais")

#2da Forma
pais_buscar=input("Dame el pais a buscar")
for i in range(0,len(paises)):
    if paises[i] ==pais_buscar:
       print("Si encontre el pais")
    else:
        print("No se encontro el pais")

#Cuantas veces aparece un elemento dentro de la lista

print(f"Este numero aparece:{numeros.count(12)} vez o veces")

numeros.append(12)
print(f"Este numero aparece:{numeros.count(12)} vez o veces")

#Identificar o conocer el indice de un valor

indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#Recorrer los valores de la lista

#1er forma con los valores
for i in paises:
    print(i)

#2da Forma con los indices
for i in range(0,len(paises)):
    print(f"El valor {i} es: {paises[i]}")

#Unir contenido de listas
print(paises)
print(numeros)

paises.extend(numeros)
print(paises)
