from tools.framecontrol import FrameController as fc
from tools.jsonloader import getjsondata

class DixonVE:
    def __init__(self):
        self.jsonconfig = getjsondata(r'tools\templater\templates.json')
        self.templates = self.jsonconfig['templates']
        self.fc = fc()
        self.fc.readframe()
        

