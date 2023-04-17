def beolvasas(a, m, lm):
    fw = open("asdd.txt", "w")
    sor =fr.readline()
    while sor != "":
        sor = sor.split()
        a.append(sor[0])
        m.append(sor[1])
        lm.append(sor[2])
        sor =fr.readline()
    fw.close()

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