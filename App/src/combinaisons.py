# Bibliothèques standard
from collections import Counter

# Modules Personnels
import cartes as X1
import joueurs as X2

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


def verifier_combinaisons(joueur, cartes_sur_table):
    all_cartes = cartes_sur_table + [joueur.card_1, joueur.card_2]
    # Classement des combinaisons par ordre de priorité
    combinaisons = [
        ('carre', is_carre(all_cartes), 6),
        ('couleur', is_couleur(all_cartes), 5),
        ('suite', is_suite(all_cartes), 4),
        ('brelan', is_brelan(all_cartes), 3),
        ('deux_paires', is_deux_paires(all_cartes), 2),
        ('paire', is_paire(all_cartes), 1),
        ('haute_carte', True, 0)                # Par défaut, on aura 'haute carte'
    ]

    for meilleure_combi, presente, valeur in combinaisons:
        if presente:
            return meilleure_combi, valeur

def determiner_gagnant(joueurs, cartes_sur_table):
    meilleurs_joueurs = []
    meilleure_valeur = 0

    for joueur in joueurs:
        combinaison, valeur_combinaison = verifier_combinaisons(joueur, cartes_sur_table)
        
        if valeur_combinaison > meilleure_valeur:
            meilleurs_joueurs = [joueur]
            meilleure_combinaison = combinaison
            meilleure_valeur = valeur_combinaison
        elif valeur_combinaison == meilleure_valeur:
            meilleurs_joueurs.append(joueur)

    return meilleurs_joueurs, meilleure_combinaison
