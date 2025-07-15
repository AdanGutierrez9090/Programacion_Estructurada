import agenda



def main(): 
    agenda_contactos={}
    opcion=True
    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menu_principal()
        match opcion:
                
                case "1":
                    agenda.agregar_contacto(agenda_contactos)
                    agenda.esperarTecla()
                case "2":
                    agenda.mostrar_contacto(agenda_contactos)
                    agenda.esperarTecla()
                case "3":
                    agenda.buscar_contacto(agenda_contactos)
                    agenda.esperarTecla()
                        
                case "4":
                    agenda.modificar_contacto(agenda_contactos)

                case "5":
                    agenda.eliminar_contacto(agenda_contactos)

                case "6":
                    opcion=False   
                    agenda.borrarPantalla() 
                    print("\n \U0001F6AA \tTerminaste la ejecucion del SW \U0001F6AA")
                case _:
                    
                    print("  \n \u274C \tOpción invalida vuelva a intentarlo \u274C ... por favor")
                    agenda.esperarTecla()

if __name__=="__main__":
    main()