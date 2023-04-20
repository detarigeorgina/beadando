from random import randint
asd = []
magasok = []
lm = []

for j in range(500):
    magasok.append(randint(140,195))
    lm.append(randint(12, 49))

while len(asd) < 500:

    azonosito = ""
    for i in range(10):
        
        azonosito += chr(randint(65, 90))
    if azonosito not in asd:
        asd.append(azonosito)
    pass

fw = open("be.txt", "w")
for i in range(20):
    fw.write(asd[i]+" "+str(magasok[i])+" "+  str(lm[i]) + "\n")
fw.close()
