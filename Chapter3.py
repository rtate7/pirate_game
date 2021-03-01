from Helpers import clearScreen 
import random
from Constants import *
from Chapter4 import Chapter4

class Chapter3:
    choices = [
        "Sail through the storm",
        "Go the long way"
    ]

    gameOver = False

    def __init__(self, player):
        self.player = player
        self.startChapter()

    def startChapter(self):
        print("You've survived the battle and it's time to fix up the ship. There's a storm between you and your home port.")
        self.presentChoices()
        self.handleChoice(self.getChoice())
        Chapter4(self.player)

    def presentChoices(self):
        print("\nYou've got to decide whether to sail through the storm or to go the long way around the storm to get to port.")
        for i in range(0, 2):
            print(str(i + 1) + " - " + self.choices[i])

    def getChoice(self):
        return input("\nWhich do you choose? (1 - 2) ")

    def direct(self):
        print("You chose to sail through the storm")
        stormDamage = random.randint(1, 6) * STORM_STRENGTH
        self.player.hp -= stormDamage
        print("\nYou took " + str(stormDamage) + " points of damage while sailing through the storm.")
        self.checkForPlayerKilled()

    def longWay(self):
        print("You chose to go around the storm")
        wagesPaid = random.randint(1, 6) * CREW_THIRST
        if self.player.loot < wagesPaid:
            wagesPaid = self.player.loot
       
        self.player.loot -= wagesPaid

        print("You spent " + str(wagesPaid) + " gold pieces for the crew's wages while taking the long way home.")

    def checkForPlayerKilled(self):
        self.gameOver = self.player.hp < 0

    def handleChoice(self, choice):
        choice = int(choice)
        print(choice)
        options = { 1 : self.direct,
                    2 : self.longWay
          }
        if choice > 0 and choice < 2:
            options[choice]()
        