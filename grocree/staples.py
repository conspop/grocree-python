import json
import os
from .utils import parse_command


class Staples:
    def __init__(self):
        self.staples = self.load()

    def load(self):
        with open("grocree/staples.json", "r") as staples_file:
            staples = json.load(staples_file)
            return staples.sort(key=lambda staple: staple.get("item"))

    def dump(self):

        with open("grocree/staples.json", "w") as staples_file:
            json.dump(self.staples, staples_file)

    def menu(self):
        os.system("clear")

        print("Staples")
        print("=======")
        print("")

        for index, staple in enumerate(self.staples):
            print(f"{index + 1} - {staple['item']} ({staple['amount']})")

        print("")

        self.command()

    def command(self):
        user_input = input().lower()
        command = parse_command(user_input)

        if command == "del":
            self.delete(user_input[4:].split(" "))
        else:
            self.add(user_input)

    def delete(self, items):
        for item in items:
            self.staples.pop(int(item) - 1)
        self.dump()
        self.menu()

    def add(self, item):
        amount = input().lower()
        self.staples.append({"item": item, "amount": amount})
        self.dump()
        self.menu()
