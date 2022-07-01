import cv2
import pytesseract
from translate import Translator


pytesseract.pytesseract.tesseract_cmd = 'D:\\Programming\\Tesseract for textFromphotos\\tesseract.exe'



img = cv2.imread('imgs\img1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=config)
#print(text)

translator = Translator(to_lang="ru")
new=translator.translate(text)
print(new)

cv2.imshow('Result', img)
cv2.waitKey(0)



