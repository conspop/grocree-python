import os
import json

class Recipes:
    def __init__(self):
        self.data = self.load()

    def load(self):
        with open("grocree/recipes.json", "r") as read_file:
            return sorted(json.load(read_file), key=lambda recipe: recipe.get("name"))
    
    def dump(self):
        with open("grocree/recipes.json", "w") as write_file:
            json.dump(self.data, write_file)

    def menu(self):
        while True:
            os.system("clear")
            
            print('RECIPES')
            print('_________')
            print('')
            
            for index, recipe in enumerate(self.data):
                print(str(index + 1) + " - " + recipe['name'])
            
            print('')

            list_del_back = input('~ ')

            if list_del_back == 'back':
                break
            elif list_del_back[0:3] == 'del':
                self.data.pop(int(list_del_back[4]) - 1)
            elif list_del_back[0:3] == 'add':
                self.data.append({'name':list_del_back[4:], 'ingredients':[]})
            elif self.data[int(list_del_back) - 1]:
                self.list(int(list_del_back) - 1)

    def list(self, recipe):
        while True:
            os.system("clear")
            
            print(self.data[recipe]['name'].upper())
            print('_________')
            print('')
            
            for index, ingredient in enumerate(self.data[recipe]['ingredients']):
                print(str(index + 1) + " - " + ingredient)
            
            print('')

            add_del_back = input('~ ')

            if add_del_back == 'back':
                break
            elif add_del_back[0:3] == 'del':
                self.data[recipe]['ingredients'].pop(int(add_del_back[4]) - 1)
            elif add_del_back not in self.data[recipe]['ingredients']:
                self.data[recipe]['ingredients'].append(add_del_back)


        

                
        


        
