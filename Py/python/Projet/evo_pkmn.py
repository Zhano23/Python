import requests
from bs4 import BeautifulSoup
import re

# Demander à l'utilisateur de saisir le nom du Pokémon
pokemon = input("Entrez le nom d'un Pokémon : ")
url = f"https://www.pokepedia.fr/{pokemon}"
page = requests.get(url)

# Liste des types connus (à adapter si nécessaire)
types_pokemon = ["Normal", "Feu", "Eau", "Plante", "Électrik", "Glace", "Combat", "Poison", 
                 "Sol", "Vol", "Psy", "Insecte", "Roche", "Spectre", "Dragon", "Ténèbres", 
                 "Acier", "Fée"]

if page.status_code == 200:
    with open('annexe_py/pokemon.txt', 'w', encoding='utf-8') as pokemon_text:
        soup = BeautifulSoup(page.text, 'html.parser')
    
        first_p = soup.find('p')
        if first_p:
            # Chercher tous les liens <a> dans ce paragraphe
            links = first_p.find_all("a")

            # Vérifier si un des liens correspond à un type Pokémon connu
            for link in links:
                type_text = link.text.strip()
                if type_text in types_pokemon:
                    print(f"Type détecté : {type_text}")
                    break  # On prend le premier type trouvé
    
        table_class = f"tableaustandard {type_text.lower()}"  # Exemple de classe
        table = soup.find("table", class_=table_class)
        # Vérifier si le tableau existe
        if table:
            cells = table.find_all("td")  # Trouver toutes les balises <td> dans le tableau
            
            visible_texts = [cell.get_text(strip=False) for cell in cells if cell.get_text(strip=False)]
            visible_texts = [re.sub(r'[▲▼]', '', text) for text in visible_texts]


            # Afficher les résultats
            for text in visible_texts:
                pokemon_text.write(text)  # Écriture du code source HTML dans le fichier
        else:
                print(f"{pokemon}n'a pas d'évolution et n'est l'évolution d'aucun Pokémon.")