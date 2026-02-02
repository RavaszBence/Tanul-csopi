import random


def general(tol: int, ig: int, db: int) -> list:
    random_szamok = []
    for _ in range(db):
        random_szamok.append(random.randint(tol, ig))
    return random_szamok

szamlista = general(int(input(f"Add meg hánytól kezdődjön a lista: ")), int(input("Add meg meddig tartson a lista: ")), int(input("Add meg hány db elemet tartalamzzon a lista: ")))

with open("random szamok2.txt", "w", encoding="UTF8") as kifájl:
    print(f"Random generált számok: {szamlista}", file=kifájl) # print a fájlba
    print("A fájl elkészült!") # üzenet a konzolba
    