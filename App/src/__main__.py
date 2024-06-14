#Standard Python Library
import os
from application_terminal import Terminal
from application_panda3D import Panda
from application_tkinter import GraphicApplication

#Personnal Modules
...

#from application import App

#Main function
def main():
    os.system('cls')
    

    """
    app_instance = App()
    app_instance.quit_app()
    """
    #Choix du mode d'utilisation

    loop = 1
    while loop:
        app_mode = input("Bonjour, veuillez selectionner un mode :"
                     +"1) Terminal  2) Panda3D  3) Tkinter\n")
        app_mode = int(app_mode)
        match app_mode:
            #Terminal
            case 1:
                loop = 0
                print("Vous avez choisi le mode Terminal")
                terminal_instance = Terminal()
                pass

            #Panda3D
            case 2:
                loop = 0
                print("Vous avez choisi le mode Panda3D")
                terminal_instance = Panda()
                pass

            #CustomTkinter
            case 3:
                loop = 0
                print("Vous avez choisi le mode Tkinter")
                GUI_instance = GraphicApplication()
                GUI_instance.mainloop()

                pass

            #Default == non reconnu
            case _:
                print("This command is unavailable !i!i!i")


#Main guard
if __name__ == "__main__":
    main()
