from tools.Videoeditor.DixonVE import DixonVE
from tools.jsonload import JsonLoader
from tools.framecontrol import FrameController

#x = DixonVE()
#print(x.templates)


fc = FrameController()
jl = JsonLoader()
while fc.check is True:
    fc.readframe()
    #fc.setobject(jl.templatelist)
    #fc.show()

#print(jl.data)q