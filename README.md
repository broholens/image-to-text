# image-to-text
通过百度文字识别API，将图片转为可复制的文字。目前支持手机号和邮箱地址的转换。

邮箱地址的转换支持如下:
- 126.com
- qq.com
- 163.com
- gmail.com
- sina.com
- hotmail.com
- outlook.com
- sina.cn
- live.com
- sohu.com
- foxmail.com
- icloud.com
- 139.com

## 

## 使用方法(windows)

1. **[下载压缩包](https://pan.baidu.com/s/1bQ8rKa4OFRNTytTAlAzkZw) 并解压。(提取码：6a57)**

2. **运行img2text.exe(建议添加快捷方式到桌面)**

3. **截取需要被识别的区域图片:**

   - example 1:

     ![image](https://github.com/broholens/images/blob/master/image_to_text_1.jpg)

   - example 2:

     ![image](https://github.com/broholens/images/blob/master/image_to_text_2.jpg)

   - example 3:

     ![image](https://github.com/broholens/images/blob/master/image_to_text_3.jpg)

4. **查看应用(可选步骤，只是用来人工确认识别结果)**

   ![image](https://github.com/broholens/images/blob/master/image_to_text_5.jpg)

5. **转换的结果已经自动复制在粘贴板上了，可以直接粘贴**

## 

## 注意:
- **如果粘贴板上没有可粘贴的内容，请尝试改变截图大小.可按住Ctrl滚动鼠标滚轮调整大小**
- **如果发生意想不到的错误，请重新运行img2text.exe**

*enjoy :)*

## 

## TODO

- **一个百度云账号，多个人同时使用会出错**
- 国外手机号,如0085297930264
- ~~live.com~~
- ~~139.com~~
- ~~sohu.com~~
- ~~icloud.com~~
- ~~foxmail.com~~
- 邮箱中的字符识别
- ~~邮箱和手机号分割包含其他字符,如“;”~~
- 邮箱识别不准确,需要训练模型
- aliyun.com
- yeah.net



## 开发小记

1. pyinstaller打包出现问题，切换python版本为3.5后ok

2. 开始想把剪切板上的DibImageFile直接返回，后来发现不行，只能存为临时文件tmp.png

3. API识别结果后，使用fuzzywuzzy来进行后缀更正，qq.com被错误识别为gmail.com，最后通过判断@的后缀字符数来进行校正

4. pyperclip 只能复制text到粘贴板

5. GUI开发时，轮询剪切板上有没有内容`root.after(300, recognize)`，在开始mainloop前，需要加上`root.after(0, recognize)`
6. 设置window大小300x200，中间是小x
