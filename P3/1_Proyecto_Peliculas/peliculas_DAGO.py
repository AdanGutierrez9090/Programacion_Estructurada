import mysql.connector
from mysql.connector import Error

#Dict u objeto  para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma)

#peliculas={
 #  "nombre":"",
  # "categoria":"",
   #"clasificacion":"",
   #"genero":"",
   #"idioma":","
   #""
#}




pelicula={}
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t ...Oprima cualquier tecla para continuar ...")  

def conectar():
   try:
         conexion=mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="",
         database="bd_peliculas"
      )
         return conexion
   except Error as e:
      print(f"El error que sucedio es: {e}")
      return None

def crearPeliculas():
  conexionBD=conectar()
  if conexionBD!= None:
    borrarPantalla()
    print(".:: \U0001F4DD Alta de Peliculas \U0001F4DD ::. \n ")
    pelicula.update({"nombre":input("Ingrese  el nommbre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingrese  la categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingrese  la clasificación : ").upper().strip()})
    pelicula.update({"genero":input("Ingrese el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingrese el idioma: ").upper().strip()})


    #### Agregar Registro a la base de datos
    try:
        cursor=conexionBD.cursor()
        sql="insert into peliculas (id,nombre,categoria,clasificacion,genero,idioma) values(null,%s,%s,%s,%s,%s)"
        val=(pelicula['nombre'], pelicula['categoria'],pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])

        cursor.execute(sql,val)
        conexionBD.commit()

        input("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO¡ \u2705 :::")


    except Error as e:
        print("Error al intentar insertar un registro en la DB")




def mostrarPeliculas():
    borrarPantalla()
    conexionDB=conectar()
    if conexionDB != None:
        print("\n\t.:: Consultar o Mostrar las películas ::.\n")

        cursor=conexionDB.cursor()
        sql="SELECT * FROM `peliculas`"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t Mostrar peliculas")
            print(f"{"ID":<10} {"Nombre":<15} {"Clasificacion":<15} {"Genero":<15} {"Idioma":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10} a{fila[1]:<15} a{fila[2]:<15} a{fila[3]:<15} a{fila[4]:<15} a{fila[5]:<15}")
            print(f"-"*80)

        else:
            print("\t .:: \u26A0 No hay peliculas en el sistema \u26A0 ::.")

     


    esperarTecla()


def buscarPeliculas():
    borrarPantalla()
    conexionDB=conectar()
    if conexionDB != None:
        print("\n\t.:: Buscar película ::.\n")

        cursor=conexionDB.cursor()
        nombre=input("Dame el nombre de la pelicula a buscar: ").upper().strip()
        sql="SELECT * FROM peliculas WHERE nombre= %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\n\t Mostrar peliculas")
            print(f"{"ID":<10} {"Nombre":<15} {"Categoria":<15} {"Clasificacion":<15} {"Genero":<15} {"Idioma":<15}")
            print(f"-"*80)
            for filas in registros:
                print(f"{filas[0]:<10} {filas[1]:<15} {filas[2]:<15} {filas[3]:<15} {filas[4]:<15} {filas[5]:<15}")
            print(f"-"*80)

        else:
            print("\t .:: \u26A0 No hay peliculas en el sistema \u26A0 ::.")


    esperarTecla()


def borrarPeliculas():
    borrarPantalla()
    conexionDB=conectar()
    if conexionDB != None:
        print("\n\t.:: Borrar película ::.\n")

        cursor=conexionDB.cursor()
        nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
        sql="SELECT * FROM peliculas WHERE nombre= %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
             print("\n\t Mostrar peliculas")
             print(f"{"ID":<10} {"Nombre":<15} {"Categoria":<15} {"Clasificacion":<15} {"Genero":<15} {"Idioma":<15}")
             print(f"-"*80)
             for filas in registros:
                print(f"{filas[0]:<10} {filas[1]:<15} {filas[2]:<15} {filas[3]:<15} {filas[4]:<15} {filas[5]:<15}")
                print(f"-"*80)

                resp=input(f"¿Deseas borrar la pelicula de {nombre}(si/no)?").lower().strip()
                if resp=="si":
                    sql="delete from peliculas where nombre=%s"
                    val=(nombre,)
                    cursor.execute(sql,val)
                    conexionDB.commit()
                    print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO¡ \u2705 :::")
        else:
            print("\t .:: \u26A0 No hay peliculas en el sistema \u26A0 ::.")

    esperarTecla()



def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Características de una Película  ::.\n")
    conexionDB=conectar()
    if conexionDB != None:
        print("\n\t.:: Modificar película ::.\n")

        cursor=conexionDB.cursor()
        nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
        sql="SELECT * FROM peliculas WHERE nombre= %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        print("\n\t Mostrar peliculas")
        print(f"{"ID":<10} {"Nombre":<15} {"Categoria":<15} {"Clasificacion":<15} {"Genero":<15} {"Idioma":<15}")
        print(f"-"*80)
        for filas in registros:
            print(f"{filas[0]:<10} {filas[1]:<15} {filas[2]:<15} {filas[3]:<15} {filas[4]:<15} {filas[5]:<15}")
            print(f"-"*80)


        if registros:
            resp=input(f"¿Deseas modificar la pelicula de {nombre}si/no?").lower().strip()
            if resp=="si":
                pelicula["nombre"]=input("\U0001F4DD Nombre").upper().strip()
                pelicula["categoria"]=input("\U0001F4DD categoria").upper().strip()
                pelicula["clasificacion"]=input("\U0001F4DD clasificacion").upper().strip()
                pelicula["genero"]=input("\U0001F4DD genero").upper().strip()
                pelicula["idioma"]=input("\U0001F4DD idioma").upper().strip()
         


                sql="update peliculas set nombre=%s,categoria=%s,clasificacion=%s,genero=%s,idioma=%s where nombre=%s"
                val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"],nombre)
                cursor.execute(sql,val)
                conexionDB.commit()
                print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO¡ \u2705 :::")
        else:
            print("\t .:: \u26A0 No hay peliculas en el sistema \u26A0 ::.")

    esperarTecla()


    


