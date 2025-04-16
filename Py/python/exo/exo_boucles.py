i=0
somme=0#initialisation des variables 
sup=[]

nombres = str(input("Entrez une liste de nombre séparé par un espace "))
nombres=nombres.split()#crée une liste via les nombres donner /!\ Ne fonctionne que pour les chaines de caractère
for n in nombres:
    n= int(n)
    nombres[i]=n
    i+=1
    somme=n+somme
    moyenne=somme/len(nombres)
    moyenne=moyenne.__round__(2)
    
for n in nombres:
    if n > moyenne:
        sup.append(n)
long=len(sup)

print(f"la somme des nombres de la liste est de {somme}")
print(f"la moyenne des nombres de la liste est de {moyenne}")
print(f"il y a {long} nombres supérieurs à la moyenne et qui sont {sup}")