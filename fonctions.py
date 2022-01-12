# import re (exo 1)
import fonctions #(exo 2 et suivants)
import csv #(exo 3)
from datetime import date #(exo 3)
import os #(exo 4)


# EXO 2

def calcul_age():
    while True:
        try:
            annee = int(input("Quelle est votre année de naissance ? \n"))
        except:
            print("Veuillez indiquer l'année en chiffres !")
        else:
            if 1920 <= annee < 2020:
                print("OK")
                break
            else:
                print("Veuillez indiquer une année entre 1920 et 2020 !")
    if annee > 2022 - 6:
        print("#####################")
        groupe = "Vous n'etes pas admis"
        print("#####################")
    elif annee > 2022 - 12:
        print("#####################")
        groupe = "Vous etes poussin"
        print("#####################")
    elif annee > 2022 - 18:
        print("#####################")
        groupe = "Vous etes cadet"
        print("#####################")
    elif annee > 2022 - 24:
        print("#####################")
        groupe = "Vous etes junior"
        print("#####################")
    elif annee > 2022 - 30:
        print("#####################")
        groupe = "Vous etes semi-pro"
        print("#####################")
    elif annee >= 2022 - 40:
        print("#####################")
        groupe = "Vous etes pro"
        print("#####################")
    else:
        print("#####################")
        groupe = "Vous n'etes pas admis"
        print("#####################")

    nom = input("Quel est votre nom ? \n")
    prenom = input("Quel est votre prénom ? \n")
    mail = f'{str.capitalize(prenom[0])}.{(nom)}@baton-rouge.fr'

    print(f'Catégorie : {(groupe)} ; Nom : {(nom)} ; Prénom : {(prenom)} ; Mail : {(mail)}')
    print("#####################")

    return groupe, nom, prenom, mail

# EXO 3

def fichier_csv(groupe, nom, prenom, mail):
    with open(f'inscrits-{date.today().year}-{date.today().month}-{date.today().day}.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=':')
        spamwriter.writerow([f'{groupe}, {nom}, {prenom}, {mail}'])




