'''
proyecto 3
Crear un proyecto que permita gestionar(administrar) calificaciones,colocar un
menu de opciones para agregar,mostrar,calcular promedio de calificaciones de un estudiante

NOTAS
1.- Utilizar fucncionws y mandar a llamar desde otro archivo(modulos)
2.-Utilizar list(bidiomensional) para almacenar el nomnbre del alumno, asi como sus tres calificaciones

'''

import calificaciones

def main():
    datos=[]
    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()
    
        match opcion:
            case "1":
                calificaciones.agregarcalificaciones()
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrarCalificaciones()
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedio()
                calificaciones.esperarTecla()

            case "4":
                calificaciones.buscarAlumno()

            case "5":
                calificaciones.modificarAlumno()

            case "6":
                calificaciones.borrarAlumno()
                    
            case "7":
                opcion=False   
                calificaciones.borrarPantalla() 
                print("\n \U0001F6AA \tTerminaste la ejecucion del SW \U0001F6AA")

            
            case _:
                
                print("  \n \u274C \tOpción invalida vuelva a intentarlo \u274C ... por favor")
                calificaciones.esperarTecla()

if __name__=="__main__":
    main()