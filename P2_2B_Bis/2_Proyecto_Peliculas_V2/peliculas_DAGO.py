

#Dict u objeto  para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma)

# Sistema de gestión de una sola película
pelicula = {}

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t🕹️ Oprima cualquier tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("🎬 .:: Alta de Película ::.\n")
    pelicula.update({"nombre": input("🎞️ Ingrese el nombre: ").upper().strip()})
    pelicula.update({"categoria": input("🗂️ Ingrese la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("🔖 Ingrese la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("🎭 Ingrese el género: ").upper().strip()})
    pelicula.update({"idioma": input("🌐 Ingrese el idioma: ").upper().strip()})
    print("\n✅ ¡La operación se realizó con éxito!")
    esperarTecla()

def mostrarPeliculas():
    borrarPantalla()
    print("\n📋 .:: Consultar Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t🎬 {i.capitalize()} : {pelicula[i]}")
    else:
        print("\n⚠️ No hay película registrada.")
    esperarTecla()

def borrarPeliculas():
    borrarPantalla()
    print("\n🗑️ .:: Borrar Película ::.\n")
    resp = input("❓ ¿Deseas borrar la película? (si/no): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        print("\n✅ ¡Película eliminada con éxito!")
    else:
        print("\nℹ️ Operación cancelada.")
    esperarTecla()

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n➕ .:: Agregar Característica ::.\n")
    atributo = input("🔤 Ingresa el nombre del nuevo atributo: ").lower().strip()
    valor = input("📝 Ingresa el valor del atributo: ").upper().strip()
    pelicula[atributo] = valor
    print("\n✅ ¡La característica fue agregada!")
    esperarTecla()

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n🔧 .:: Modificar Característica ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t📌 {i} : {pelicula[i]}")
        atributo = input("\n✏️ Ingresa el atributo que deseas modificar: ").lower().strip()
        if atributo in pelicula:
            nuevo_valor = input("🔁 Ingresa el nuevo valor: ").upper().strip()
            pelicula[atributo] = nuevo_valor
            print("\n✅ ¡Modificación exitosa!")
        else:
            print("❌ El atributo no existe.")
    else:
        print("⚠️ No hay película registrada.")
    esperarTecla()

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n🗑️ .:: Borrar Característica ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t📌 {i} : {pelicula[i]}")
        atributo = input("\n❓ Ingresa la característica a eliminar: ").lower().strip()
        if atributo in pelicula:
            del pelicula[atributo]
            print("\n✅ ¡Característica eliminada!")
        else:
            print("❌ Característica no encontrada.")
    else:
        print("⚠️ No hay película registrada.")
    esperarTecla()

def menu():
    borrarPantalla()
    print("\n🎬 .:: SISTEMA DE GESTIÓN DE PELÍCULA ::. 🎬\n")
    print("1️⃣  Agregar nueva película")
    print("2️⃣  Mostrar película")
    print("3️⃣  Borrar película")
    print("4️⃣  Agregar característica")
    print("5️⃣  Modificar característica")
    print("6️⃣  Borrar característica")
    print("7️⃣  Salir 🚪")

# Bucle principal
while True:
    menu()
    opcion = input("\n📌 Selecciona una opción (1-7): ").strip()

    if opcion == "1":
        crearPeliculas()
    elif opcion == "2":
        mostrarPeliculas()
    elif opcion == "3":
        borrarPeliculas()
    elif opcion == "4":
        agregarCaracteristicaPeliculas()
    elif opcion == "5":
        modificarCaracteristicaPeliculas()
    elif opcion == "6":
        borrarCaracteristicaPeliculas()
    elif opcion == "7":
        print("\n👋 ¡Gracias por usar el sistema de películas!")
        break
    else:
        print("⚠️ Opción no válida.")
        esperarTecla()
