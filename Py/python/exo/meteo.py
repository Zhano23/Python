temps= str(input("Fait-il beau ? "))
temps=temps.lower()

while temps not in ["oui", "non"]:
    temps= input("Réessayer, Fait-il beau ? ").lower()
    
if temps=="oui":
    print("vous pouvez aller a la plage")
elif temps=="non":
    pluie = str(input("Il pleut ? :"))

    while pluie not in ["oui", "non"]:
        pluie = input("Réessayer, Il pleut ? ").lower()
    
    if pluie=="oui":
        print("Pensez à prendre un parapluie")
    elif pluie=="non" :
        neige =str(input("Il neige ?"))

        while neige not in ["oui", "non"]:
            neige = input("Réessayer, Il neige ? ").lower()

        if neige=="oui":
            print("Pensez à prendre des bottes ou mettre des chaines au roues de la voiture")
        else :
            print("Restez quand meme a la maison")