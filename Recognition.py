import cv2
import pytesseract as ptsr
from Output import Output
from Transform import Transform
from pytesseract import Output as otpt

class Recognition():
    def GetRecognizedPics(self, image):
        classifier = cv2.CascadeClassifier('haar3.xml')
        return classifier.detectMultiScale(image)
    
    def GetTexts(self, fragments):
        texts = []
        output = Output()
        transform = Transform()
        for fragment in fragments: 
            #gray = cv2.cvtColor(fragment,cv2.COLOR_BGR2GRAY)
            #threshold = cv2.resize(fragment, [1280, 720])
            #threshold = cv2.threshold(threshold, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            
            #threshold = cv2.Canny(threshold, 100, 200)
            #threshold = cv2.Canny(threshold, 100, 200)
            #threshold = transform.dilate(threshold)
            #threshold = transform.thresholding(threshold)
            
            #threshold = transform.erode(threshold)
            #threshold = transform.opening(threshold)
            #threshold = transform.MorphologyTransform(threshold)
            
            #threshold = transform.deskew(threshold)
            #threshold = cv2.medianBlur(threshold,25)
            #output.ShowPic(threshold)
            custom_config = r'--oem 3 --psm 6'
            
            texts.append(ptsr.image_to_data(fragment, output_type=otpt.DICT, config=custom_config, lang='eng'))
            #texts.append(ptsr.image_to_string(threshold))
        return texts
    
    def GetLetters(self, pic):
        contours, hierarchy = cv2.findContours(pic, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        output = pic.copy()
        for idx, contour in enumerate(contours):
            (x, y, w, h) = cv2.boundingRect(contour)
            # print("R", idx, x, y, w, h, cv2.contourArea(contour), hierarchy[0][idx])
            # hierarchy[i][0]: the index of the next contour of the same level
            # hierarchy[i][1]: the index of the previous contour of the same level
            # hierarchy[i][2]: the index of the first child
            # hierarchy[i][3]: the index of the parent
            if hierarchy[0][idx][2] == -1:
                cv2.rectangle(output, (x, y), (x + w, y + h), (70, 0, 0), 1)
        return output