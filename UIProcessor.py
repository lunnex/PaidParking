import json

class UIProcessor:
    def __init__(self, window):
        self.window = window
        
    def UpdateSetting(self):
        settings = {
            "uppreThresh": self.window.uppreThresh.value(),
            "lowerTheresh": self.window.lowerTheresh.value(),
            "erode": self.window.erode.value(),
            "dilate": self.window.dilate.value(),
            "medianBulr": self.window.medianBulr.value()  
        }
        
        with open('config.json', 'w') as outfile:
            json.dump(settings, outfile)
    
    def SetValue(self):
        with open('config.json') as infile:
            settings = infile.read()
            templates = json.loads(settings)
            self.window.uppreThresh.setValue(templates['uppreThresh'])
            self.window.lowerTheresh.setValue(templates['lowerTheresh'])
            self.window.erode.setValue(templates['erode'])
            self.window.dilate.setValue(templates['dilate'])
            self.window.medianBulr.setValue(templates['medianBulr'])
            
    def GetValue(self):
        with open('config.json') as infile:
            settings = infile.read()
            return json.loads(settings)
        
    def GetCurrentValue(self):
        return {
            "uppreThresh": self.window.uppreThresh.value(),
            "lowerTheresh": self.window.lowerTheresh.value(),
            "erode": self.window.erode.value(),
            "dilate": self.window.dilate.value(),
            "medianBulr": self.window.medianBulr.value()  
        }
