from random import randint
asd = []

for j in range(500):
    azonosito = ""
    for i in range(10):
        
        azonosito += chr(randint(65, 90))
    asd.append(azonosito)

fw = open("asdd.txt", "w")
for i in range(len(asd)):
    fw.write(asd[i]+"\n")
fw.close()