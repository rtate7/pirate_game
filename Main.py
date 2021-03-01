#!/usr/bin/env python3

# Bob Tate
# 2/28/2021

from Player import Player
from Chapter1 import Chapter1
from Helpers import clearScreen 

def getPlayerName():
    print("Welcome to the game")
    name = input ("Please enter your username: ")
    print("Hi " + name + ", let's get started!")
    return name

clearScreen()
player = Player(getPlayerName())
Chapter1(player)
