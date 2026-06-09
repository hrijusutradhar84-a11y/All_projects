import shop
import quests 

class City:
    def __init__(self, name):
        self.name = name
        self.city_shop = shop.shop1 
        self.quests_list = []       

    def show_shop(self):
        print(f"Welcome to the market of {self.name}!")
        self.city_shop.display_items()

    def display_quests(self):
        print(f"--- Quest Board of {self.name} ---")
        if not self.quests_list:
            print("No quests available right now.")
        else:
            for index, quest in enumerate(self.quests_list, start=1):
                print(f"{index}. {quest.description} (+{quest.coins}g, +{quest.fame} fame)")

