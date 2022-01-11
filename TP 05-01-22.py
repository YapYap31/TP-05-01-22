#### créer 1 branche github par fonctionnalité ####

####################
#### EXERCICE 1 ####
####################

# import re

nom = input("Quel est votre nom ? \n")
prenom = input("Quel est votre prénom ? \n")
annee = int(input("Quelle est votre année de naissance ? \n"))

# if annee > 2022 - 6:
#     print("#####################")
#     groupe = "Vous n'êtes pas admis"
#     print("#####################")
# elif annee > 2022 - 12:
#     print("#####################")
#     groupe = "Vous êtes catégorie : poussin"
#     print("#####################")
# elif annee > 2022 - 18:
#     print("#####################")
#     groupe = "Vous êtes catégorie : cadet"
#     print("#####################")
# elif annee > 2022 - 24:
#     print("#####################")
#     groupe = "Vous êtes catégorie : junior"
#     print("#####################")
# elif annee > 2022 - 30:
#     print("#####################")
#     groupe = "Vous êtes catégorie : semi-pro"
#     print("#####################")
# elif annee >= 2022 - 40:
#     print("#####################")
#     groupe = "Vous êtes catégorie : pro"
#     print("#####################")
# else:
#     print("#####################")
#     groupe = "Vous n'êtes pas admis"
#     print("#####################")

# print(f"Nom : {(nom)} ; Prénom : {(prenom)} ; Mail : {str.capitalize(prenom[0])}.{(nom)}@baton-rouge.fr")
# print("#####################")

####################
#### EXERCICE 2 ####
####################


import fonctions

# util = int(input("Combien de personnes souhaitez-vous inscrire ? \n"))


# for i in range(util):
#     fonctions.calcul_age()
    

####################
#### EXERCICE 3 ####
####################


# fonctions.calcul_age()

# while True:
#     personnes = input("Avez-vous une autre personne à inscrire ? y/n \n")
#     if personnes == "n":
#         break
#     else:
#         fonctions.calcul_age()

import csv
from datetime import date

with open(f'inscrits-{date.today().year}-{date.today().month}-{date.today().day}.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=':')
    spamwriter.writerow([f'{groupe}, f'{nom}', f'{prenom}', f'{str.capitalize(prenom[0])}.{(nom)}@baton-rouge.fr'])


####################
#### EXERCICE 4 ####
####################


# on peut utiliser la bibliothèque pandas mais ici on va rester sur import csv

fout=open("inscrits_total.csv","a")
# first file:
for line in open("sh1.csv"):
    fout.write(line)
# now the rest:    
for num in range(2,201):
    f = open("sh"+str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()