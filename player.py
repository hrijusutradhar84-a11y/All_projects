class Player:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.damage = 1
        self.fame, self.levels, self.coins = 0, 0, 0
        self.Current_location = 0
        self.inventory = []