
while True:
    a=input("Entrez le numerateur: ")
    b=input("Entrez le denominateur: ")
    try:
        resultat=float(a)/float(b) #Essaie le code 
        break        
        
    except ValueError: #si l'erreur est une ValueError permet de termminer le code sans crash (exemple: lettre à la place 'un nombre ou l'inverse)
        print("L'une des 2 valeurs saisie n'est pas un nombre. Veuillez réessayer ! ")
        
    except ZeroDivisionError: #si l'erreur est une ZeroDivisionError permet de termminer le code sans crash 
        print("Division par zero impossible. Veuillez réessayer !")


print(f"le resultat est {resultat}")