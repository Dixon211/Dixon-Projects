import json

#tool to get Json Data
# returns json class object, can use 
def getjsondata(filename):
    try:
         with open(filename, 'r') as file:
            config = json.load(file)
            
    except FileNotFoundError:
        print(f"{filename} could not be found")
        return(False)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the configuration file {filename}.")
        return (False)
    
    return config