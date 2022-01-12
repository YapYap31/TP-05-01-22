# import re (exo 1)
import fonctions #(exo 2 et suivants)
import csv #(exo 3)
from datetime import date #(exo 3)
import os #(exo 4)


#### créer 1 branche github par fonctionnalité ####

####################
#### EXERCICE 1 ####
####################


# nom = input("Quel est votre nom ? \n")
# prenom = input("Quel est votre prénom ? \n")
# annee = int(input("Quelle est votre année de naissance ? \n"))
# mail = f'{str.capitalize(prenom[0])}.{(nom)}@baton-rouge.fr'

# if annee > 2022 - 6:
#     print("#####################")
#     groupe = "Vous n'etes pas admis"
#     print("#####################")
# elif annee > 2022 - 12:
#     print("#####################")
#     groupe = "Vous etes poussin"
#     print("#####################")
# elif annee > 2022 - 18:
#     print("#####################")
#     groupe = "Vous etes cadet"
#     print("#####################")
# elif annee > 2022 - 24:
#     print("#####################")
#     groupe = "Vous etes junior"
#     print("#####################")
# elif annee > 2022 - 30:
#     print("#####################")
#     groupe = "Vous etes semi-pro"
#     print("#####################")
# elif annee >= 2022 - 40:
#     print("#####################")
#     groupe = "Vous etes pro"
#     print("#####################")
# else:
#     print("#####################")
#     groupe = "Vous n'etes pas admis"
#     print("#####################")

# print(f'Catégorie : {(groupe)} ; Nom : {(nom)} ; Prénom : {(prenom)} ; Mail : {(mail)}')
# print("#####################")

####################
#### EXERCICE 2 ####
####################


util = int(input("Combien de personnes souhaitez-vous inscrire ? \n"))


for i in range(util-1):
    fonctions.calcul_age()
    

####################
#### EXERCICE 3 ####
####################

groupe, nom, prenom, mail = fonctions.calcul_age()
fonctions.fichier_csv(groupe, nom, prenom, mail)

while True:
    personnes = input("Avez-vous une autre personne à inscrire ? y/n \n")
    if personnes == "n":
        break
    else:
        groupe, nom, prenom, mail = fonctions.calcul_age()
        fonctions.fichier_csv(groupe, nom, prenom, mail)


####################
#### EXERCICE 4 ####
####################


# on peut utiliser la bibliothèque pandas mais ici on va rester sur import csv

repertoire = os.listdir()
fout=open('inscrits_total.csv', 'a')
for i in repertoire:
    if '.csv' in i:
        if 'inscrits_total.csv' not in i:
            f = open(i, 'r')
            for line in f:
                fout.write(line)
            f.close()
fout.close()