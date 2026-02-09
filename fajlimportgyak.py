with open("forras.txt", "r", encoding="utf8") as fajl:
    szoveg = fajl.read()
    
butusjelek = [".", ",", ":", "(", ")", "[", "]", "{", "}", "!", "?", "-", ";", "\n"]

for jel in butusjelek:
    szoveg = szoveg.replace(jel, " ") # jelek eltűntetése
    
szoveg = szoveg.lower()

szavak = szoveg.split()

print(f"A szavak száma: {len(szavak)}")

tisztitott = []

for szó in szavak:
    if szó != "":
        tisztitott.append(szó)
        
szavak = tisztitott

g_bvel_kezdodo = []

for szó in szavak:
    if szó[0] == "g":
        g_bvel_kezdodo.append(szó)
        
g_bvel_kezdodo.sort()

print(f"G betűvel kezdődő szavak: {g_bvel_kezdodo}")

with open("kimenetgibson.txt", "w", encoding="utf8") as kifalj:
    print(*g_bvel_kezdodo, sep="; ", file=kifalj)
    
    
gitarszo = []

for szó in szavak:
    if szó == "gitárt":
        gitarszo.append(szó)
        
print(f"A gitárt ennyiszer szerepel: {len(gitarszo)}")