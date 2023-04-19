import os

def beolvasas(a, m, lm,mi):
    fr = open(mi, "r")
    sor =fr.readline()
    while sor != "":
        sor = sor.split()
        a.append(sor[0])
        m.append(int(sor[1]))
        lm.append(int(sor[2]))
        sor =fr.readline()
    fr.close()

def kivalogatas(a,lm):
    lab40 = []
    for i in range(len(lm)):
        if lm[i] == 40:
            lab40.append(a[i])
    return(lab40)

def picike(a,l):
    picurka = []
    for i in range(len(l)):
        if l[i] == min(l):
            picurka.append(a[i])
    return (picurka)

def menu(a,m,l):
    os.system('cls')
    be = input("Magassághoz írd be: mag |Lábakhoz írd be: labacska |Azonosítókhoz írd be: azon |40-es lábakhoz ird be: uwu |Csepp lábakhoz írd be: icikepicike|")
    if be == "mag":
        os.system('cls')
        print("Magasságok","\n",*a)
        be = ""
    elif be == "labacska":
        os.system('cls')
        print("Lábak","\n",*l)
        be = ""
    elif be == "azon":
        os.system('cls')
        print("Azonositok","\n" , *a)
        be = ""
    elif be == "uwu":
        os.system('cls')
        print("40-es lábú gengszterek:","\n")
        lista = kivalogatas(a,l)
        print(lista)
        be = ""
    elif be == "icikepicike":
        os.system('cls')
        print("Pindúr pandúrok:","\n")
        lista = picike(a,l)
        print(*lista)
        be = ""
    be = input("Szeretnél e további dolgokat meglesni? y/n|")
    if be == "y":
        os.system('cls')
        menu(a,m,l)

def main():
    micsudi = input("Mit nyissunk meg?(Kiterjesztéssel add meg): ")
    azonosito, magassag, labmeret = [], [], []
    beolvasas(azonosito, magassag, labmeret,micsudi)
    menu(azonosito,magassag,labmeret)


main()