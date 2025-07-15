'''
Crear un programa que calcule e imprima las tablas de multiplicar del cualquier numero

Requisitos:

2.- Sin funciones
'''
#version 4
def tablaMultiplicar(num):
    for i in range(1,11):
        mult=num*i
        print(f"{num} x {i} = {mult}")
        return mult
        

#Version 4 profe
def tabla(numero):
    num=numero
    respuesta=""
    for i in range(1,11):
        mult=num*i
        respuesta += f"\t{num} X {i} = {mult}\n"
    return respuesta

numero = int(input("Dame le numero de la tabla de multiplicar a calcular: "))
print(f"Tabla de muñtiplicar del {numero}")
resultado=tabla(numero)
print(f"{resultado}")





#Version 2
num=int(input("Dame el numero de de la tabla de multiplicar a calcular: "))

for i in range(1,11):
    res=num*i
    print(f"{num} x {i} = {res}")

#Version 3
i=1
while i<=10:
    res=num*i
    print(f"{num} x {i} = {res}")
    i+=1




#Version 1

'''
num=int(input("Dame el numero de de la tabla de multiplicar a calcular: "))

res=num*1
print(f"{num} *1 = {res}

res=num*2
print(f"{num}*2 = {res})

res=num*3
print(f"{num}*3 = {res})

res=num*4
print(f"{num}*4 = {res})

res=num*5
print(f"{num}*5 = {res})

res=num*6
print(f"{num}*6 = {res})

res=num*7
print(f"{num}*7 = {res})

res=num*8
print(f"{num}*8 = {res})

res=num*9
print(f"{num}*9 = {res}")

res=num*10
print(f"{num}*10 = {res}")
'''