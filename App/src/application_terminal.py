

#Personnal Modules
from application import Application

print("Balise : fichier terminal")


class Terminal(Application):
    print("Balise : classe terminal")
    #Attibuts de classe
    project_name = "Projet en Python"
    
    #
    def __init__(self):
        self.terminal_state = "Chargement en cours...."
        self.app_launch()
        #Attributs d'instance
        #
        #

    #
    def app_launch(self):

        print(f"Bienvenue sur le {Terminal.project_name}")

    #
    def app_menu(self):

        print("Menu Principal : Que voulez vous faire ?\n 1) Start Game\n\t 2) Options\n\t 3) Quitter")

    #
    def app_options(self):
        ...
    
    #
    def app_close(self):
        ...
