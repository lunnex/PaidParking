import cv2
import numpy as np

class Transform():
    def GetROI(self, image):
        showCrosshair = True
        fromCenter = False
        rectangle = cv2.selectROI("image", image, showCrosshair, fromCenter)
        (x, y, w, h) = rectangle
        return image[y : y + h, x: x + w]
    
    def MorphologyTransform(self, image, settings):
        copyImage = image.copy()
        if settings['medianBulr'] % 2 == 0:
            settings['medianBulr'] = settings['medianBulr'] + 1
        copyImage = cv2.GaussianBlur(copyImage, (settings['medianBulr'], settings['medianBulr']), cv2.BORDER_CONSTANT)
        copyImage = self.thresholding(copyImage, settings)
        copyImage = self.dilate(copyImage, settings)
        copyImage = self.erode(copyImage, settings)
        #copyImage = cv2.erode(copyImage, np.ones((settings['erode'], settings['erode'])))
        cv2.imshow("0", copyImage)
        return copyImage
        #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
        #return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel) 
    
    def Resize(self, image):
        return cv2.resize(image, [450, 250])
    
    def thresholding(self, image, settings):
        #return cv2.threshold(image, settings['lowerTheresh'], settings['uppreThresh'], cv2.THRESH_BINARY)[1]
        if settings['adaptiveThresholdBlock'] % 2 == 0:
            settings['adaptiveThresholdBlock'] = settings['adaptiveThresholdBlock'] + 1
        return cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,settings['adaptiveThresholdBlock'],settings['adaptiveThresholdConstant'])
    
    def deskew(self, image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated
    
    def dilate(self, image, settings):
        kernel = np.ones((settings['dilate'],settings['dilate']),np.uint8)
        return cv2.dilate(image, kernel, iterations = 1)
    
    def erode(self, image, settings):
        kernel = np.ones((settings['erode'],settings['erode']),np.uint8)
        return cv2.erode(image, kernel, iterations = 1)

    def opening(self, image):
        kernel = np.ones((9,9),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

