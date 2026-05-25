class Karakter:
    def __init__(self, Name, Race, Class, Level, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, HitPoints):
        self.Name = Name
        self.Race = Race
        self.Class = Class
        self.Level = int(Level)
        self.Strength = int(Strength)
        self.Dexterity = int(Dexterity)
        self.Constitution = int(Constitution)
        self.Intelligence = int(Intelligence)
        self.Wisdom = int(Wisdom)
        self.Charisma =int(Charisma)
        self.HitPoints = int(HitPoints)
        
        
    def __str__(self):
        return f"\n\n{self.Name}\nRace: {self.Race}\nClass: {self.Class}\nLevel: {self.Level}\nStrength: {self.Strength}\nDexterity: {self.Dexterity}\nConstitution: {self.Constitution}\nIntelligence: {self.Intelligence}\nWisdom: {self.Wisdom}\nCharisma: {self.Charisma}\nHit points: {self.HitPoints}"
        