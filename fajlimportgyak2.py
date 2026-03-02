with open("sevenfold.txt", "r", encoding="utf8") as fajl:
    szoveg = fajl.read()

szavak = szoveg.split()
butus_jelek = [".", ",", "[", "]", "(", ")"]

for jel in butus_jelek:
    szoveg = szoveg.replace(jel, "")
    
print(szoveg)

sortor = []
for sor in szoveg.split("\n"): # sorok megszámolása lista bejárásával
    sortor.append(sor)
print(f"ennyi sor: {len(sortor)}")

a_betus_szavak = []
for szó in szavak:
    if szó[0] == "a" and len(szó) != 1 and len(szó) != 2 or szó[0] == "A" and len(szó) != 1 and len(szó) != 2:
        a_betus_szavak.append(szó)

with open("a_betu_sevenfold.txt", "w", encoding="utf8") as kifajl:
    print("A betűvel kezdődő szavak:",*a_betus_szavak, file=kifajl, sep=" - ")