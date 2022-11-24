from asyncio.windows_events import NULL
from cgitb import text
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import matplotlib.cbook as cbook
import pytesseract as ptsr
import copy
import requests
from pytesseract import Output as otpt
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QImage
from PyQt6.QtGui import QPixmap
import sys
from PyQt6 import QtWidgets, uic
import json 
from UIProcessor import UIProcessor
from Output import Output
from Recognition import Recognition
from Transform import Transform
import keras

ptsr.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#image = Image.open(requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg', stream=True).raw)
image = Image.open('248823.jpg')
#image = image.resize((450,250))
image = np.array(image)

#image = cv2.imread('1.jpg')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("ui.ui", self)

class PicWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("form.ui", self)
    
    def SetPic(self, image):
        recognition = Recognition()
        image = recognition.GetLetters(image)
        #recognition.ExtractLetters(image)
        
        
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        image = cv2.resize(image, [450, 100])
        height, width, a = image.shape
        bytesPerLine = 3 * width
        cvImg = image.copy()
        qImg = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format.Format_BGR888)
        self.picBox.setPixmap(QPixmap(qImg))
        
    def SetText(self, image):
        recognition = Recognition()
        letters = recognition.ExtractLetters(image)
        model_path = 'C:\\Users\\ilyak\\Desktop\\ViolatorRecognition\\emnist_letters.h5'
        model = keras.models.load_model(model_path)
        texts = recognition.GetText(model, letters)
        self.text.setText(texts)

def GetPic():
    output = Output()
    settings = ui.GetCurrentValue()
    gt = Transform()
    #image = gt.Resize(image)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #grayImage = gt.MorphologyTransform(grayImage, settings)
    
    #image = cv2.equalizeHist(image)
    #recognition = Recognition()
    #transformedImage = gt.MorphologyTransform(grayImage, settings)
    #pics = recognition.GetRecognizedPics(grayImage)
    fragments = output.GetFragments(grayImage, pics, settings)
    if len(output.GetFragments(grayImage, pics, settings)) > 0:
        fragments = output.GetFragments(grayImage, pics, settings)[0]
    else:
        fragments = grayImage
    return fragments

def UpdatePic(picWin):
    picture = GetPic()
    picWin.SetPic(picture)
    #picWin.SetText(picture)
    
def Recognize(picWin):
    picture = GetPic()
    picWin.SetText(picture)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
picwindow = PicWindow()

ui = UIProcessor(window)
ui.SetValue()
window.saveButton.clicked.connect(ui.UpdateSetting)
window.recognizeButton.clicked.connect(lambda: Recognize(picwindow))
output = Output()

window.upperThresh.valueChanged.connect(lambda: UpdatePic(picwindow))
window.lowerTheresh.valueChanged.connect(lambda: UpdatePic(picwindow))
window.erode.valueChanged.connect(lambda: UpdatePic(picwindow))
window.dilate.valueChanged.connect(lambda: UpdatePic(picwindow))
window.adaptiveThresholdBlock.valueChanged.connect(lambda: UpdatePic(picwindow))
window.adaptiveThresholdConstant.valueChanged.connect(lambda: UpdatePic(picwindow))
window.medianBulr.valueChanged.connect(lambda: UpdatePic(picwindow))

settings = ui.GetValue()


    

gt = Transform()
#image = gt.Resize(image)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image = cv2.equalizeHist(image)
recognition = Recognition()
#transformedImage = gt.MorphologyTransform(grayImage, settings)
pics = recognition.GetRecognizedPics(grayImage)
fragments = output.GetFragments(grayImage, pics, settings)
texts = recognition.GetTexts(fragments)


#image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
image = output.AddRectangles(image, pics, texts)
output.ShowPic(image)
#input()




picwindow.SetPic(fragments[0])


picwindow.show()
window.show()
app.exec()
