import os
from grocree.staples import Staples


class Nav:
    def __init__(self):
        self.staples = Staples()

    def menu(self):
        os.system("clear")

        print("Main Menue")
        print("=======")
        print("")

        print("1 - staples")
        print("2 - recipes")
        print("3 - lists")

        choice = input()

        if choice == "1":
            self.staples.menu()
