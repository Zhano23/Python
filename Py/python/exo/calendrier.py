import datetime
import locale  # Import du module locale

# Définir la langue en français (Windows : "fra", Linux/Mac : "fr_FR.UTF-8")
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")  # Sur Linux/Mac
locale.setlocale(locale.LC_TIME, "fra")  # Sur Windows (essaie si le premier ne marche pas)

yy = 2025
mm = 4
dd = 5

result = datetime.date(yy, mm, dd)

# Affichage avec le nom du mois en français
print(result.strftime("%d %B %Y")) #
