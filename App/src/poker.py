# Bibliothèques standard
import os

# Modules Personnels
import cartes as X1
import joueurs as X2
import combinaisons as X3

NB_MAX = 6

def distribution_cartes(joueurs, paquet, cartes_table):
    nb_distribue = 0
    for i, joueur in enumerate(joueurs):
        joueur.card_1 = paquet[i]

        # On s'assure qu'il reste des cartes dans le paquet
        # On distribue la seconde carte "après" que tout le monde en ait une
                                        # (En utilisant un saut de taille égal au nb de joueurs)
        if i + len(joueurs) < len(paquet):
            joueur.card_2 = paquet[i + len(joueurs)]

        nb_distribue += 2       # Nécessaire pour connaitre le nb distribué

    for j in range(0,5):        # Enregistre dans une liste les 5 cartes au centre de la table
        cartes_table.append(paquet[nb_distribue+j])
        print(f"Carte {j} : {cartes_table[j]}")
    

def lancer_partie():
    while 1:
        a = input("Prêts à lancer la partie ? ( Oui ) : ").lower()
        if a == "oui":
            return os.system('cls')
        

def tour(joueurs):
    mise_max = 0
    pot = 0

    fin_de_tour = 0
    while not fin_de_tour:  # On sort lorsque tous les joueurs sont à jour dans leur mises
    
        for joueur in joueurs:              # En premier temps chaque joueur agit

            if joueur.in_game:
                           
                while True:                 # Permet de recommencer si le choix est invalide
                    action = int(input(f"\n----{joueur}---- \n (1) se coucher\n (2) suivre\n (3) miser : "))
                    match action:
                        case 1 :
                            X2.se_coucher(joueur)
                            break

                        case 2 :
                            pot += X2.suivre(joueur, mise_max)
                            if fin_de_tour <= 0:
                                fin_de_tour += 1
                            break

                        case 3 :
                            
                            mise = X2.miser(joueur, mise_max)
                            mise_max = max(mise_max, joueur.mise)
                            pot += mise
                            fin_de_tour = 0
                            break

                        case _:
                            print("Action invalide. Essayez à nouveau.")
                # Fin while
        # Fin for
    
    """
    # Aide : Nécessaire pour débloquer 
    # Ceci étant, cela posera probleme lors des "All-in" avec des montants différents
    for joueur in joueurs:  
        joueur.mise = 0
    """

    return pot

def gagnant(joueurs, cartes_table):
    print(f"\n-------Rappel : les cartes du centre-------\n")
    meilleur_joueur = None
    meilleure_valeur = 0

    for joueur in joueurs:
        valeur_combinaison = X3.verifier_combinaisons(joueur, cartes_table)

        if valeur_combinaison > meilleure_valeur:
                meilleur_joueur = joueur
                meilleure_valeur = valeur_combinaison

    return meilleur_joueur


# MAIN FUNCTION
def main():
    cartes_au_centre = []

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
    distribution_cartes(liste_des_joueurs, paquet, cartes_au_centre)

    'Commenter cette ligne pour lors d_une vraie utilisation'
    X2.afficher_joueurs(liste_des_joueurs)

    # Partie
    while(True):
        lancer_partie()
        pot = int(0)
        for round in range(0,4):
            print(f"\n-------Tour N°{round+1}-------")

            match round:
                case 0:
                    pot = tour(liste_des_joueurs)
                case 1:
                    print(f" {cartes_au_centre[0]}   {cartes_au_centre[1]}   {cartes_au_centre[2]}")
                    pot = tour(liste_des_joueurs)
                case 2:
                    print(f" {cartes_au_centre[0]}   {cartes_au_centre[1]}   {cartes_au_centre[2]}   {cartes_au_centre[3]}")
                    pot = tour(liste_des_joueurs)
                case 3:
                    print(f" {cartes_au_centre[0]}   {cartes_au_centre[1]}   {cartes_au_centre[2]}   {cartes_au_centre[3]}   {cartes_au_centre[3]}")
                    pot = tour(liste_des_joueurs)

            # Remise à zéro des mises pour les prochains tours
            for joueur in liste_des_joueurs:
                joueur.mise = 0

        # Trouver le gagnant, à qui on incrémente l'argent
        gagnant_manche = X3.determiner_gagnant(liste_des_joueurs,cartes_au_centre)
        print(f"{gagnant_manche}")
        gagnant_manche.money += pot

    
# MAIN GUARD
if __name__ == "__main__":
    main()
