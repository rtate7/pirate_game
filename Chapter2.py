# Bob Tate
# 2/28/2021

# Chapter 2 - This file contains the story elements for the second chapter of the game.

from Helpers import clearScreen 
import random
from Constants import *
from Chapter3 import Chapter3

class Chapter2:
    choices = [
        "Fire - Fire the cannons!",
        "Brace - Prepare to defend against an attack.",
        "Run Away - Get out of combat",
        "Plunder - Attempt to board the enemy ship"
    ]
    complete = False
    gameOver = False
    enemyHp = CH_TWO_ENEMY_STARTING_HP

    def __init__(self, player):
        self.player = player
        self.startChapter()

    def startChapter(self):
        print("You’ve gotten away with the ship and your life! A small merchant vessel has fallen into your path. Time to plunder!")
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
            Chapter3(self.player)

    def fire(self):
        print("You chose Fire")
        attack = random.randint(1, 6) * self.player.shipAttack
        self.enemyHp -= attack
        print("\nYou did " + str(attack) + " points of damage to the ship.")
        print("Your enemy returns fire!")
        self.player.takeDamage(CH_TWO_BAD_GUY_STRENGTH)

    def brace(self):
        print("You chose Brace")
        self.player.shipArmor += 5
        print("Enemy firing!")
        self.player.takeDamage(CH_TWO_BAD_GUY_STRENGTH)

    def runAway(self):
        print("You chose Run Away")
        print("Enemy firing!")
        player.takeDamage(CH_TWO_BAD_GUY_STRENGTH)
        self.complete = true

    def plunder(self):
        print("You chose Plunder")
        print("Boarding the enemy vessel!")
        self.player.takeBoardingDamage(self.enemyHp)
        self.player.plunder(CH_TWO_PLUNDER_MULTIPLIER)

    def checkForChapterComplete(self):
        self.complete = self.enemyHp <= 0

    def checkForPlayerKilled(self):
        self.gameOver = self.player.hp <= 0

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
        