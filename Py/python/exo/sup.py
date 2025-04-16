while True:
    a,b,c=input("Entrez les nombres : ")
    # b=input("Entrez un 2eme nombre : ")
    # c=input("Entrez un 3eme nombre : ")
    try:
        a = int(a)  # Convertir l'entrée en entier
        b = int(b)
        c = int(c)
        if a>b and a>c:
            print(f"le plus grand nombre est {a}")
        elif b>a and b>c:
            print(f"Le plus grand nombre est {b}")
        else:
            print(f"Le plus grand nombre est {c}")
    except ValueError: #si l'erreur est une ValueError permet de termminer le code sans crash (exemple: lettre à la place 'un nombre ou l'inverse)
        print("La valeur saisie n'est pas un nombre. Veuillez réessayer ! ")
