Taille={"Raoul":1.80, #Permet d'ajouter des valeur en créant le  dictionnaire
     "Assia":1.58,
     "Nabila":1.60,
     "Lamya":1.74}
print(Taille["Raoul"]) #Affiche la valeur d'un clé
Taille["Jalal"] = Taille.pop("Raoul") #Permet de changer le nom d'une clé et de supprimer l'ancienne /!\ Place la nouvelle clé à la fin du dictionnaire
print(Taille)

Taille["Victor"]=1.8 #Permet d'ajouter une valeur après avoir crée le dictionnaire
del Taille["Victor"] #Permet de suprimer une clé et sa valeur

Fruits={} #Permet de crée un dictionnaire vide
Fruits["Banane"]="Jaune" #Ajoute une paire au dictionnaire (clé)(valeur)
Fruits["Poire"]="Vert"
Fruits["Mandarine"]="Orange"
print(Fruits["Banane"]) #Appeler la clé permet d'affiché la valeur associé

print(Taille.keys()) #Affiche les clé d'un dictionnaire
print(Taille.values()) #Affiche les valeurs d'un dictionnaire
print(Taille.items()) #Affiche les paires d'un dictionnaire
print(Taille.get("Nabila")) #Affiche la valeur d'une clé /!\ Si la clé n'est pas présente, retourne la valeur 'none' et n'arrete pas le programme
print(Taille.pop("Assia")) #Supprime la clé choisie et retourna le valeur
print("Robert" in Taille) #Verifie si une clé existe dans le dictonnaire (retourne True/False)
Fruits.clear() #Vide le dictionnaire choisi
print(Fruits)

