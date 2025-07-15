import os

#Crear una lista de numeros e imprimir el contenido
num=[1,2,3,4,5,6,7,8,9,10]

print(f"Los numeros son {num}")

for i in num:
    print(i)

for i in range  (0,len(num)):
    print(num[i])

#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una paalbra
# y el numero de veces que sse encontro
os.system("cls")
palabras=["hola","pelota","Peru","Juego"]



coincidencia= "Peru" in palabras
if coincidencia:
    print("Si se encotro la coincidencia")
else:
    print("No se encontro ninguna coincidencia")

print(palabras)
palabra=input("Dame la palabra que desdeas buscar:")

#1er Forma

if palabra in palabras:
    print("Si se encotro la coincidencia")
    print(f"El numero de veces que se e ncontro la palabra es: {palabras.count(palabra)}")
else:
    print("No se encontro ninguna coincidencia")



#3ra Forma
encontro=False
for i in range(0,len(palabras)):
    if palabras[i] == palabra:
        encontro=True
        #print("Si se encotro la coincidencia")

         #print("No se encontro ninguna coincidencia")
if encontro:
    print("Si se encotro la coincidencia")
else:
    print("No se encontro ninguna coincidencia")


#2da forma

for i in palabras:
    if  i == palabra:
        encontro=True

if encontro:
    print("Si se encotro la coincidencia")
else:
    print("No se encontro ninguna coincidencia")


input("Oprima tecla")

#Ejemplo 3 Añadir elementos a una lista
os.system("cls")
numeros=[]
print(numeros)

opc=True
while opc:
    numero=float(input("Dame un numero entero o decimal: ")) 
    numeros.append(numero)
    resp=input("Deseas agregar otro numero?: ").lower()
    if resp=="si":
        opc=True
    else:
        opc=False

print(numeros)

input("Oprima una tecla para continuar")

#Ejemplo 4 crear una lista que sea multidimensional que sea una agenda
agenda=[
    ["Carlos","6181234567"],
    ["Alberto","6671234567"],
    ["Martin","6785678923"]
        ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena += f"{agenda[r][c]},"
    cadena+="\n"
print(cadena)

