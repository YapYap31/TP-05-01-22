#### créer 1 branche github par fonctionnalité ####

### EXERCICE 1 ###

import re

nom = input("Quel est votre nom ? \n")
prenom = input("Quel est votre prénom ? \n")
annee = int(input("Quelle est votre année de naissance ? \n"))

if annee > 2022 - 6:
    print("#####################")
    print("Vous n'êtes pas admis")
    print("#####################")
elif annee > 2022 - 12:
    print("#####################")
    print("Vous êtes catégorie : poussin")
    print("#####################")
elif annee > 2022 - 18:
    print("#####################")
    print("Vous êtes catégorie : cadet")
    print("#####################")
elif annee > 2022 - 24:
    print("#####################")
    print("Vous êtes catégorie : junior")
    print("#####################")
elif annee > 2022 - 30:
    print("#####################")
    print("Vous êtes catégorie : semi-pro")
    print("#####################")
elif annee >= 2022 - 40:
    print("#####################")
    print("Vous êtes catégorie : pro")
    print("#####################")
else:
    print("#####################")
    print("Vous n'êtes pas admis")
    print("#####################")

print(f"Nom : {(nom)} ; Prénom : {(prenom)} ; Mail : {str.capitalize(prenom[0])}.{(nom)}@baton-rouge.fr")
print("#####################")

### EXERCICE 2 ###


