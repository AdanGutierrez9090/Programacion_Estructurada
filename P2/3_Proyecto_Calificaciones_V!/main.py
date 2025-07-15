'''proyecto 3
Crear un proyecto que permita gestionar(administrar) calificaciones,colocar un
menu de opciones para agregar,mostrar,calcular promedio de calificaciones de un estudiante

NOTAS
1.-Utilizar fucncionws y mandar a llamar desde otro archivo(modulos)
2.-Utilizar list(bidiomensional) para almacenar el nomnbre del alumno, asi como sus tres calificaciones

'''

import calificaciones

def main():
    datos = []
    opcion = True
    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                opcion = False
                calificaciones.borrarPantalla()
                print("\n\t👋 ¡Gracias por usar el sistema! Hasta pronto.")
            case _:
                print("\n\t❌ Opción inválida, vuelve a intentarlo...")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()
