#Addition des minutes et secondes en heures et jours
choix_minutes = str(input("Voulez-vous convertir des minutes en heures ?")).lower()
while choix_minutes != "oui" and choix_minutes !="non":
    choix_minutes = input("Réessayer: Voulez-vous convertir des minutes en heures ? ")
if choix_minutes == "oui":
    nbr_minutes = str(input("Veuillez entrez un nombre de minutes à convertir ? "))
    while nbr_minutes.isnumeric() == False:
        nbr_minutes =input("Réessayer: Veuillez entrez un nombre de minutes à convertir :")
    nbr_minutes= int(nbr_minutes)
    minutes_a_heures = nbr_minutes//60
    minutes_restantes = nbr_minutes % 60
    print(f"ça fait {minutes_a_heures}h et {minutes_restantes} minutes")

nbr_heures = str (input("Veuillez entrez des heures à convertir: "))
while nbr_heures.isnumeric() == False:
    nbr_heure =input("Réessayer: Veuillez entrez des heures à convertir: ")
nbr_heures= int(nbr_heures)
heures_a_jours = nbr_heures//24
heures_restantes = nbr_heures % 24
if choix_minutes == "oui":
    print(f"ça fait {heures_a_jours} jours {heures_restantes+minutes_a_heures} heures et {minutes_restantes} minutes")
else : 
    print(f"ça fait {heures_a_jours}jours et {heures_restantes} heures")

