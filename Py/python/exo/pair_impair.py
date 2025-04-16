mot=list(input("Entrez un mot : "))
voyelles=["a","e","i","o","u","y"]
longueur=len(mot)
l=0
for m in mot:
    lettre = m.strip()
    if lettre in voyelles:
        l=l+1
print(l)