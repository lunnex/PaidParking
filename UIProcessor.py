import json

class UIProcessor:
    def __init__(self, window):
        self.window = window
        
    def UpdateSetting(self):
        settings = {
            "upperThresh": self.window.upperThresh.value(),
            "lowerTheresh": self.window.lowerTheresh.value(),
            "erode": self.window.erode.value(),
            "dilate": self.window.dilate.value(),
            "medianBulr": self.window.medianBulr.value(),  
            "adaptiveThresholdBlock": self.window.adaptiveThresholdBlock.value(),
            "adaptiveThresholdConstant": self.window.adaptiveThresholdConstant.value()  
        }
        
        with open('config.json', 'w') as outfile:
            json.dump(settings, outfile)
    
    def SetValue(self):
        with open('config.json') as infile:
            settings = infile.read()
            templates = json.loads(settings)
            self.window.upperThresh.setValue(templates['upperThresh'])
            self.window.lowerTheresh.setValue(templates['lowerTheresh'])
            self.window.erode.setValue(templates['erode'])
            self.window.dilate.setValue(templates['dilate'])
            self.window.medianBulr.setValue(templates['medianBulr'])
            self.window.adaptiveThresholdBlock.setValue(templates['adaptiveThresholdBlock'])
            self.window.adaptiveThresholdConstant.setValue(templates['adaptiveThresholdConstant'])
            
    def GetValue(self):
        with open('config.json') as infile:
            settings = infile.read()
            return json.loads(settings)
        
    def GetCurrentValue(self):
        return {
            "upperThresh": self.window.upperThresh.value(),
            "lowerTheresh": self.window.lowerTheresh.value(),
            "erode": self.window.erode.value(),
            "dilate": self.window.dilate.value(),
            "medianBulr": self.window.medianBulr.value(),
            "adaptiveThresholdBlock": self.window.adaptiveThresholdBlock.value(),
            "adaptiveThresholdConstant": self.window.adaptiveThresholdConstant.value()  
        }
