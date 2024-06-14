# Bibliothèques standard
...

# Modules Personnels
...

class Joueur:
    def __init__(self, name, money = int(1000), card_1 = None, card_2 = None):
        self.name = name
        self.money = money
        self.card_1 = card_1
        self.card_2 = card_2
        self.mise = 0
        self.in_game = True  # 'True' si le joueur n'est pas couché ni à sec
                        
    def __str__(self):
        return (f"Nom: {self.name}, Solde: {self.money}, Mise du tour: {self.mise}, Carte 1: {self.card_1}, Carte 2: {self.card_2}")
        
# Fonction appelée dans le main pour générer les joueurs en fonction du nombre entré.
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


# Différentes actions que le joueur pour mener
def se_coucher(joueur):
    joueur.in_game = False
    print(f"{joueur.name} se couche...")


def suivre(joueur, mise_max):
    mise = mise_max - joueur.mise
    joueur.mise += mise
    joueur.money -= mise
    print(f"{joueur.name} suit avec : {mise}. Solde restant : {joueur.money}")
    return mise


def miser(joueur, mise_min):
    
    while True: # Lorsque la mise sera acceptée, on break
        # La mise doit obligatoirement être supérieur ou égale à la plus grosse mise
        mise_min = mise_min - joueur.mise +1
        mise = int(input(f"{joueur.name}, entrez votre mise (minimum {mise_min}) : "))
        if mise >= mise_min and mise <= joueur.money:
            joueur.money -= mise
            joueur.mise += mise
            print(f"{joueur.name} relance avec : {mise}. Solde restant : {joueur.money}")
            return mise
        else:
            print(f"Mise invalide. Vous devez miser au moins {mise_min} et au plus {joueur.money}.")



# MAIN FUNCTIONx
def main():
    bla = generer_joueurs(5)
    afficher_joueurs(bla)
    


# MAIN GUARD
if __name__ == "__main__":
    main()
