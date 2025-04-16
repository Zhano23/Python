dec = int(input("Veuillez entrer un nombre a convertir: "))
bin = dec%2
dec = dec//2
while dec != 0:
    bin = dec%2
    dec = dec//2
    print(bin)