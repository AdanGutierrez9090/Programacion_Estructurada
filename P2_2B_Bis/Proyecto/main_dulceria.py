
import dulceria

def main():
    datos = []
    opcion = True

    while opcion:
        dulceria.borrarPantalla()
        opcion = dulceria.menu_principal()

        match opcion:
            case "1":
                dulceria.borrarPantalla()
                dulceria.agregar_producto(datos)
                dulceria.esperarTecla()

            case "2":
                dulceria.borrarPantalla()
                dulceria.ver_inventario(datos)
                dulceria.esperarTecla()

            case "3":
                dulceria.borrarPantalla()
                dulceria.entrada_producto(datos)
                dulceria.esperarTecla()

            case "4":
                dulceria.borrarPantalla()
                dulceria.salida_producto(datos)
                dulceria.esperarTecla()

            case "5":
                dulceria.borrarPantalla()
                dulceria.buscar_codigo(datos)
                dulceria.esperarTecla()

            case "6":
                dulceria.borrarPantalla()
                print("\n🚪 Saliendo del sistema. ¡Hasta luego!")
                opcion = False

            case _:
                dulceria.borrarPantalla()
                print("⚠️ Opción inválida. Intente nuevamente.")
                dulceria.esperarTecla()

if __name__ == "__main__":
    main()
