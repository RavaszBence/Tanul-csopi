import random

random_szamok = []
for x in range(50):
    random_szamok.append(random.randint(0, 100))


with open("random szamok.txt", "w", encoding="UTF8") as kifájl:
    print(f"Random generált számok: {random_szamok}", file=kifájl) # print a fájlba
    print("A fájl elkészült!") # üzenet a konzolba
    