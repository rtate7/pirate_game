# Bob Tate
# 2/28/2021

# Chapter 1 - This file contains the story elements for the first chapter of the game.

from Helpers import clearScreen 
import random
from Constants import *
from Chapter2 import Chapter2

class Chapter1:
    choices = [
        "Sneak - move slowly towards the ship",
        "Run - move quickly towards the ship",
        "Steal - steal loot from the townspeople",
        "Bribe - pay off the crew members who are searching for you"
    ]
    complete = False
    gameOver = False
    distanceToShip = STARTING_DISTANCE_TO_SHIP
    hiddenTurns = 0

    def __init__(self, player):
        self.player = player
        self.startChapter()

    def startChapter(self):
        print("You’ve just won a pirate’s ship in a game of Liar’s Dice. He’ll uphold his side of the bargain by allowing you to take the ship if you can get on board before the crew kills you. Escape with your ship and your life!")
        self.chapterLoop()

    def presentChoices(self):
        print("\nYou've got some choices to make. You're " + str(self.distanceToShip) + " paces away from the ship. You can:")
        for i in range(0, 4):
            print(str(i + 1) + " - " + self.choices[i])

    def getChoice(self):
        return input("\nWhich do you choose? (1 - 4) ")

    def chapterLoop(self):
        while(not self.complete and not self.gameOver):
            self.presentChoices()
            choice = self.getChoice()
            clearScreen()
            self.handleChoice(choice)
            self.checkForPlayerKilled()
            self.checkForChapterComplete()
            if self.hiddenTurns > 0:
                self.hiddenTurns -= 1
        if self.gameOver:
            print("Thanks for playing, but you've been killed.")
            playAgain = input("Want to play again? (Y/N)")
            if playAgain == 'Y' or playAgain == 'y':
                self.player.reset()
                Chapter1(self.player)
        elif self.complete:
            Chapter2(self.player)

    def checkForFound(self):
        badGuyPerception = random.randint(10, 30)
        sneakiness = random.randint(1, 6) * self.player.stealth
        return badGuyPerception > sneakiness

    def sneak(self):
        print("You chose Sneak")
        move = random.randint(1, 6)
        print("\n\nYou managed to get " + str(move) + " paces closer to the ship.")
        self.distanceToShip -= move
        self.stealth = SNEAK_STEALTH
        if self.hiddenTurns == 0 and self.checkForFound():
            print("You were found and had to fight your way out.")
            self.player.takeDamage(CH_ONE_BAD_GUY_STRENGTH)

    def run(self):
        print("You chose Run")
        move = random.randint(5, 30)
        print("\n\nYou managed to get " + str(move) + " paces closer to the ship.")
        self.distanceToShip -= move
        self.stealth = RUN_STEALTH
        if self.hiddenTurns == 0 and self.checkForFound():
            print("You were found and had to fight your way out.")
            self.player.takeDamage(CH_ONE_BAD_GUY_STRENGTH)

    def steal(self):
        print("You chose Steal")
        amountStolen = random.randint(5, 30)
        self.player.loot += amountStolen
        print("You managed to steal " + str(amountStolen) + " gold pieces")
        self.stealth = STEAL_STEALTH
        if self.hiddenTurns == 0 and self.checkForFound():
            print("You were found and had to fight your way out.")
            self.player.takeDamage(CH_ONE_BAD_GUY_STRENGTH)

    def bribe(self):
        print("You chose Bribe")
        price = random.randint(5, 20)
        print("for a price of " + price + " gold coins, the search will be called off for two turns")
        choice = input("Do you want to pay the price? (Y/N)")
        if input == 'Y' or input == 'y':
            if self.player.loot >= price:
                self.player.loot -= price
                self.hiddenTurns = 2 
            else:
                print("You don't have enough money, and that makes the bad guys mad.") 
                self.player.takeDamage(CH_ONE_BAD_GUY_STRENGTH)
        else:
            print("You chose not to pay the bribe, and that makes the bad guys mad.")
            self.player.takeDamage(CH_ONE_BAD_GUY_STRENGTH)

    def checkForChapterComplete(self):
        self.complete = self.distanceToShip < 0

    def checkForPlayerKilled(self):
        self.gameOver = self.player.hp < 0

    def handleChoice(self, choice):
        choice = int(choice)
        print(choice)
        options = { 1 : self.sneak,
                    2 : self.run,
                    3 : self.steal,
                    4 : self.bribe
        }
        if choice > 0 and choice < 4:
            options[choice]()
        



