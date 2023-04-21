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

def picike(l):
    return (min(l))

def valamilab(l:list,s=21):
    if s in l:
        print("itt a kedvenc láb az adatok közt!")
    else:
        print("Nincs ily furcsa lábacska az adataim közt:(")

def menu(a,m,l):
    os.system('cls')
    be = input("Magassághoz írd be: mag |Lábakhoz írd be: labacska |Azonosítókhoz írd be: azon |40-es lábakhoz ird be: uwu |Csepp lábakhoz írd be: icikepicike|Különbejáratuú láb választásához írd be: enmondom|")
    if be == "mag":
        os.system('cls')
        print("Magasságok","\n",*m)
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
        print(*lista)
        be = ""
    elif be == "icikepicike":
        os.system('cls')
        print("Pindúr pandúrok:","\n")
        kis = picike(a,l)
        print(kis)
        be = ""
    elif be == "enmondom":
        os.system('cls')
        no = input("Akarsz e speckó lábacskát megadni? y/n")
        if no == "y":
            zsa = int(input("Mekkorka láb a kedvenced?: "))
            valamilab(l,zsa)
        else:
            print("Választottunk helyetted egy 21-es lábat, most lessük meg benne van e az adataimban!","\n")
            valamilab(l)

        be = ""
    be = input("Szeretnél e további dolgokat meglesni? y/n|")
    if be == "y":
        os.system('cls')
        menu(a,m,l)
    else:
        os.system('cls')

def main():
    micsudi = input("Mit nyissunk meg?(Kiterjesztéssel add meg): ")
    azonosito, magassag, labmeret = [], [], []
    beolvasas(azonosito, magassag, labmeret,micsudi)
    menu(azonosito,magassag,labmeret)

main()