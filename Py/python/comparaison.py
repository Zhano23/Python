animal = str(input("Entrez le nom d'un animal "))
match animal:
    case "chat" :
        print("Les chats sont très calme")
    case "chien":
        print("Je prefere les chiens aux chats")
    case "oiseau" :
        print("se reveil tot font du bruit et faut de la place pour une cage")
    case "poisson":
        print("il faut un aquarium donc de la place")
    case _:
        print("C'est pas dans ma base de donnée")

nbr = str(input("Entrez un nombre "))
if nbr.isnumeric()==True:
    print("c'est un nombre let's go")

else :
    print("c'est pas un nombre")