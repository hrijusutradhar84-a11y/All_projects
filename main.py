import city; import quests
import player; import Enemy; import weapon
import shop ;import items

import random
import pygame

'''-----------------CITY DEFINITION-------------------'''

city1 = city.City("Delmir")
city2 = city.City("Aelmir")
city3 = city.City("Seimir")
city4 = city.City("Debomir")
city5 = city.City("Swarnmir")

city_list = [city1, city2, city3, city4, city5]

'''-------------------------------QUESTS AND CITIES---------------------------------------------------'''

city1.quests_list = [
    quests.Quest("Defeat the Goblin King", 100, 50, Enemy.Goblin),
    quests.Quest("Rescue the Villagers", 150, 75, Enemy.Orc)
]
city2.quests_list = [
    quests.Quest("Slay the Orc Warlord", 200, 100, Enemy.Orc),
    quests.Quest("Defeat the Troll", 50, 25, Enemy.Troll)
]
city3.quests_list = [
    quests.Quest("Defeat the Dragon", 300, 150, Enemy.Dragon),
    quests.Quest("Defeat 1 troll", 250, 125, Enemy.Troll)
]
city4.quests_list = [
    quests.Quest("Defeat the Demon Lord", 500, 250, Enemy.Demon_lord),
    quests.Quest("Defeat the Demon Lord2", 500, 250, Enemy.Demon_lord2)
]
city5.quests_list = [
    quests.Quest("Defeat the Demon God", 1000, 500, Enemy.Demon_god)
]
'''---------------------------CHARECTER CHOICE---------------------------------------------------'''


def char_choose():
    print("Choose your character:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        return player.Player("Warrior", 150, weapon.Weapon("Sword", 20, 1, 1))
    elif choice == "2":
        return player.Player("Mage", 100, weapon.Weapon("Staff", 30, 1, 1))
    elif choice == "3":
        return player.Player("Archer", 120, weapon.Weapon("Bow", 25, 1, 1))
    else:
        print("Invalid choice. Please try again.")
        return char_choose()

player1 = char_choose()
print(f"Welcome {player1.name} to the world of adventure!")


'''-------------------------------PLAYER INPUT---------------------------------------------------'''
def playerinput():
    print("What do you want to do?")
    print("1. Move")
    print("2. Shop")
    print("3. Check Inventory")
    print("4. Check Stats")
    print("5. Quit")
    print("6. Quests")
    
    choice = input("Enter your choice: ")
    return choice
def actual_choice():
    choice = playerinput()
    
    #FOR MOVING BETWEEN CITIES
    if choice == "1":
        print("Where do you want to go?")
        for i in range(len(city_list)):
            print(f"{i+1}. {city_list[i].name}")
        city_choice = input("Enter your choice: ")
        if city_choice in ["1", "2", "3", "4", "5"]:
            player1.Current_location = int(city_choice) - 1
            print(f"You have moved to {city_list[player1.Current_location].name}")
        else:
            print("Invalid choice. Please try again.")
    
    # FOR THE SHOP
    if choice == '2':
        print("Welcome to the shop!")
        shop.shop1.display_items()
        X = input("Do you want to buy something? (yes/no): ")
        if X.lower() == "yes":
            item_choice = input("Enter the name of the item you want to buy: ")
            for item in shop.shop1.showcase:
                if item.name.lower() == item_choice.lower():
                    if player1.coins >= item.price:
                        player1.coins -= item.price
                        player1.inventory.append(item)
                        shop.shop1.showcase.remove(item)
                        print(f"You have bought {item.name}!")
                    else:
                        print("You don't have enough coins!")
                    break
            else:
                print("Item not found!")
        else:            print("Maybe next time!")
    # CHECKING INVENTORY
    if choice == '3':
        print("Your inventory:")
        if not player1.inventory:
            print("Your inventory is empty.")
        else:
            for item in player1.inventory:
                print(f"{item.name} - {item.price} coins")
            y = input("Do you want to use an item? (yes/no): ")
            if y.lower() == "yes":
                item_choice = input("Enter the name of the item you want to use: ")
                for item in player1.inventory:
                    if item.name.lower() == item_choice.lower():
                        if item.name == "Health potion":
                            player1.health += 50
                            print("You have used a Health potion! Your health has increased by 50.")
                        elif item.name == "attack potion":
                            player1.weapon.damage += 5
                            print("You have used an attack potion! Your weapon damage has increased by 5.")
                        elif item.name == "Demonic Axe":
                            player1.weapon = weapon.Weapon("Demonic Axe", 50, 1, 1)
                            print("You have equipped the Demonic Axe! Your weapon damage is now 50.")
                        elif item.name == "Halo blade":
                            player1.weapon = weapon.Weapon("Halo blade", 40, 1, 1)
                            print("You have equipped the Halo blade! Your weapon damage is now 40.")
                        elif item.name == "Holy Sword":
                            player1.weapon = weapon.Weapon("Holy Sword", 60, 1, 1)
                            print("You have equipped the Holy Sword! Your weapon damage is now 60.")
                        player1.inventory.remove(item)
                        break
                else:
                    print("Item not found!")

    # CHECKING STATS
    if choice == '4':
        print(f"Name: {player1.name}")
        print(f"Health: {player1.health}")
        print(f"Weapon: {player1.weapon.name} (Damage: {player1.weapon.damage + player1.damage})")
        print(f"Coins: {player1.coins}")
        print(f"Current Location: {city_list[player1.Current_location].name}")
        print(f"Fame: {player1.fame}")

    # QUITTING THE GAME
    if choice == '5':
        print("Thanks for playing! Goodbye!")
        exit()
    # CHECKING QUESTS
    if choice == '6':
        city_list[player1.Current_location].display_quests()
        quest_choice = input("Do you want to accept a quest? (yes/no): ")
        if quest_choice.lower() == "yes":
            quest_number = input("Enter the number of the quest you want to accept: ")
            if quest_number.isdigit() and 1 <= int(quest_number) <= len(city_list[player1.Current_location].quests_list):
                selected_quest = city_list[player1.Current_location].quests_list[int(quest_number) - 1]
                print(f"You have accepted the quest: {selected_quest.description}")
                fight(selected_quest.target)
                if selected_quest.target.health <= 0:
                    player1.coins += selected_quest.coins
                    player1.fame += selected_quest.fame
                    print(f"You have completed the quest and earned {selected_quest.coins} coins and {selected_quest.fame} fame!")
                    city_list[player1.Current_location].quests_list.remove(selected_quest)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Maybe next time!")

'''-------------------------------FIGHT FUNCTION---------------------------------------------------'''

def fight(enemy):
    time = 0
    Total_damage_dealt = 0
    Total_damage_received = 0
    while enemy.health > 0 and player1.health > 0:
        # Player attacks first
        if time % player1.weapon.reload == 0:
            damage_dealt = player1.weapon.damage + player1.damage + random.randint(0, max(1, int(player1.levels * 5))) + random.randint(0, int(player1.weapon.crit*10)) / 2
            enemy.health -= damage_dealt
            Total_damage_dealt += damage_dealt
            player1.levels += (damage_dealt // 100)
            print(f"You attack the {enemy.name} with your {player1.weapon.name} and deal {damage_dealt} damage!")
        
        if enemy.health <= 0:
            print(f"You have defeated the {enemy.name}!")
            return
        
        
            # Enemy attacks back
        if time % enemy.reload == 0:
            damage_received = enemy.damage - random.randint(0, max(1, int(player1.levels * 5))) + random.randint(0, int(enemy.damage)) / 2
            player1.health -= damage_received
            Total_damage_received += damage_received
            print(f"The {enemy.name} attacks you with its {enemy.weapon} and deals {damage_received} damage!")
        
        if player1.health <= 0:
            print("You have been defeated! Game Over.")
            exit()
        time += 0.2
    player1.health += Total_damage_received
    enemy.health += Total_damage_dealt
'''-------------------------------MAIN GAME LOOP---------------------------------------------------'''
while True:
    actual_choice()