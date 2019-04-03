import re
import time
from datetime import datetime
import pyperclip  # support plain text only 
from aip import AipOcr  # pip install baidu-aip
from fuzzywuzzy import process  # string matching
from PIL import ImageGrab  # grab image from clipboard
from PIL.BmpImagePlugin import DibImageFile


class Convertor:

    APP_ID = '11565085'
    API_KEY = 'dh9pPBqw1H4hQQyPrk4HHVv6'
    SECRET_KEY = '6mjlcxPsT2NRs7wETIqs3xYBjz0pdyH5'
    # email suffix
    choices = ['qq.com', '126.com', '163.com', 'gmail.com', 'outlook.com', 'hotmail.com', 'sina.com']
    # phone pattern
    phone_ptn = re.compile('\d{11}')

    def __init__(self):
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.filename = 'tmp.png'
        self.image = None

    def load_image(self):
        with open(self.filename, 'rb')as f:
            return f.read()

    def save_clipboard_img(self):
        # save image grabbed from clipboard to templete file.
        while 1:
            try:
                image = ImageGrab.grabclipboard()
                break
            except:
                # wait for screenshoot
                time.sleep(1)
        # 粘贴板内容跟上次的内容是否相同
        if image == self.image:
            return False
        self.image = image
        # 判断是否为截图类型
        if isinstance(image, DibImageFile):
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
        # @ 可能解析为 (
        words = words.replace('(', '@')
        # 联系电话: **********
        if ':' in words:
            words = words.split(':')[-1]
        # 通过@来判断使用哪个方法
        if '@' in words:
            return self.extract_mail(words)
        return self.extract_phone(words)


    def extract_mail(self, words):
        # split string by @
        try:
            word, suffix = words.split('@')
        except:
            return
        # 选择最匹配的邮箱
        # TODO: qq错误匹配为gmail
        words = word.strip() + '@' + process.extractOne(suffix, self.choices)[0]
        # set clipboard
        pyperclip.copy(words)
        return words

    def extract_phone(self, words):
        words = words.split('已验证')[0]
        # 转接
        if '转' in words:
            a, b = words.split('转')
            words = '-'.join([a, b])
            # 复制到粘贴板
            pyperclip.copy(words)
            return words
        # 手机号
        words = self.phone_ptn.findall(words)
        if not words:
            return 
        words = words[0]
        pyperclip.copy(words)
        return words
        


# if __name__ == '__main__':
#     c = Convertor()
#     while 1:
#         result = c.extract()
#         if result:
#             print(datetime.now(), '----', result)