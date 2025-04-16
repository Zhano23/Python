while True:
    nbr=input("Entrez un nombre pour en afficher la table : ")
    try:
        nbr = int(nbr)  # Convertir l'entrée en entier
        for i in range (11):
            result=nbr*i
            print(f"{nbr}x{i}={result}")
    except ValueError: #si l'erreur est une ValueError permet de termminer le code sans crash (exemple: lettre à la place 'un nombre ou l'inverse)
        print("La valeur saisie n'est pas un nombre. Veuillez réessayer ! ")
    