def accueil():
    while True:
        try:
            user_choice = int(input("Votre choix : "))
            if 1 <= user_choice <= 5:
                return(user_choice)  # Sort de la boucle si le choix est valide
            else:
                print("Erreur : Le nombre doit être entre 1 et 5.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

liste=["pomme"]

while True:
    print("\nChoisissez parmi les 5 options suivantes:")
    print("1-Ajouter un élément à la liste")
    print("2-Retirer un élément de la liste")
    print("3-Voir le liste")
    print("4-Vider la liste")
    print("5-Quitter")



    user_choice=accueil()
    if user_choice==1:
    
        while True:

            item = input("\nQue voulez-vous ajouter ? (tapez 'exit' pour quitter) ").strip()
            
            if item.lower() == "exit":
                break  # Quitte la boucle
        
            if item in liste:
                print("\nArticle déjà présent")
            else:
                liste.append(item)
                print("L'article a bien été ajouté a votre liste")

        print("Dans la liste de course il y a : \n")        
        for i in liste:
            print(i)

    elif user_choice==2:
        print("\nVoici la liste de course : \n")
        for i in liste:
            print(i)
    
        while True:
                try:
                    choix=int(input("\nQuel élément de la liste voulez-vous retirer ? (tapez 0 pour quitter) "))
                    if choix== 0:
                        break  # Quitte la boucle
                    if 1 <= choix <= len(liste):
                        on=input(f"Vous voulez donc retirer {liste[choix-1]} ? (oui/non) ").lower()
                        while on not in["oui","non"]:
                            on= input(f"Réessayer, Vous voulez donc retirer {liste[choix-1]} ? (oui/non) ").lower()
                        if on=="oui":
                            print(f"\n{liste[choix-1]} a bien été supprimé\n")
                            del liste[choix-1]
                            break
                        elif on =="non":
                            print("D'accord on recommence")
                            continue
                    else:
                        print(f"Erreur : Le nombre doit être entre 1 et {len(liste) }")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")

    elif user_choice==3:
        print("\nVoici la liste de course : \n")
        for i in liste:
            print(i)
        continue
    
    elif user_choice==4:
        sur=input("\nÊtes-vous sur de vouloir vider la liste ? (oui/non)").lower()
        while sur not in ["oui","non"]:
            sur = input ("Réesssayer, Êtes-vous sur de vouloir vider le liste ? (oui/non)").lower()
        if sur=="oui":
            liste.clear()
            print ("\nListe vidé.")
        elif sur =="non":
            print("Retour a l'accueil")
            continue
    
    elif user_choice==5:
        print("Vous avez demandé à ce que le programme s'arrete.\n Fin du programme")
        break