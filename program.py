def beolvasas(a, m, lm):
    fr = open("asdd.txt", "r")
    sor =fr.readline()
    while sor != "":
        sor = sor.split()
        a.append(sor[0])
        m.append(sor[1])
        lm.append(sor[2])
        sor =fr.readline()
    fr.close()

#kereses
def megszamolas(a,lm):
    lab40 = []
    for i in range(lm):
        if lm == 40:
            lm[azonosito].append(lab40)
    print(lab40)

#osszegzés

#megszamolas



def main():
    beolvasas(azonosito, magassag, labmeret)
    megszamolas(azonosito, labmeret)
main()