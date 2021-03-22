import os

# Helpers - This file contains a helper method used to clear the terminal display.

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
