import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except:
        print(f"⚠️ Error al conectar a la base de datos")
        return None


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n \U0001F552 \t ...Oprima cualquier tecla para continuar \U0001F552...")  

def menu_principal():
  print("\t\t  📆..::: Sistema de Gestión de Gestión de Agenda de contactos :::... 📆\n\t\t\t 1️⃣  Agregar contacto  \n\t\t\t 2️⃣  Mostrar todos los contactos\n\t\t\t 3️⃣  Buscar contacto por nombre \n\t\t\t  4️⃣ Modificar Contactos   \n\t\t\t  5️⃣ Elimminar Contactos\n\t\t\t\U0001F6AASALIR ")
  opcion=input("\t\t\t 👉 Elige una opción (1-6): ").upper()
  return opcion

def AgregarContactos():
    borrarPantalla()
    print("➕ Agregar Contacto")
    nombre = input("Nombre: ").strip().capitalize()
    telefono = input("📞 Teléfono: ").strip()
    correo = input("✉️ Correo: ").strip()

    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO contactos (nombre, telefono, correo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, telefono, correo))
        conexion.commit()
        print("✅ Contacto agregado exitosamente.")
    except :
        print(f" Oucrrio algo inesperado")
    finally:
        cursor.close()
        conexion.close()

def MostrarContactos():
    borrarPantalla()
    print("📋 Lista de Contactos")

    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM contactos")
        resultados = cursor.fetchall()
        if resultados:
            print(f"{'ID':<5}{'Nombre':<20}{'Teléfono':<15}{'Correo':<30}")
            print("-"*70)
            for fila in resultados:
                print(f"{fila[0]:<5}{fila[1]:<20}{fila[2]:<15}{fila[3]:<30}")
        else:
            print("❌ No hay contactos registrados.")
    except :
        print(f" Sucedio algo inesperado")
    finally:
        cursor.close()
        conexion.close()

def BuscarContactos():
    borrarPantalla()
    print("🔍 Buscar Contacto")
    nombre = input("Nombre a buscar: ").strip().capitalize()

    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        resultados = cursor.fetchall()
        if resultados:
            for fila in resultados:
                print(f"👤 {fila[1]} - 📞 {fila[2]} - ✉️ {fila[3]}")
        else:
            print("❌ No se encontró el contacto.")
    except:
        print(f" Sucedio algo inesperado")
    finally:
        cursor.close()
        conexion.close()

def ModificarContacto():
    borrarPantalla()
    print("✏️ Modificar Contacto")
    nombre = input("Nombre del contacto a modificar: ").strip().capitalize()

    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        contacto = cursor.fetchone()
        if contacto:
            print(f"\n📌 Actual: {contacto[1]} - {contacto[2]} - {contacto[3]}")
            nuevo_tel = input("Nuevo teléfono (deja vacío para no cambiar): ").strip() or contacto[2]
            nuevo_correo = input("Nuevo correo (deja vacío para no cambiar): ").strip() or contacto[3]
            sql_update = "UPDATE contactos SET telefono = %s, correo = %s WHERE id = %s"
            cursor.execute(sql_update, (nuevo_tel, nuevo_correo, contacto[0]))
            conexion.commit()
            print("✅ Contacto modificado.")
        else:
            print("❌ Contacto no encontrado.")
    except :
        print(f"Sucedio algo inesperado")
    finally:
        cursor.close()
        conexion.close()

def EliminarContacto():
    borrarPantalla()
    print("🗑️ Eliminar Contacto")
    nombre = input("Nombre del contacto a eliminar: ").strip().capitalize()

    conexion = conectar()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
        contacto = cursor.fetchone()
        if contacto:
            print(f"\n📌 {contacto[1]} - {contacto[2]} - {contacto[3]}")
            confirmacion = input("¿Deseas eliminar este contacto? (si/no): ").strip().lower()
            if confirmacion == "si":
                cursor.execute("DELETE FROM contactos WHERE id = %s", (contacto[0],))
                conexion.commit()
                print("✅ Contacto eliminado.")
        else:
            print("❌ Contacto no encontrado.")
    except :
        print(f"Sucedio algo inesperado")
    finally:
        cursor.close()
        conexion.close()
