import json

class JsonLoader:
    #we init boys
    def __init__(self) -> None:
        #define variables
        self.templatelist = None
        self.data = self.load(r'tools\templater\templates.json')  

    #load Json    
    def load(self, filename) -> dict:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
        except FileNotFoundError:
            print(f"{filename} could not be found")
        return config
    
    def converttemplates(self):
        return 0
   
