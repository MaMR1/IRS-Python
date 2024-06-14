# Bibliothèques standard
from collections import Counter

# Modules Personnels
...

def haute_main(valeur):
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    return valeurs.index(valeur)

def is_paire(paquet):
    valeurs = [carte.number for carte in paquet]
    compteur = Counter(valeurs)
    return max(compteur.values()) == 2

def is_deux_paires(ensemble_cartes):
    valeurs = [carte.number for carte in ensemble_cartes]
    compteur = Counter(valeurs)
    return len([v for v in compteur.values() if v == 2]) == 2

def is_brelan(ensemble_cartes):
    valeurs = [carte.number for carte in ensemble_cartes]
    compteur = Counter(valeurs)
    return max(compteur.values()) == 3

def is_suite(ensemble_cartes):
    valeurs = sorted(set([haute_main(carte.number) for carte in ensemble_cartes]))
    for i in range(len(valeurs) - 4):
        if valeurs[i + 4] - valeurs[i] == 4:
            return True
    return False

def is_couleur(ensemble_cartes):
    couleurs = [carte.couleur for carte in ensemble_cartes]
    compteur = Counter(couleurs)
    return max(compteur.values()) >= 5

def is_carre(ensemble_cartes):
    valeurs = [carte.number for carte in ensemble_cartes]
    compteur = Counter(valeurs)
    return max(compteur.values()) == 4

# Fonction qui permet de relever les combinaisons des joueurs en synergie avec la fonction suivante
def evaluer_main(joueur, cartes_table):
    total_cartes = cartes_table + [joueur.card_1, joueur.card_2]
    if is_carre(total_cartes):
        return 7, 'Carré'
    elif is_brelan(total_cartes) and is_paire(total_cartes):
        return 6, 'Full'
    elif is_couleur(total_cartes):
        return 5, 'Couleur'
    elif is_suite(total_cartes):
        return 4, 'Suite'
    elif is_brelan(total_cartes):
        return 3, 'Brelan'
    elif is_deux_paires(total_cartes):
        return 2, 'Deux Paires'
    elif is_paire(total_cartes):
        return 1, 'Paire'
    else:
        return 0, max(total_cartes, key=lambda carte: haute_main(carte.number)).number

def trouver_gagnant(joueurs, cartes_table):
    mains = [(joueur, evaluer_main(joueur, cartes_table)) for joueur in joueurs if joueur.in_game]
    gagnant = max(mains, key=lambda x: x[1])
    return gagnant[0], gagnant[1]

