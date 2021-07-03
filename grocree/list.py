import os

from grocree.staples import Staples
from grocree.recipes import Recipes
from grocree.todoist import Todoist

class List:
    def __init__(self):
        self.staples = Staples()
        self.recipes = Recipes()
        self.todoist = Todoist()
        self.list = {
            "staples": "N",
            "recipes": [],
            "singles": []
        }

    def menu(self):
        while True:
            os.system("clear")
            
            print('LIST')
            print('_________')
            print('')

            print('Staples: ' + self.list['staples'])
            print('')

            print('Recipes:')
            for recipe in self.list['recipes']:
                print(recipe['name'])

            print('Singles:')
            for single in self.singles:
                print(single)

            

            list_del_back = input('~ ')

            if list_del_back == 'back':
                break
            elif list_del_back[0:3] == 'del':
                self.data.pop(int(list_del_back[4]) - 1)
            elif list_del_back[0:3] == 'add':
                self.data.append({'name':list_del_back[4:], 'ingredients':[]})
            elif self.data[int(list_del_back) - 1]:
                self.list(int(list_del_back) - 1)


    