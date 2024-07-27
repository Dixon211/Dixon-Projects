import json

class JsonLoader:
    #we init boys
    def __init__(self) -> None:
        #define variables
        self.templatelist = None
        self.data = None
        self.load(r'tools\templater\templates.json')

    #load Json    
    def load(self, filename) -> dict:
        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
                self.templatelist = self.data['templates']
        except FileNotFoundError:
            print(f"{filename} could not be found")
    


   
