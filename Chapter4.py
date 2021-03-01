from Helpers import clearScreen 
import random
from Constants import *
from Chapter5 import Chapter5

class Chapter4:
    choices = [
        "Buy Guns - make your ship's attacks stronger",
        "Buy Armor - improve your ship's resiliance to enemy attacks",
        "Sell Booty - exchange your plundered booty for cold, hard cash",
        "Repair Ship - restore your ship's health"
    ]
    complete = False

    def __init__(self, player):
        self.player = player
        self.startChapter()

    def startChapter(self):
        print("You’ve made it back to port. Time to spend some loot!")
        self.chapterLoop()

    def presentChoices(self):
        print("\nYou've got some choices to make. You can:")
        for i in range(0, 4):
            print(str(i + 1) + " - " + self.choices[i])

    def getChoice(self):
        return input("\nWhich do you choose? (1 - 4) ")

    def chapterLoop(self):
        while(not self.complete):
            self.presentChoices()
            choice = self.getChoice()
            clearScreen()
            self.handleChoice(choice)
            stay = input("Would you like to perform any more actions? (Y/N)")
            if stay != "Y" and stay != "y":
                self.complete = True

        if self.complete:
            Chapter5(self.player)

    def buyGuns(self):
        print("You chose to Buy Guns")
        print("Your ship currently has an attack strength of " + str(self.player.shipAttack) + ".")
        print("You have " + str(self.player.loot) + " gold pieces.")
        print("You can upgrade the ship's guns at a price of " + str(ATTACK_POINT_PRICE) + " gold pieces per attack point.")
        attackPointsPurchased = int(input("How many attack points do you want to buy?"))
        if attackPointsPurchased * ATTACK_POINT_PRICE <= self.player.loot:
            self.player.shipAttack += attackPointsPurchased
            self.player.loot -= attackPointsPurchased * ATTACK_POINT_PRICE
            print("Ship's attack has been upgraded to " + str(self.player.shipAttack))
        else:
            print("You don't have enough money to buy that many attack points.")

    def buyArmor(self):
        print("You chose to Buy Armor")
        print("Your ship currently has defense strength of " + str(self.player.shipArmor) + ".")
        print("You have " + str(self.player.loot) + " gold pieces.")
        print("You can upgrade the ship's armor at a price of " + str(ARMOR_POINT_PRICE) + " gold pieces per armor point.")
        armorPointsPurchased = int(input("How many armor points do you want to buy?"))
        if armorPointsPurchased * ARMOR_POINT_PRICE <= self.player.loot:
            self.player.shipArmor += armorPointsPurchased
            self.player.loot -= armorPointsPurchased * ARMOR_POINT_PRICE
            print("Ship's armor has been upgraded to " + str(self.player.shipArmor))
        else:
            print("You don't have enough money to buy that many armor points.")

    def sellBooty(self):
        print("You chose to sell some Booty")
        print("You have booty worth a value of " + str(self.player.booty) + ".")
        negotiate = input("Do you want to try to negotiate a better price? (Y/N)")
        if negotiate == "y" or negotiate == "Y":
            multiplier = random.randint(50, 200)
            saleValue = self.player.booty * multiplier / 100
        else:
            saleValue = self.player.booty
        print("You've sold your booty for a total price of " + str(saleValue) + ".")
        self.player.booty = 0
        self.player.loot += saleValue

    def repairShip(self):
        print("You chose to repair your ship")
        print("Your ship currently has " + str(self.player.hp) + " hp out of a max possible " + str(STARTING_HP) + "hp.")
        print("You have " + str(self.player.loot) + " gold pieces.")
        print("You can repair the ship at a price of " + str(HP_PRICE) + " gold pieces per hp.")
        hpPurchased = int(input("How many hp do you wish to purchase?"))
        if hpPurchased + self.player.hp > STARTING_HP:
            hpPurchased = STARTING_HP - self.player.hp
        if hpPurchased * HP_PRICE <= self.player.loot:
            self.player.hp += hpPurchased
            self.player.loot -= hpPurchased * HP_PRICE
            print("Ship's hp is " + str(self.player.hp))
        else:
            print("You don't have enough money to buy that many hp.")


    def checkForChapterComplete(self):
        self.complete = self.enemyHp <= 0

    def checkForPlayerKilled(self):
        self.gameOver = self.player.hp < 0

    def handleChoice(self, choice):
        choice = int(choice)
        print(choice)
        options = { 1 : self.buyGuns,
                    2 : self.buyArmor,
                    3 : self.sellBooty,
                    4 : self.repairShip
        }
        if choice > 0 and choice < 4:
            options[choice]()
        