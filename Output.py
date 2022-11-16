import cv2
from Transform import Transform

class Output():   
    def ShowPic(self, image):
        #plt.imshow(image)
        cv2.imshow('Output',image)
        
        
    def AddRectangles(self, image, rectangles, texts):
        copyImage = image.copy()
        for i in range(0, len(rectangles)):
            if (len(texts[i]) > 0 and len(texts[i]) < 8):
                copyImage = cv2.rectangle(copyImage, (rectangles[i][0], rectangles[i][1]), (rectangles[i][0] + rectangles[i][2], rectangles[i][1] + rectangles[i][3]), (255, 0, 0), 3)
            elif (len(texts[i]) >= 8 and len(texts[i]) <= 9):
                copyImage = cv2.rectangle(copyImage, (rectangles[i][0], rectangles[i][1]), (rectangles[i][0] + rectangles[i][2], rectangles[i][1] + rectangles[i][3]), (0, 255, 0), 3)
        return copyImage
    
    def Cadr(self, image, rectangle):
        return image[rectangle[1] : rectangle[1] + rectangle[3], rectangle[0]: rectangle[0] + rectangle[2]]
    
    def GetFragments(self, image, rectangles, settings):
        fragments = []
        transform = Transform()
        for rectangle in rectangles:
            fragments.append(transform.MorphologyTransform(self.Cadr(image, rectangle), settings))
        return fragments