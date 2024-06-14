# Python-IRS

## __main__.py

#### Fichier principal qui joint la globalité des fichier.
#### Le mode Terminal est finalisé.
#### Le mode Panda3D n'est pas disponible (seul la démo du panda est fonctionnelle.
#### Le mode Tkinter est presque abouti.


## Cartes.py

#### Ce fichier s'occupe des fonctions propres aux cartes : qui ne nécessitent pas de modules personnels.
#### La fonction pour distribuer les cartes sera donc dans le main() puisque cela nécessite l'utilisation des Joueurs. 
#### Cependant, on trouve dans ce fichier la fonction qui génère les Carte, la classe Carte, et la fonction pour afficher, au besoin, le résultat de cette génération.

## Joueurs.py

#### Ce fichier s'occupe des fonctions propres aux cartes : qui ne nécessitent pas de modules personnels.

## Combinaisons.py

#### Ce fichier s'occupe des différentes combinaisons reconnues dans le jeu.
#### Il définit aussi les fonctions permettant de relever le joueur avec la meilleure main.

## Poker.py

#### Dépend de *cartes.py*, *joueurs.py* et *combinaisons.py*.
#### Ce fichier regroupe toutes les fonctions propres aux règles du jeu : au déroulé d'une partie.

## Poker_GUI.py

#### Version Tkinter de *poker.py*

## Modifications à apporter

### Fonctionnement même du jeu :
####Il n'est pas possible de finir une partie, la gestion des "All-in" avec la proportionnalité des gains n'est pas implémentée

### Mode Panda3D
#### Doit être implémenté.

### Mode Tkinter
#### Version alpha+ en place, finalisation nécessaire.

#####*By Martin, Have fun*
*
