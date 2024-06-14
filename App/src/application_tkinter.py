import customtkinter
import poker_GUI

#Personnal Modules
from application import Application

print("Balise : fichier Tkinter")
class GraphicApplication(Application, customtkinter.CTk):
    print("Balise : classe Tkinter")

    def __init__(self):

        self.app_launch()

        #Création des différents boutons
        #Attention à bien spécifier la bonne fonction à utiliser dans le bouton
        
        self.button_launch = customtkinter.CTkButton(self, text="Start",command=self.button_launch)
        self.button_launch.grid(row=0, column=0, padx=20, pady=10)
            
        self.button_options = customtkinter.CTkButton(self, text="Options",command=self.button_options)
        self.button_options.grid(row=1, column=0, padx=20, pady=10)
            
        self.button_close = customtkinter.CTkButton(self, text="Quiiter le jeu", command=self.button_close)
        self.button_close.grid(row=2, column=0, padx=20, pady=10)

    def app_launch(self):
        super().__init__()
        self.geometry("300x200")
        self.title("CTk example")

    def app_menu(self):
        pass
  
    def app_options(self):
        ...
    
    def app_close(self):
        exit()

    #Fonctions pour le bon fonctionnement des boutons
    def button_launch(self):
        print("Balise : Bouton Start Game")
        pokerGUI_instance = poker_GUI.PokerApp()
        pokerGUI_instance.mainloop()
    def button_options(self):
        print("Balise : Bouton Options")
        self.app_options()
    def button_close(self):
        print("Balise : Bouton Close")
        self.app_close()

#Main Guard
if __name__ == "__main__":
    app_instance = GraphicApplication()
    app_instance.mainloop()

