#!/usr/bin/env python3
import random
from Constants import *

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = STARTING_HP
        self.loot = 0
        self.booty = 0
        self.stealth = 10
        self.shipAttack = STARTING_SHIP_ATTACK
        self.shipArmor = STARTING_SHIP_ARMOR

    def takeDamage(self, damage):
        damage *= random.randint(1, 6)
        damage -= (random.randint(1, 6) * self.shipArmor)
        if damage < 0:
            damage = 0
        print("You've taken " + str(damage) + " points of damage.")
        self.hp -= damage
        if self.hp > 0:
            print("You have " + str(self.hp) + " hit points remaining.")

    def takeBoardingDamage(self, damage):
        self.hp -= damage 
        print("You take " + str(damage) + " points of damage while boarding.")
        if self.hp > 0:
            print("You have " + str(self.hp) + " hit points remaining.")

    def plunder(self, multiplier):
        plunderedBooty = multiplier * random.randint(1, 6)
        self.booty += plunderedBooty
        print("You've plundered booty worth " + str(plunderedBooty) + " gold pieces.")

    def reset(self):
        self.hp = STARTING_HP
        self.loot = 0
        self.booty = 0
        self.stealth = 10
        self.shipAttack = STARTING_SHIP_ATTACK