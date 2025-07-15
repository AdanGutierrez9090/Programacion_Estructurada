'''
dict.-
Es un tipo de datos que se utiliza para almacenar datoss de diferente tipo de datos pero en lugar de tener como las
listas indices numericos tienen alfanumericos.Es decir algo parecido como los objetos

Tambien se conoce como un arreglo asosiativo u Objeto JSON

El diccionario es una coleccion ordenada** y modificable.
No hay miembros duplicados.
'''

import os
os.system("clear")

#lista 
# paises={"Mexico","Brazil","canada","España"}

#dict o objeto
pais_mexico={
    "nombre":"Mexico",
    "Capital":"CDMEX",
    "Poblacion":"12000000",
    "Idioma":"Español",
    "status":True}

pais_brazil={
    "nombre":"Brazil",
    "Capital":"Brazilia",
    "Poblacion":"10000000",
    "Idioma":"Portuges",
    "status":True}

pais_canada={
    "nombre":"Canada",
    "Capital":"Otawa",
    "Poblacion":"19000000",
    "Idioma":"Frances",
    "status":True}

alumno={
    "nombre":"Daniel",
    "apellido_pat":"Hernandez",
    "apellido_mat":"Gonzales",
    "carrera":"TI",
    "area":"Software Multiplataforma",
    "modalidad":"Bilingue",
    "matricula":"123456",
    "semestre":"2"
}

print(alumno)

for i in alumno:
    print(f"{i}={alumno[1]})