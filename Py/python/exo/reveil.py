import time
from datetime import time as datetime_time

# Demander à l'utilisateur l'heure et la minute
heure = int(input("Entrez une heure: "))
minute = int(input("Entrez les minutes : "))

# Créer un objet time avec l'heure et les minutes
heure_glo = datetime_time(heure, minute)

# Afficher l'heure formatée
print("Heure formatée :", heure_glo.strftime("%H:%M"))

temps = time.localtime()
heure_locale = time.strftime("%H:%M", temps)
print("Il est :", heure_locale)
