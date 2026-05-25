import random

szamlista = []

# toltsd fel a listat 40 db veletlenszeru szammal 1 és 100 kozott
for szam in range(40):
    szamlista.append(random.randint(1, 100))
    
# átlag számítás listából 2 tizedes
print(f"A lista átlaga: {sum(szamlista) / len(szamlista):.2f}")


# szúrd be a lista végére a 999-et
szamlista.append(999)
print("\n", szamlista)

# vegyük el a lista végéről a 999-et
szamlista.remove(999)
print("\n", szamlista)

# szúrd be a lista elejére a 879-et
szamlista.insert(0, 879)
print("\n", szamlista)

# szúrd be a lista 10. indexére a 700-at
szamlista.insert(9, 700)
print("\n", szamlista)

# vegyük el a lista 10. indexéről a 700-at
szamlista.pop(9)
print("\n", szamlista)