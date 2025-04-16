fruits=["pomme","poire","orange","banane"] 
#Liste

print(fruits[2]) #affiche le 3eme élément
print(fruits[-3])#Afficher le 3eme élément en partant de la fin le 0 reste le meme
fruits[1]="peche" #modifie poire en peche
print(fruits[1]) #Affiche le 2eme élément
print(fruits)#Affiche la liste entiere

fruits.append("raisin") #Ajoute raisin a la fin de la liste
print(fruits)
fruits.remove('orange')#Retire orange de la liste

print(fruits)
print(f"Il y a {len(fruits)} élément dans la liste.")#affiche la longueur d'une liste
fruits.reverse()#Inverse l'orde des éléments d'une liste 
print(fruits)
fruits.sort() #Trie par  ordre alphabetique 

del fruits[2] #Supprime le 3eme élément d'une liste
print(fruits)

print(f"Il y a {fruits.count("banane")} fois banane dans la liste")#Compte le nombre de répétition d'un mot dans une liste
print(f"Banane est à l'emplacement {fruits.index("banane")}")#Permet de connaitre l'emplacement d'un élément d'une liste/!\ Ne fonctionne pas sur les doubles liste seulement les plates
fruits.insert(1,"bob")#Permet d'insérer un nouvel élétement dans une liste à l'emplacement voulu. (un seul)
print(fruits)
print(f"Le mot {fruits.pop(3)} a été supprimé de la liste") #Supprime l'élément choisie de la liste mais l'affiche dans la console


liste = [1,2]

#Append ne permet d'ajouter qu'un seul élément (une liste est considéré comme un seul élément meme si elle en contient plusieurs)

liste.append(3)
liste.append([4,5,6]) #Ajoute 4, 5 et 6 comme 3eme élements de la liste dans une nouvelle liste en tant que nombre et non chaine de caratère

#Extend permet d'ajouter plusieurs éléments à une liste

liste.extend(["pomme","poire"]) #Ajoute pomme et poire comme 4 et 5eme élément de la liste
liste.extend("8""9") #Ajoute 8 et 9 comme 6 et 7eme élément de la liste comme chaine de caractère
print(liste)#Affiche la liste complète
print(f"La 5eme lettre du 4eme élément de la liste est {liste[4][4]}") #Affiche la 5eme lettre du 4eme élément de la liste (e de pommme)
print(f"La 3eme lettre en partant de la fin du 5eme élément de la liste est {liste[5][-3]}") #Affiche la 3eme lettre en partant de la fin du 5eme élément de la liste (i de poire)
print(f"Le 2eme élément de la 2eme liste est {liste[3][1]}") #Affiche le 2eme élément de la nouvelle liste (5 de la liste [4,5,6])
print(f"Le 5eme éléments de la liste est {liste[4]}") #Affiche le 5eme élément de la liste(pomme)



#Un tuple est une liste non modifiable on ne oeut qu'ajouter un autre tuple et rien d'autre 
#Pour crée un tuple on remplace les crochets par des parenthèses

mon_tuple = (1,2,3)
print(mon_tuple)
bis_tuple = (4,"cinq","six")
print(bis_tuple)
nouv_tuple=mon_tuple+bis_tuple
print(nouv_tuple)
print("six" in nouv_tuple) #Veifie si la valeur cher se trouve dans la liste/tuple
