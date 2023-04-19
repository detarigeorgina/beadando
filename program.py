import os

def beolvasas(a, m, lm):
    fr = open("asdd.txt", "r")
    sor =fr.readline()
    while sor != "":
        sor = sor.split()
        a.append(sor[0])
        m.append(int(sor[1]))
        lm.append(int(sor[2]))
        sor =fr.readline()
    fr.close()

#kereses
def megszamolas(a,lm):
    lab40 = []
    for i in range(len(lm)):
        if lm[i] == 40:
            lab40.append(a[i])
    print(lab40)

#osszegzés

#megszamolas



def main():
    azonosito, magassag, labmeret = [], [], []
    beolvasas(azonosito, magassag, labmeret)
    megszamolas(azonosito, labmeret)
    print("Azonositok","\n" , *azonosito)
    be = input("Kövihez nyomd meg: y ")
    if be == "y":
        os.system('cls')
        be = ""
        print("Magasságok","\n",*magassag)
        be = input("Kövihez nyomd meg: y ")
        if be == "y":
            os.system('cls')
        be = ""
        print("Lábak","\n",*labmeret)

main()