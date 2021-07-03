import os
from grocree.staples import Staples
from grocree.recipes import Recipes

class Menu:
    def __init__(self):
        self.staples = Staples()
        self.recipes = Recipes()

    def run(self):
        while True:
            os.system('clear')

            print('MAIN MENU')
            print('_________')
            print('')
            print('1 - staples')
            print('2 - recipes')
            print('')

            choice = input('~ ')

            if choice == "1":
                self.staples.list()

            if choice == "2":
                self.recipes.menu()
