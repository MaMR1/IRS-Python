
# Personnal Modules
from application import Application
import poker

print("Balise : fichier terminal")
class Terminal(Application):
    print("Balise : classe terminal")
    # Attibuts de classe
    project_name = "Projet en Python"
    
    #
    def __init__(self):
        choix = None
        self.terminal_state = "Chargement en cours...."
        self.app_menu()
              
        # Attributs d'instance
        #
        
    #
    def app_launch(self):
        print("Balise : app_launch")
        print(f"Bienvenue sur le {Terminal.project_name}")
        poker.main()
    #
    def app_menu(self):
        print("Balise : app_menu")
        match int(input("Menu Principal : Que voulez vous faire ?\n 1) Start Game\n\t 2) Options\n\t\t 3) Quitter\n")):
            case 1:
                self.app_launch()
            case 2:
                self.app_options()
            case 3:
                self.app_close()
    #
    def app_options(self):
        print("Balise : app_options")
        #
    def app_close(self):
        exit()
        
