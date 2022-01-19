import random
def beolvas(filenev):
    # ide jön a kód
    lista = []
    forrasfile = open(filenev,mode='r',encoding='UTF-8')
    for sor in forrasfile:
        lista.append(sor.strip())
    forrasfile.close()
    return lista

def feladvany(szo):
    return szo[0] + "." * (len(szo) - 2) + szo[-1]

def cserel(feladvany, szo, betu):
    eredmeny = szo[0]
    for i in range(1, len(szo)-1):
        if szo[i] == betu:
            eredmeny += betu
        else:
            eredmeny += feladvany[i]
    eredmeny += szo[-1]
    return eredmeny 

def keres(feladvany, lista):
    eredmeny=[]
    for helyseg in lista:
        if len(feladvany) == len(helyseg) and helyseg[0] == feladvany[0] and helyseg[-1] == feladvany[-1]:
            eredmeny.append(helyseg)
    return eredmeny

def betutipp(feladvany:str, helyseg):
    index = feladvany.index('.')
    return helyseg[index]

def ellenor(eredeti, uj, betu):
    if len(eredeti) != len(uj):
        return False
    for i in range(len(eredeti)):
        if eredeti[i] != uj[i]:
            if eredeti[i] != '.':
                return False
            else:
                if uj[i] != betu:
                    return False  
    return True

def kizar(lista, betu):
    eredmeny=[]
    for helyseg in lista:         
        if not betu in helyseg[1:-1]:
            eredmeny.append(helyseg)
    return eredmeny


