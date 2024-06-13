# Bibliothèques standard
...

# Modules Personnels
import cartes as X1
import joueurs as X2

NB_MAX = 6


def distribution_cartes(joueurs, paquet):

    for i, joueur in enumerate(joueurs):
        joueur.card_1 = paquet[i]

        # On s'assure qu'il reste des cartes dans le paquet
        # On distribue la seconde carte "après" que tout le monde en ait une
        if i + len(joueurs) < len(paquet):
            joueur.card_2 = paquet[i + len(joueurs)]

def tour(joueurs):
    mise_max = 0
    pot = 0

    for joueur in joueurs:
        if joueur.in_game:
            action = int(input(f"{joueur.name} : (1) se coucher\t (2) suivre\t (3) miser : "))
           
            choix = 1
            while choix:
                match action:
                    case 1 :
                        X2.se_coucher(joueur)
                        choix = 0
                    case 2 :
                        pot += X2.suivre(joueur, mise_max)
                        choix = 0
                    case 3 :
                        mise = X2.miser(joueur, mise_max)
                        mise_max = max(mise_max, mise)
                        pot += mise
                        choix = 0
                    case _:
                        print("Action invalide. Essayez à nouveau.")
    
    return pot

# MAIN FUNCTION
def main():
    print(" BIENVENUE au Poker ! ")

    # Choix du nombre de joueurs
    nombre_de_joueurs = NB_MAX+1
    while((nombre_de_joueurs > NB_MAX) or (nombre_de_joueurs < 0)):

        nombre_de_joueurs = int(input(f"----Choisissez le nombre de joueurs ( MAXIMUM : {NB_MAX})---- "))

    # Choix des prénoms
    print ("\n----Choix des Prénoms----")
    liste_des_joueurs = X2.generer_joueurs(nombre_de_joueurs)

    print ("\n----Création des joueurs----")
    X2.afficher_joueurs(liste_des_joueurs)

    print("\n----Génération du paquet de cartes melange----")
    paquet = X1.generer_paquet()
    paquet = X1.melanger_paquet(paquet)
    X1.afficher_paquet(paquet)

    print("\n----Distribution des cartes----")
    distribution_cartes(liste_des_joueurs, paquet)

    'Commenter cette ligne pour une vraie utilisation'
    X2.afficher_joueurs(liste_des_joueurs)

    
# MAIN GUARD
if __name__ == "__main__":
    main()
