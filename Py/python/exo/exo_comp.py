nombre1 = str(input("Entrez un 1er nombre: "))
nombre2 = str(input("Entrez un 2eme nombre: "))
if nombre1.isnumeric() == False or nombre2.isnumeric() == False:
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")
else:
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

operation = str(input("Choisissez un type d'opération (+ - * /) : "))
if operation =="+":
    resultat=nombre1+nombre2
    print (resultat)
elif operation == "-":
    resultat=nombre1-nombre2
    print(resultat)
elif operation == "*":
    resultat=nombre1*nombre2
    print(resultat)
elif operation == "/":
    if nombre2 == 0:
        print("Erreur: impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")
    resultat=nombre1/nombre2
    resultat=resultat.__round__(2)
    print(resultat)
else:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")