import cv2
import pytesseract
from translate import Translator

pytesseract.pytesseract.tesseract_cmd = 'D:\\Programming\\Tesseract for textFromphotos\\tesseract.exe'


def get_text(img_src):
    img = cv2.imread(img_src)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=config)
    if len(text) > 500:
        return "-E-"
    # print(text)
    #cv2.imshow('Result', img)
    #cv2.waitKey(0)
    return text


def translate(text):
    if text == "-E-":
        return "Chars > 500"
    translator = Translator(to_lang="ru")
    translated_text = translator.translate(text)
    #print(translated_text)
    return translated_text
