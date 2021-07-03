import os
import json

class Staples:
    def __init__(self):
        self.data = self.load()

    def load(self):
        with open("grocree/staples.json", "r") as read_file:
            return sorted(json.load(read_file))
    
    def dump(self):
        with open("grocree/staples.json", "w") as write_file:
            json.dump(self.data, write_file)

    def list(self):
        while True:
            os.system("clear")
            
            print('STAPLES')
            print('_________')
            print('')
            
            for index, staple in enumerate(self.data):
                print(str(index + 1) + " - " + staple)
            
            print('')

            add_del_back = input('~ ')

            if add_del_back == 'back':
                break
            elif add_del_back[0:3] == 'del':
                self.data.pop(int(add_del_back[4]) - 1)
            elif add_del_back not in self.data:
                self.data.append(add_del_back)
        


        
