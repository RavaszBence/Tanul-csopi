with open("alma.txt", "r", encoding="UTF8") as fájl:
    szöveg = fájl.read()

print(f"A szöveg karakter száma: {len(szöveg)}")

sortor = []
for sor in szöveg.split("\n"): # sorok megszámolása lista bejárásával
    sortor.append(sor)
print(f"ennyi sor: {len(sortor)}")

szöveg = szöveg.lower()

szavak = szöveg.split()

alma_szo_hanyszor = []
for szó in szavak:
    if szó == "alma":
        alma_szo_hanyszor.append(szó)
        
print(alma_szo_hanyszor)
print(len(alma_szo_hanyszor))

