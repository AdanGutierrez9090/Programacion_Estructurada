def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t🔁 ...Oprime cualquier tecla para continuar...")

def menu_principal():
    print(" " * 22 + "📚..:: SISTEMA DE GESTIÓN DE CALIFICACIONES ::..📚")
    print("\n" + " " * 30 + "1️⃣ - Agregar Calificaciones")
    print(" " * 30 + "2️⃣ - Mostrar Calificaciones")
    print(" " * 30 + "3️⃣ - Calcular Promedios")
    print(" " * 30 + "4️⃣ - SALIR 🚪")
    return input("\n" + " " * 28 + "🟩 Elige una opción (1-4): ").strip()


def agregar_calificaciones(lista):
    borrarPantalla()
    print("\n\t📝 Agregar Calificaciones 📝\n")
    nombre = input("\t👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"\t✏️ Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("\t⚠️ Ingresa una calificación entre 0 y 10.")
            except ValueError:
                print("\t❌ Ingresa un valor numérico válido.")
    lista.append([nombre] + calificaciones)
    print("\n\t✅ ¡Calificaciones agregadas con éxito!")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\n\t📋 Mostrar Calificaciones 📋\n")
    if len(lista) > 0:
        print(f"\t{'👤 Nombre':<15} {'📘 Calf. 1':<12} {'📙 Calf. 2':<12} {'📗 Calf. 3':<12}")
        print(f"\t{'-'*55}")
        for fila in lista:
            print(f"\t{fila[0]:<15} {fila[1]:<12.1f} {fila[2]:<12.1f} {fila[3]:<12.1f}")
        print(f"\t{'-'*55}")
        print(f"\n\t🧑‍🎓 Total de alumnos registrados: {len(lista)}")
    else:
        print("\t🚫 No hay calificaciones registradas.")

def calcular_promedios(lista):
    borrarPantalla()
    print("\n\t📈 Calcular Promedios 📈\n")
    if len(lista) > 0:
        print(f"\t{'👤 Nombre':<20} {'📊 Promedio':<10}")
        print(f"\t{'-'*35}")
        suma_general = 0
        for fila in lista:
            promedio = sum(fila[1:]) / 3
            suma_general += promedio
            print(f"\t{fila[0]:<20} {promedio:<10.2f}")
        promedio_grupo = suma_general / len(lista)
        print(f"\t{'-'*35}")
        print(f"\n\t🌟 Promedio general del grupo: {promedio_grupo:.2f} 🌟")
    else:
        print("\t⚠️ No hay calificaciones para calcular promedios.")
