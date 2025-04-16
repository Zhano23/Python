import csv

# Liste pour stocker les résultats
salaires = []

# Lire le fichier CSV d'entrée et calculer les salaires
with open('annexe_py/input.csv', encoding='utf-8') as heures_csv:
    reader = csv.DictReader(heures_csv, delimiter=',')
    
    for ligne in reader:
        nom = ligne['nom']
        heures_travaillees = float(ligne['heures_travaillees'])  # Convertir en float
        salaire = heures_travaillees * 15  # Calculer le salaire
        print(f"{nom} a travaillé {heures_travaillees} heure(s) et a gagné {salaire} €")

        # Ajouter aux résultats pour l'écriture
        salaires.append({'nom': nom, 'salaire': salaire})

# Écrire les salaires dans le fichier output.csv
with open('annexe_py/output.csv', 'w', encoding='utf-8') as salaire_csv:
    fieldnames = ['nom', 'salaire']
    writer = csv.DictWriter(salaire_csv, fieldnames=fieldnames)

    writer.writeheader()  # Écrire l'en-tête
    writer.writerows(salaires)  # Écrire toutes les lignes

print("Fichier output.csv créé avec succès !")
