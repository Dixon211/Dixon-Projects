#speed checking tool
class Speedcheck:
    def __init__(self):
        try:
            import datetime
            import time
            self.datetime = datetime
            self.time = time
        except:
            print('SpeedCheck could not run, please import datetime with command:\n    import datetime')
        self.recordedtime = None
        self.on = False

    def record(self):
        self.recordedtime = self.datetime.datetime.now()
        return None

    def timecheck(self):
        if self.time == None:
            return(f"Time was not recorded, call <ClassObject>.record() first\n\n")
        else:
            differential = self.datetime.datetime.now()-self.recordedtime
            return(f'Speed: {differential}')
        
    def toggle(self):
        if self.on == True:
            self.on = False
        else:
            self.on = True