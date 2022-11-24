import cv2
import numpy as np
import pytesseract as ptsr
from Output import Output
from Transform import Transform
from pytesseract import Output as otpt
from collections import Counter


class Recognition():
    def GetRecognizedPics(self, image):
        classifier = cv2.CascadeClassifier('haar3.xml')
        return classifier.detectMultiScale(image)
    
    def GetMaxFrequencyValue(self, hierarchy):
        allValues = []
        for item in hierarchy:
            allValues.append(item[3])
        c = Counter(allValues)
        
        try:
            return c.most_common(1)[0][0]
        except:
            return -1
    
    def GetMaxArea(self, hierarchy):
        firstMax = 0
        secondMax = 0
        firstMax = self.GetMaxFrequencyValue(list(filter(lambda x: x[3] > 0, hierarchy[0])));
        #secondMax = self.GetMaxFrequencyValue(list(filter(lambda x: firstMax > x[3] and x[3] > 0, hierarchy[0])));
        
        return (firstMax, secondMax)
    
    def GetLetters(self, pic):
        contours, hierarchy = cv2.findContours(pic, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
        output = pic.copy()
        firstMax, secondMax = self.GetMaxArea(hierarchy)
        
        for idx, contour in enumerate(contours):
            (x, y, w, h) = cv2.boundingRect(contour)
            if ((hierarchy[0][idx][3] == firstMax or hierarchy[0][idx][3] == secondMax) and cv2.contourArea(contour) > 30):
                cv2.rectangle(output, (x, y), (x + w, y + h), (70, 0, 0), 1)
        return output
    
    def ExtractLetters(self, pic):
        contours, hierarchy = cv2.findContours(pic, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
        output = pic.copy()
        firstMax, secondMax = self.GetMaxArea(hierarchy)
        letters = []
        
        for idx, contour in enumerate(contours):
            (x, y, w, h) = cv2.boundingRect(contour)
            if ((hierarchy[0][idx][3] == firstMax or hierarchy[0][idx][3] == secondMax) and cv2.contourArea(contour) > 30):
                cv2.rectangle(output, (x, y), (x + w, y + h), (70, 0, 0), 1)
                letter_crop = pic[y:y + h, x:x + w]
            # print(letter_crop.shape)

            # Resize letter canvas to square
                size_max = max(w, h)
                letter_square = 255 * np.ones(shape=[size_max, size_max], dtype=np.uint8)
                if w > h:
                    # Enlarge image top-bottom
                    # ------
                    # ======
                    # ------
                    y_pos = size_max//2 - h//2
                    letter_square[y_pos:y_pos + h, 0:w] = letter_crop
                elif w < h:
                    # Enlarge image left-right
                    # --||--
                    x_pos = size_max//2 - w//2
                    letter_square[0:h, x_pos:x_pos + w] = letter_crop
                else:
                    letter_square = letter_crop

                # Resize letter to 28x28 and add letter and its X-coordinate
                letters.append((x, w, cv2.resize(letter_square, (28, 28), interpolation=cv2.INTER_AREA)))
            letters.sort(key=lambda x: x[0], reverse=False)

        # cv2.imshow("Input", img)
        # # cv2.imshow("Gray", thresh)
        # cv2.imshow("Enlarged", img_erode)
        # cv2.imshow("Output", output)
        #cv2.imshow("0", letters[0][2])
        #cv2.imshow("1", letters[1][2])
        #cv2.imshow("2", letters[2][2])
        #cv2.imshow("3", letters[3][2])
        #cv2.imshow("4", letters[4][2])
        #cv2.waitKey(0)
        return letters
    
    def GetText(self, model, letters):
        text = ""
        for i in range(len(letters)):
            dn = letters[i+1][0] - letters[i][0] - letters[i][1] if i < len(letters) - 1 else 0
            text += self.TextPrediction(model, letters[i][2])
            if (dn > letters[i][1]/4):
                text += ' '
        return text
    
    def TextPrediction(self, model, img):
        emnist_labels = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
        img_arr = np.expand_dims(img, axis=0)
        img_arr = 1 - img_arr/255.0
        img_arr[0] = np.rot90(img_arr[0], 3)
        img_arr[0] = np.fliplr(img_arr[0])
        img_arr = img_arr.reshape((1, 28, 28, 1))

        predict = model.predict([img_arr])
        result = np.argmax(predict, axis=1)
        return chr(emnist_labels[result[0]])
    
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