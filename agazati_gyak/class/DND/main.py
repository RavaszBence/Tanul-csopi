from modul import Karakter


karakterek = []
with open("dnd_characters.csv", "r", encoding="utf-8") as file:
    next(file)
    for sor in file:
        adat = sor.strip().split(",")
        karakterek.append(Karakter(adat[0], adat[1], adat[2], adat[3], adat[4], adat[5], adat[6], adat[7], adat[8], adat[9], adat[10]))
        

for karakter in karakterek:
    print(karakter)
    
# írd ki kinek a legnagyobb az ereje

legerosebb = karakterek[0]

for karakter in karakterek:
    if karakter.Strength > legerosebb.Strength:
        legerosebb = karakter
        
print(legerosebb.Name)
