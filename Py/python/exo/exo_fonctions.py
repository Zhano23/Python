def salaire_mensuel(salaire_annuel):
    result_sal_mensuel=salaire_annuel/12
    return(result_sal_mensuel)

def salaire_hebdomadaire(salaire_mensuel):
    result_sal_hebdo=salaire_mensuel/4
    return(result_sal_hebdo)

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    result_sal_horaire=salaire_hebdomadaire/heures_travaillees
    return(result_sal_horaire)

sal_annu=float(input("Entrez votre salaire annuel "))
heure_taff=float(input("Entrez vos heures travailler par semaine "))
salaire_mensuel(sal_annu)
somme=salaire_mensuel(sal_annu)
somme=salaire_hebdomadaire(somme)
somme=salaire_horaire(somme,heure_taff)
somme=somme.__round__(2)
print(f"Votre salaire horaire est de {somme} euros net")