szavak2 = []
with open("alma.txt", "r", encoding="UTF8") as fájl:
    szöveg = fájl.read()


print(f"A szöveg karakter száma: {len(szöveg)}")

# butus_jelek = [".", ",", ";", "?", "!", "[", "]"]
# for jel in butus_jelek:
#     szöveg = szöveg.replace(jel, " ")
sortor = []
for sor in szöveg.split("\n"): # sorok megszámolása lista bejárásával
    sortor.append(sor)
print(f"ennyi sor: {len(sortor)}")

szöveg = szöveg.lower()

szavak = szöveg.split()

otleghosszabb = []

for x in range(5):
    leghosszabb = ""
    
    for szo in szavak:
        if len(szo) >= len(leghosszabb):
            leghosszabb = szo
            
    otleghosszabb.append(leghosszabb)
    szavak.remove(leghosszabb)
    
print(otleghosszabb)

szavak2 = szöveg.split()

alma_szo_hanyszor = []
x = -1
alma_szo_indexek = []
for szó in szavak2:
    x += 1
    if szó == "alma":
        print(szó)
        alma_szo_indexek.append(x)
        alma_szo_hanyszor.append(szó)
        
print(alma_szo_hanyszor)
print(len(alma_szo_hanyszor))
print(alma_szo_indexek)

mondatok = szöveg.split(".")


harom_leghossz = []
for x in range(3):
    leghosszmond = ""
    
    for mondat in mondatok:
        if len(mondat) >= len(leghosszmond):
            leghosszmond = mondat
    harom_leghossz.append(leghosszmond)
    mondatok.remove(leghosszmond)
    
print(harom_leghossz)

mondatok2 = szöveg.split(".")

harom_legrovidebb = []
for x in range(3):
    legrovmondd = leghosszmond
    
    for mondat in mondatok2:
        if len(mondat) <= len(legrovmondd):
            legrovmondd = mondat
    harom_legrovidebb.append(legrovmondd)
    mondatok2.remove(legrovmondd)
    
print("\n", harom_legrovidebb)

