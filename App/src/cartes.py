# Bibliothèques standard
import random

# Modules Personnels
...


# La classe pour créer une carte avec les attributs de couleur et de numéro
class Carte:
    def __init__(self, couleur, number):
        self.couleur = couleur
        self.number = number

    def __str__(self):
        return f"{self.number} \\ {self.couleur}"

def generer_paquet():
    couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    paquet = [Carte(i, j) for i in couleurs for j in valeurs]
    return paquet

def melanger_paquet(paquet):
    random.shuffle(paquet)
    return paquet           # Convertir la liste en tuple 
                            # Pour éviter qu'elle ne se mélange à nouveau à la distribution

def afficher_paquet(paquet):
    for i in paquet:
        print(i, end= "\t")

def afficher_carte_precise(paquet, index):
    print(f"{paquet[index]}")


# MAIN FUNCTION
def main():
    # Générer le paquet de 52 cartes
    paquet_initial = generer_paquet()
    paquet_melange = paquet_initial[:]  # Sans [:], temp agirait comme un pointeur plutôt que de recopier
    
       
    # Mélanger le paquet  
    paquet_melange = melanger_paquet(paquet_melange)
    
    # Test : Afficher une carte précise, ici la '1ere' de la liste
    # afficher_carte_precise(paquet_initial,0)

    # Afficher le paquet avant tri
    afficher_paquet(paquet_initial)

    # Afficher le paquet après tri
    afficher_paquet(paquet_melange)




# MAIN GUARD
if __name__ == "__main__":
    main()
    
