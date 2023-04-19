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

def menu(a,m,l):
    be = input("Magassághoz írd be: mag |Lábakhoz írd be: labacska |Azonosítókhoz írd be: azon |40-es lábakhoz ird be: uwu|")
    if be == "mag":
        print("Magasságok","\n",*a)
        be = ""
    elif be == "labacska":
        print("Lábak","\n",*l)
        be = ""
    elif be == "azon":
        print("Azonositok","\n" , *a)
        be = ""
    elif be == "uwu":
        print("40-es lábú gengszterek:","\n")
        lista = kivalogatas(a,l)
        print(lista)
        be = ""
    be = input("Szeretnél e további dolgokat meglesni? y/n|")
    if be == "y":
        menu(a,m,l)

def main():
    micsudi = input("Mit nyissunk meg?(Kiterjesztéssel add meg): ")
    azonosito, magassag, labmeret = [], [], []
    beolvasas(azonosito, magassag, labmeret,micsudi)
    menu(azonosito,magassag,labmeret)


main()