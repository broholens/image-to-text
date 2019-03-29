import re
import os
import time
from tkinter import Tk, PhotoImage, Label, Button
import pyperclip  # support plain text only 
from aip import AipOcr  # pip install baidu-aip
from fuzzywuzzy import process  # string matching
from PIL import ImageGrab  # grab image from clipboard
from PIL.BmpImagePlugin import DibImageFile



class Convertor:

    APP_ID = '11565085'
    API_KEY = 'dh9pPBqw1H4hQQyPrk4HHVv6'
    SECRET_KEY = '6mjlcxPsT2NRs7wETIqs3xYBjz0pdyH5'
    choices = ['qq.com', '126.com', '163.com', 'gmail.com', 'outlook.com', 'hotmail.com']
    phone_ptn = re.compile('\d{11}')

    def __init__(self):
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        # phone pattern
        self.previous_filename = 'tmp.png'
        self.filename = 'tmp.png'
        self.image = ''

    def load_image(self):
        with open(self.filename, 'rb')as f:
            return f.read()

    def save_clipboard_img(self):
        # save image grabbed from clipboard to templete file.
        image = ImageGrab.grabclipboard()
        if image == self.image:
            return False
        if isinstance(image, DibImageFile):
            if os.path.exists(self.filename):
                os.remove(self.filename)
            self.filename = str(time.time()*1000) + '.png'
            image.save(self.filename)
            return True
        return False

    def extract(self):
        # save and load
        is_image_saved = self.save_clipboard_img()
        if is_image_saved is False:
            return
        image = self.load_image()
        # recongize image
        result = self.client.basicGeneral(image)
        words = result['words_result'][0]['words']
        if '@' in words:
            return self.extract_mail(words)
        return self.extract_phone(words)


    def extract_mail(self, words):
        # split string by @
        word, suffix = words.split('@')
        if ':' in word:
            word = word.split(':')[-1]
        words = word + '@' + process.extractOne(suffix, self.choices)[0]
        # set clipboard
        pyperclip.copy(words)
        return words

    def extract_phone(self, words):
        # match phone number
        phone = self.phone_ptn.findall(words)
        print(phone)
        if phone:
            # set to clipboard
            pyperclip.copy(phone[0])
            return phone[0]
        return 'Phone number not found!'


# class ConvertorGUI(Tk):
#     def __init__(self, *args, **kwargs):
#         super(ConvertorGUI, self).__init__()
# def config_label():
#     pass

root = Tk()
convertor = Convertor()
label = Label()
label.pack()
result = convertor.extract()
print(result)
# while 1:
#     result = convertor.extract()
#     if not result:
#         time.sleep(1)
#         continue
#     label.config(text=result, image=PhotoImage(convertor.filename), compound='top')

root.mainloop()

