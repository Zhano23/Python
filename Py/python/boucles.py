for i in range (100):
    if i == 52:
        break #arrete la boucle et  va à la suite du programme
    print(f"J'ai {i} ans")

reponse=str(input("Tu as faim ? ")).lower()
while reponse not in ["oui", "non"]:
    reponse= input("Réessayer, Tu as faim ? ").lower()
if reponse == "oui":
    print("Allons manger")
else:
    print("Alors on a encore le temps")

animaux=["chien","chat","poisson","oiseau"]
for n in animaux:
    if n=="poisson":
        continue
    print(n)
    