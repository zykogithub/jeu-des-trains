from random import randint
from time import time

from module_toutes_les_gares import gare_dico

""" algorithme du jeu
    1 tant que l'utilisateur n'a pas dit stop ou a mis le nombre maximum d'entrée,
    ajouter une valeur dans la liste de répons
    2 parcourir la liste rattachée à la gare et comparer chaque élément de la liste
    réponse à celle de la gare
    3 S'il y a une correspondance, retiré l'élément de la liste réponse
    4 ensuite, voici les résultats que le jeu peut donner :
        1 Si la liste réponse est vide : bonne réponse
        2 Si la liste réponse n'a pas changé de taille : mauvaise réponse
        3 Si la liste a changé de taille mais n'est pas vide : afficher les éléments
        de la liste de la gare pour dire qu'ils sont en bonne réponse
        Puis afficher les éléments restant pour dire qu'ils sont en mauvaise réponse
"""


def jeu_des_gares_():
    # Générer un entier aléatoirement pour cibler une gare
    # Chaque dico de la liste a pour seule clef le nom de la gare.
    gare_selectionne = randint(0, len(gare_dico) - 1)

    cle_jeu = None
    valeur_reponse = []
    for cle, valeur in gare_dico[gare_selectionne].items():
        cle_jeu = cle
        valeur_reponse = valeur

    # debut du jeu :
    print(
        "Bonjour, Bienvenue dans le jeu : devine la gare ! \n"
        "Le jeu est simple : Nous allons donnez un nom de gare, "
        "il faudra donner la(es) ligne(s) qui la traverse(nt) \n"
    )
    print(
        "Bien évidement, vous avez seulement 5 minutes pour toutes les données, "
        "alors dépéchez-vous ! Bonne chance !"
    )
    print(f"Quelle(s) est (sont) les lignes traversée(s) à la gare de : {cle_jeu} ?")
    print("Ecrivez sous la forme : RER A ou RER B, etc")

    # debut de l'algorithme du jeu
    tour = 0
    MAXIMUM = 10
    DUREE_MAX = 300  # 5 minutes = 300 secondes
    debut = time()
    temps_ecoule = 0
    liste_reponse = []
    reponse = None

    print(f"Vous ne pourrez pas rentrer au dela de {MAXIMUM} réponses")

    while reponse != "STOP" and tour < MAXIMUM and temps_ecoule <= DUREE_MAX:
        temps_ecoule = time() - debut
        reponse = input(
            "Ecrivez une nouvelle réponse. \n"
            "Tapez STOP pour arrêter de répondre \n"
        )
        reponse = reponse.upper()

        if reponse != "STOP":
            liste_reponse.append(reponse)
            tour += 1
            print(f"Il vous reste {MAXIMUM - tour} essais.")

    # Nettoyage de la liste si le dernier élément est STOP
    if liste_reponse and liste_reponse[-1] == "STOP":
        del liste_reponse[-1]

    taille_reponse = len(liste_reponse)

    # Comparaison des réponses
    for i in range(len(liste_reponse) - 1, -1, -1):
        essaie = liste_reponse[i]
        if essaie in valeur_reponse:
            del liste_reponse[i]

    # Affichage des résultats
    if temps_ecoule >= DUREE_MAX:
        print("Dommage, vous avez dépassé le temps imparti.")

    if len(liste_reponse) == 0 and tour > 0:
        print("Bravo, vous avez donné toutes les bonnes réponses !")
    elif len(liste_reponse) == taille_reponse:
        print("Dommage, aucune bonne réponse... Voici ce qu'il fallait :")
        for ligne in valeur_reponse:
            print(ligne)
    else:
        print("Certaines réponses sont correctes ! Voici celles qui manquaient :")
        for ligne in valeur_reponse:
            print(ligne)


""" nota bene :
    - testez si la réponse rentrée est incorrect
    - prévoir une boucle si l'utilisateur ne rentre rien
    - limiter le nombre de réponses inutiles
"""
