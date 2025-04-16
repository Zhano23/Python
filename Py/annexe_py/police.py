import requests

# URL du fichier de la police (exemple : Google Fonts ou autre)
url = "https://www.fontspace.com/get/family/gpe4m"  # Remplace par l'URL réelle de la police

# Nom sous lequel on va enregistrer la police
font_path = "ma_police.ttf"

# Télécharger la police
response = requests.get(url)
if response.status_code == 200:
    with open(font_path, "wb") as file:
        file.write(response.content)
    print(f"Police téléchargée et enregistrée sous {font_path}")
else:
    print("Échec du téléchargement")