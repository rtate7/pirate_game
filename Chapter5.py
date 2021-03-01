from Helpers import clearScreen 
import random
from Constants import *

class Chapter5:
    choices = [
        "Fire - Fire the cannons!",
        "Brace - Prepare to defend against an attack.",
        "Run Away - Get out of combat",
        "Plunder - Attempt to board the enemy ship"
    ]
    complete = False
    gameOver = False
    enemyHp = CH_FIVE_ENEMY_STARTING_HP

    def __init__(self, player):
        self.player = player
        self.startChapter()

    def startChapter(self):
        print("You went looking for trouble and you found it. You've spotted a military vessel up ahead. Time for battle!")
        self.chapterLoop()

    def presentChoices(self):
        print("\nYou've got some choices to make. You've got " + str(self.player.hp) + " HP and your enemy has " + str(self.enemyHp) + " HP. You can:")
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
            self.player.shipArmor -= 1

        if self.gameOver:
            print("Thanks for playing, but you've been killed.")
            playAgain = input("Want to play again? (Y/N)")
            if playAgain == 'Y' or playAgain == 'y':
                self.player.reset()
                Chapter1(self.player)
        elif self.complete:
            Chapter4(self.player)

    def fire(self):
        print("You chose Fire")
        attack = random.randint(1, 6) * self.player.shipAttack
        self.enemyHp -= attack
        print("\nYou did " + str(attack) + " points of damage to the ship.")
        print("Your enemy returns fire!")
        self.player.takeDamage(CH_FIVE_BAD_GUY_STRENGTH)

    def brace(self):
        print("You chose Brace")
        self.defense += 5
        print("Enemy firing!")
        player.takeDamage(CH_FIVE_BAD_GUY_STRENGTH)

    def runAway(self):
        print("You chose Run Away")
        print("Enemy firing!")
        player.takeDamage(CH_FIVE_BAD_GUY_STRENGTH)
        self.complete = true

    def plunder(self):
        print("You chose Plunder")
        print("Boarding the enemy vessel!")
        player.takeBoardingDamage(self.enemyHp)
        player.plunder(CH_FIVE_PLUNDER_MULTIPLIER)

    def checkForChapterComplete(self):
        self.complete = self.enemyHp <= 0

    def checkForPlayerKilled(self):
        self.gameOver = self.player.hp < 0

    def handleChoice(self, choice):
        choice = int(choice)
        print(choice)
        options = { 1 : self.fire,
                    2 : self.brace,
                    3 : self.runAway,
                    4 : self.plunder
        }
        if choice > 0 and choice < 4:
            options[choice]()
        