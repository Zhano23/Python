fruits ={
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange",
}

fruits["kiwi"] ="vert"

couleur_banane=fruits["banane"]
fruits["pomme"] = "vert"
del fruits["banane"]
print(fruits)


Ville ={
    "nom":"Montreal",
    "pays":"Canada",
    "province":"Quebec",
    "pop":1825208,
    "superficie(km²)":315
        }

Ville["superficie(km²)"] = 365
Ville["Densité(km²)"] = 4992
Ville["Populaltion"] = Ville.pop("pop")
print(Ville)
