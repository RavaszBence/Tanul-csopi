from modul import A7X_album

a7x_albums = []

with open("a7x.csv", "r", encoding="utf-8") as file:
    next(file)
    for sor in file:
        data = sor.strip().split(",")
        a7x_albums.append(A7X_album(data[0], data[1], data[2], data[3]))
        
for album in a7x_albums:
    print(album)