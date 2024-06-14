import poker
import cartes as X1
import joueurs as X2
import customtkinter as ctk

class InputDialog(ctk.CTkToplevel):
    def __init__(self, parent, message, callback):
        super().__init__(parent)
        self.callback = callback
        self.title("Entrer une mise")
        self.geometry("300x150")

        self.label = ctk.CTkLabel(self, text=message)
        self.label.pack(pady=20)

        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10)

        self.button = ctk.CTkButton(self, text="OK", command=self.on_ok)
        self.button.pack(pady=10)

    def on_ok(self):
        value = self.entry.get()
        self.callback(value)
        self.destroy()

class PokerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Poker Game")
        self.geometry("800x600")

        self.label_title = ctk.CTkLabel(self, text="<<<<< BIENVENUE au Poker ! >>>>>")
        self.label_title.pack(pady=20)

        self.frame_controls = ctk.CTkFrame(self)
        self.frame_controls.pack(pady=10)

        self.entry_joueurs = ctk.CTkEntry(self.frame_controls, placeholder_text="Nombre de joueurs")
        self.entry_joueurs.pack(side="left", padx=10)

        self.button_start = ctk.CTkButton(self.frame_controls, text="Démarrer", command=self.start_game)
        self.button_start.pack(side="left", padx=10)

        self.frame_game = ctk.CTkFrame(self)
        self.frame_game.pack(pady=20)

        self.joueurs = []
        self.paquet = []
        self.cartes_au_centre = []
        self.pot = 0

    def start_game(self):
        nombre_de_joueurs = int(self.entry_joueurs.get())
        self.joueurs = self.generer_joueurs(nombre_de_joueurs)

        self.paquet = X1.generer_paquet()
        self.paquet = X1.melanger_paquet(self.paquet)

        self.distribution_cartes()
        self.afficher_joueurs()

        self.tour()

    def generer_joueurs(self, nombre):
        joueurs = []
        for i in range(nombre):
            name = f"Joueur {i+1}"
            joueurs.append(X2.Joueur(name))
        return joueurs

    def distribution_cartes(self):
        poker.distribution_cartes(self.joueurs, self.paquet, self.cartes_au_centre)

    def afficher_joueurs(self):
        for widget in self.frame_game.winfo_children():
            widget.destroy()
        
        for joueur in self.joueurs:
            label_joueur = ctk.CTkLabel(self.frame_game, text=str(joueur))
            label_joueur.pack(pady=5)

    def tour(self):
        for i, joueur in enumerate(self.joueurs):
            if joueur.in_game:
                frame_joueur = ctk.CTkFrame(self.frame_game)
                frame_joueur.pack(pady=10)

                label_joueur = ctk.CTkLabel(frame_joueur, text=str(joueur))
                label_joueur.pack(side="left", padx=10)

                button_se_coucher = ctk.CTkButton(
                    frame_joueur, text="Se coucher", command=lambda j=joueur: self.se_coucher(j))
                button_se_coucher.pack(side="left", padx=5)

                button_suivre = ctk.CTkButton(
                    frame_joueur, text="Suivre", command=lambda j=joueur: self.suivre(j))
                button_suivre.pack(side="left", padx=5)

                button_miser = ctk.CTkButton(
                    frame_joueur, text="Miser", command=lambda j=joueur: self.open_miser_dialog(j))
                button_miser.pack(side="left", padx=5)

    def se_coucher(self, joueur):
        poker.se_coucher(joueur)
        self.afficher_joueurs()

    def suivre(self, joueur):
        mise_max = max(j.mise for j in self.joueurs)
        self.pot += poker.suivre(joueur, mise_max)
        self.afficher_joueurs()

    def open_miser_dialog(self, joueur):
        def on_submit(value):
            mise_min = max(j.mise for j in self.joueurs)
            mise = int(value)
            if mise >= mise_min and mise <= joueur.money:
                joueur.money -= mise
                joueur.mise += mise
                self.pot += mise
                self.afficher_joueurs()
            else:
                print(f"Mise invalide. Vous devez miser au moins {mise_min} et au plus {joueur.money}.")
                self.open_miser_dialog(joueur)  # reopen the dialog if the input was invalid

        dialog = InputDialog(self, f"{joueur.name}, entrez votre mise (minimum {max(j.mise for j in self.joueurs)}) :", on_submit)

if __name__ == "__main__":
    app = PokerApp()
    app.mainloop()
