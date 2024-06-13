# Bibliothèques standard
...

# Modules Personnels
...

class Joueur:
    def __init__(self, name, money = int(100), card_1 = None, card_2 = None):
        self.name = name
        self.money = money
        self.card_1 = card_1
        self.card_2 = card_2

    def __str__(self):
        return (f"Nom: {self.name}, Solde: {self.money}, Carte 1: {self.card_1}, Carte 2: {self.card_2}")
    
#Fonction appelée dans le main pour générer les joueurs en fonction du nombre entré.
def generer_joueurs(nombre):
    joueurs = []    # Type : List
    for i in range(nombre):
        name = input(f"Entrez le nom du joueur {i+1} : ")
        # Ajouter l'instance de Joueur à la liste
        joueurs.append(Joueur(name))  
    return joueurs

def afficher_joueurs(joueurs):
    for i in joueurs:
        print(i)


# MAIN FUNCTIONx
def main():
    bla = generer_joueurs(5)
    afficher_joueurs(bla)


# MAIN GUARD
if __name__ == "__main__":
    main()
