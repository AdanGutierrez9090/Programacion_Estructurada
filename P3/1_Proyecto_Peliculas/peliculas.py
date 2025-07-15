

import mysql.connector
from mysql.connector import Error
import os

# Diccionario para almacenar los atributos
pelicula = {}

# Limpiar pantalla
def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pausar hasta que se presione una tecla
def esperarTecla():
    input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

# Conexión a la base de datos
def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"❌ Error al conectar a la BD: {e}")
        return None

# Alta de películas
def crearPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t.:: 📝 Alta de Películas 📝 ::.\n ")
        pelicula.update({"nombre": input("🎬 Nombre: ").upper().strip()})
        pelicula.update({"categoria": input("🗂️ Categoría: ").upper().strip()})
        pelicula.update({"clasificacion": input("🔠 Clasificación: ").upper().strip()})
        pelicula.update({"genero": input("🎭 Género: ").upper().strip()})
        pelicula.update({"idioma": input("🗣️ Idioma: ").upper().strip()})

        try:
            cursor = conexionBD.cursor()
            sql = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
            val = (pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])
            cursor.execute(sql, val)
            conexionBD.commit()
            print("\n\t\t ✅ ¡La operación se realizó con éxito! ✅")
        except Error as e:
            print(f"❌ Error al insertar en la BD: {e}")
        finally:
            cursor.close()
            conexionBD.close()
    else:
        print("⚠️ No hay conexión con la base de datos.")
    esperarTecla()

# Mostrar películas
def mostrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t.:: 🔍 Consultar Películas 🔍 ::.\n ")
        try:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM peliculas"
            cursor.execute(sql)
            registros = cursor.fetchall()
            if registros:
                print("\n\t🎥 Lista de Películas")
                print(f"{'ID':<5}{'Nombre':<20}{'Categoría':<15}{'Clasificación':<15}{'Género':<15}{'Idioma':<15}")
                print("-" * 85)
                for fila in registros:
                    print(f"{fila[0]:<5}{fila[1]:<20}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
                print("-" * 85)
            else:
                print("\t ⚠️ No hay películas registradas en el sistema.")
        except Error as e:
            print(f"❌ Error al consultar la BD: {e}")
        finally:
            cursor.close()
            conexionBD.close()
    else:
        print("⚠️ No hay conexión con la base de datos.")
    esperarTecla()

# Buscar películas por nombre
def buscarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t.:: 🔍 Buscar Película por Nombre 🔍 ::.\n ")
        termino = input("🔎 Ingresa el nombre o parte del nombre de la película: ").strip().upper()

        try:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM peliculas WHERE nombre LIKE %s"
            valor = ("%" + termino + "%",)  # búsqueda parcial
            cursor.execute(sql, valor)
            registros = cursor.fetchall()

            if registros:
                print("\n\t🎥 Resultados de Búsqueda")
                print(f"{'ID':<5}{'Nombre':<20}{'Categoría':<15}{'Clasificación':<15}{'Género':<15}{'Idioma':<15}")
                print("-" * 85)
                for fila in registros:
                    print(f"{fila[0]:<5}{fila[1]:<20}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
                print("-" * 85)
            else:
                print(f"\n\t⚠️ No se encontraron películas que coincidan con: {termino}")
        except Error as e:
            print(f"❌ Error al realizar la búsqueda: {e}")
        finally:
            cursor.close()
            conexionBD.close()
    else:
        print("⚠️ No hay conexión con la base de datos.")
    esperarTecla()


# Borrar pelicula
def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: 🗑️ Borrar Película por Nombre 🗑️ ::.\n ")
    nombre = input("🔎 Ingresa el nombre o parte del nombre de la película a borrar: ").strip().upper()

    if nombre == "":
        print("⚠️ No ingresaste un nombre.")
        esperarTecla()
        return

    conexionBD = conectar()
    if conexionBD is not None:
        try:
            cursor = conexionBD.cursor()

            # Verificar si hay coincidencias
            sql_buscar = "SELECT * FROM peliculas WHERE nombre LIKE %s"
            valor = ("%" + nombre + "%",)
            cursor.execute(sql_buscar, valor)
            resultados = cursor.fetchall()

            if resultados:
                print("\n\t🎥 Coincidencias encontradas:")
                print(f"{'ID':<5}{'Nombre':<20}{'Categoría':<15}{'Clasificación':<15}{'Género':<15}{'Idioma':<15}")
                print("-" * 85)
                for fila in resultados:
                    print(f"{fila[0]:<5}{fila[1]:<20}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
                print("-" * 85)

                confirmar = input(f"\n¿Deseas borrar todas las películas que coincidan con \"{nombre}\"? (si/no): ").lower()
                if confirmar in ("si", "sí", "s"):
                    sql_borrar = "DELETE FROM peliculas WHERE nombre LIKE %s"
                    cursor.execute(sql_borrar, valor)
                    conexionBD.commit()
                    print(f"\n✅ Se eliminaron {cursor.rowcount} película(s).")
                else:
                    print("\n🚫 Operación cancelada por el usuario.")
            else:
                print("\n⚠️ No se encontraron coincidencias con ese nombre.")
        except Error as e:
            print(f"❌ Error al intentar borrar: {e}")
        finally:
            cursor.close()
            conexionBD.close()
    else:
        print("⚠️ No se pudo conectar a la base de datos.")
    
    esperarTecla()


def modificarPelicula():
    borrarPantalla()
    print("\n\t.:: ✏️ Modificar Película ✏️ ::.\n")
    nombre = input("🔎 Ingresa el nombre o parte del nombre de la película a modificar: ").strip().upper()

    if not nombre:
        print("⚠️ No ingresaste un nombre.")
        esperarTecla()
        return

    conexionBD = conectar()
    if conexionBD is not None:
        try:
            cursor = conexionBD.cursor()
            sql_buscar = "SELECT * FROM peliculas WHERE nombre LIKE %s"
            valor = ("%" + nombre + "%",)
            cursor.execute(sql_buscar, valor)
            resultados = cursor.fetchall()

            if resultados:
                print("\n\t🎥 Coincidencias encontradas:")
                print(f"{'ID':<5}{'Nombre':<20}{'Categoría':<15}{'Clasificación':<15}{'Género':<15}{'Idioma':<15}")
                print("-" * 85)
                for fila in resultados:
                    print(f"{fila[0]:<5}{fila[1]:<20}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
                print("-" * 85)

                id_modificar = input("\n🆔 Ingresa el ID de la película que deseas modificar: ").strip()

                # Buscar ese ID
                sql_id = "SELECT * FROM peliculas WHERE id = %s"
                cursor.execute(sql_id, (id_modificar,))
                peli = cursor.fetchone()

                if peli:
                    print("\n✏️ Deja en blanco cualquier campo que NO quieras modificar.")
                    nuevo_nombre = input(f"Nuevo nombre [{peli[1]}]: ").strip().upper() or peli[1]
                    nueva_categoria = input(f"Nueva categoría [{peli[2]}]: ").strip().upper() or peli[2]
                    nueva_clasificacion = input(f"Nueva clasificación [{peli[3]}]: ").strip().upper() or peli[3]
                    nuevo_genero = input(f"Nuevo género [{peli[4]}]: ").strip().upper() or peli[4]
                    nuevo_idioma = input(f"Nuevo idioma [{peli[5]}]: ").strip().upper() or peli[5]

                    sql_update = """UPDATE peliculas 
                                    SET nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s 
                                    WHERE id=%s"""
                    datos = (nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, id_modificar)
                    cursor.execute(sql_update, datos)
                    conexionBD.commit()
                    print("\n✅ Película modificada exitosamente.")
                else:
                    print("\n⚠️ No se encontró una película con ese ID.")
            else:
                print("\n⚠️ No se encontraron coincidencias con ese nombre.")
        except Error as e:
            print(f"❌ Error al modificar: {e}")
        finally:
            cursor.close()
            conexionBD.close()
    else:
        print("⚠️ No se pudo conectar a la base de datos.")
    
    esperarTecla()



# Menú principal
def menu():
    while True:
        borrarPantalla()
        print("\n\t🎬 SISTEMA DE GESTIÓN DE PELÍCULAS 🎬")
        print("\n\t1. Alta de Película")
        print("\t2. Mostrar Películas")
        print("\t3. Borrar Todas las Películas")
        print("\t4. Buscar Película")
        print("\t5. Salir")
        opcion = input("\n\tSeleccione una opción: ")

        if opcion == "1":
            crearPeliculas()
        elif opcion == "2":
            mostrarPeliculas()
        elif opcion == "3":
            borrarPeliculas()
        elif opcion == "4":
            buscarPeliculas()
        elif opcion == "5":
            modificarPelicula()
        elif opcion == "6":
            print("\n\t👋 ¡Gracias por usar el sistema! ¡Hasta pronto!")
            break


