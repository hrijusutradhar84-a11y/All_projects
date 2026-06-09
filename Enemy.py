class Enemy:
    def __init__(self, name, health, damage, weapon, reload):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.reload = reload


Goblin = Enemy("Goblin", 50, 10, "Dagger", 1)
Orc = Enemy("Orc", 100, 25, "Axe", 1.2)
Troll = Enemy("Troll", 150, 50, "Club", 1.5)
Dragon = Enemy("Dragon", 300, 60, "Fire Breath", 2)
Demon_lord = Enemy("Swarno", 500, 100, "Dark Magic", 2.5)
Demon_lord2 = Enemy("Debojit", 500, 100, "Dark Magic", 3)
Demon_god = Enemy("Demon God", 1000, 200, "Ultimate Darkness", 5)
