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
    print(*lab40)

def main():
    azonosito, magassag, labmeret = [], [], []
    beolvasas(azonosito, magassag, labmeret)
    be = input("Magassághoz írd be: mag |Lábakhoz írd be: labacska |Azonosítókhoz írd be: azon |40-es lábakhoz ird be: uwu|")
    if be == "mag":
        print("Magasságok","\n",*magassag)
        be = ""
    elif be == "labacska":
        print("Lábak","\n",*labmeret)
        be = ""
    elif be == "azon":
        print("Azonositok","\n" , *azonosito)
        be = ""
    elif be == "uwu":
        print("40-es lábú gengszterek:","\n")
        megszamolas(azonosito,labmeret)
        be = ""

main()