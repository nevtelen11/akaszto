def main():
    helysegek = beolvas("helyek.txt")
    feladat = random.choice(helysegek)
    kiirando = feladvany(feladat)
    print(kiirando)
    proba = 6
    while "." in kiirando and proba > 0:
        betu = input("adj meg egy betut: ")
        if len(betu) > 1:
            if betu.lower() != feladat.lower():            
                proba = 0
            break

        if betu in feladat[1: -1]:
            kiirando = cserel(kiirando, feladat, betu)
        else:
            proba -= 1
            print("a hianyzo betu kozott nem talalhato", proba, "tipped van meg")            
        print(kiirando)

    if proba > 0:
        print("grat")
    else:
        print("jo bena vagy a gondolt szo: ", feladat)

    print("Most te gondolj!")
    kiirando=input("Írd be a feladványt:")
    lehetsegesek = keres(kiirando, helysegek)
    #print(lehetsegesek)
    # while ciklus inkább, amíg több mint 1 lehetséges van!
    if len(lehetsegesek) == 0:
        print("Nincs ilyen település.")
    elif len(lehetsegesek) == 1:
        print(lehetsegesek[0], "a gondolt város.")
    else:
        betu = betutipp(kiirando, lehetsegesek[0])
        valasz = input(f"Van benne '{betu}' betű? (i/n): ")
        if valasz == "i":
            kiirando2=input("Írd be a feladványt:")
            while not ellenor(kiirando, kiirando2, betu):
                kiirando2=input("Írd be a feladványt:")
            lehetsegesek = keres(kiirando, lehetsegesek)
        else:
            lehetsegesek = kizar(lehetsegesek, betu)
            
      

