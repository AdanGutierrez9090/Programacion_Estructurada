import agenda



def main(): 
   
    opcion=True
    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menu_principal()
        match opcion:
                
                case "1":
                    agenda.AgregarContactos()
                    agenda.esperarTecla()
                case "2":
                    agenda.MostrarContactos()
                    agenda.esperarTecla()
                case "3":
                    agenda.BuscarContactos()
                    agenda.esperarTecla()
                        
                case "4":
                    agenda.ModificarContacto()
                    agenda.esperarTecla()

                case "5":
                    agenda.EliminarContacto()
                    agenda.esperarTecla()

                case "6":
                    opcion=False   
                    agenda.borrarPantalla() 
                    print("\n \U0001F6AA \tTerminaste la ejecucion del SW \U0001F6AA")
                case _:
                    
                    print("  \n \u274C \tOpción invalida vuelva a intentarlo \u274C ... por favor")
                    agenda.esperarTecla()

if __name__=="__main__":
    main()
    