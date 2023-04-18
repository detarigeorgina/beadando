from random import randint
asd = []
magasok = []

for j in range(500):
    magasok.append(randint(140,195))

while len(asd) < 500:

    azonosito = ""
    for i in range(10):
        
        azonosito += chr(randint(65, 90))
    if azonosito not in asd:
        asd.append(azonosito)
    pass

fw = open("asdd.txt", "w")
for i in range(len(asd)):
    fw.write(asd[i]+"\n")
fw.close()