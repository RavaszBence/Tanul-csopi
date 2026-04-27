class A7X_album:
    def __init__(self, album, year, genre, lead_single):
        self.album = album
        self.year = year
        self.genre = genre
        self.lead_single = lead_single
        
    def __str__(self):
        return f"\n{self.album} | {self.year}\nGenre: {self.genre}\n Most popular song: {self.lead_single}"