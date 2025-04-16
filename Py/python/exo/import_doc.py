fichier = open("annexe_py/hello.txt","r+") #Ouverture du fichier voulu: r pour la lecture, w pour l'écriture et r+ c'est les 2
fichier.write("meliodas samaaaaa\n")#Ecriture du texte dans le fichier
fichier.write("Coca bien frais chacal\n")
fichier.write("Oh comment je suis bieeeeeng\n")
fichier.seek(0) #Permet de placer le curseur au debut du fichier
for ligne in fichier:
    # faire quelque chose avec une ligne
    print(ligne, end="") #Affiche la ligne a partir de l'emplacement du curseur grace a la boucle lis tout le fichier
fichier.close() #Ferme le fichier

import csv

with open('annexe_py/couleurs_preferees.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])


