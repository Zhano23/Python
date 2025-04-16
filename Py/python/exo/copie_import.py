import requests

url = "https://quotes.toscrape.com/"
page = requests.get(url)

# Vérifier si la requête a réussi
if page.status_code == 200:
    with open('annexe_py/copie_site.html', 'w', encoding='utf-8') as copie_html:
        copie_html.write(page.text)  # Écriture du code source HTML dans le fichier
    print("Le fichier HTML a été sauvegardé avec succès !")
else:
    print(f"Échec de la requête, code d'erreur : {page.status_code}")
