import datetime
import locale  # Import du module locale

# Définir la langue en français (Windows : "fra", Linux/Mac : "fr_FR.UTF-8")
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")  # Sur Linux/Mac
locale.setlocale(locale.LC_TIME, "fra")  # Sur Windows (essaie si le premier ne marche pas)

jour1, mois1, annee1 = map(int, input("Entrez votre date de naissance au format jj mm aaaa : ").split())

start=datetime.date(annee1, mois1, jour1)
end =datetime.date.today() # end recupere la date local d'aujourd'hui
if start > end :
    futur_days=(start-end).days # Le .days permet d'afficher seulment les jours et non l'heure
    futur_weeks, days_left = divmod(futur_days,7) # divmod permet d'affecter le quotient a la 1ere variable et le reste à 2eme variable
    print(f"Il reste {futur_days} jours avant cette date donc {futur_weeks} semaines et {days_left} jours")

else:
    past_days = (end - start).days # Le .days permet d'afficher seulment les jours et non l'heure
    past_weeks, days_left = divmod(past_days,7) # divmod permet d'affecter le quotient a la 1ere variable et le reste à 2eme variable
    past_years = past_days//365
    print (f"{past_days} jours se sont écoulé jusqu'à aujourd'hui donc {past_weeks} semaines et {days_left} jours et tu as donc {past_years} ans") 
