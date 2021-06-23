import json
import os
from .utils import parse_command


class Staples:
    def __init__(self):
        self.data = self.load()

    def load(self):
        with open("grocree/staples.json", "r") as staples_file:
            staples = json.load(staples_file)
            return sorted(staples, key=lambda staple: staple.get("item"))

    def dump(self):

        with open("grocree/staples.json", "w") as staples_file:
            json.dump(self.data, staples_file)

    def menu(self):
        os.system("clear")

        print("Staples")
        print("=======")
        print("")

        for index, staple in enumerate(self.data):
            print(f"{index + 1} - {staple['item']} ({staple['amount']})")

        print("")

        self.command()

    def command(self):
        user_input = input("~ ").lower()
        command = parse_command(user_input)

        if command == "del":
            self.delete(user_input[4:].split(" "))
        elif command == "add":
            self.add(user_input)
        elif command == "menu":
            pass

    def delete(self, items):
        for item in items:
            self.data.pop(int(item) - 1)
        self.dump()
        self.menu()

    def add(self, item):
        amount = input().lower()
        self.data.append({"item": item, "amount": amount})
        self.dump()
        self.menu()
