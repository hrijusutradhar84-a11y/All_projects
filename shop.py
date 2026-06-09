import items

class Shop:
    def __init__(self):
        self.showcase = []
    
    def display_items(self):
        print ('---SHOP---')
        for item in self.showcase:
            print(f"{item.name} - {item.price} coins")

item1 = items.Item("Health potion", 30)
item2 = items.Item("attack potion", 40)
item3 = items.Item("Demonic Axe", 150)
item4 = items.Item("Halo blade", 120)
item5 = items.Item("Holy Sword", 250)
shop1 = Shop()
shop1.showcase = [
    item1,
    item2,
    item3,
    item4,
    item5
]
