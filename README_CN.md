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


# 使用方法(windows)

#### [下载](https://github.com/broholens/image-to-text/raw/master/extractor.zip) 压缩包并解压。

#### 运行gui.exe
![image](https://github.com/broholens/images/blob/master/image_to_text_4.jpg)

#### 截取需要被识别的区域图片:

- example 1:

![image](https://github.com/broholens/images/blob/master/image_to_text_1.jpg)

- example 2:

![image](https://github.com/broholens/images/blob/master/image_to_text_2.jpg)

- example 3:

![image](https://github.com/broholens/images/blob/master/image_to_text_3.jpg)

#### 查看应用(非必须步骤，只是用来人工确认识别结果):
![image](https://github.com/broholens/images/blob/master/image_to_text_5.jpg)

#### 转换的结果已经自动复制在粘贴板上了，可以直接粘贴

## 注意:
- **如果粘贴板上没有可粘贴的内容，请尝试改变截图大小**
- **如果发生意想不到的错误，请重新运行gui.exe**

*enjoy :)*

## TODO

- 国外手机号,如0085297930264
- live.com
- 139.com
- sohu.com
- icloud.com
- foxmail.com
- 邮箱小写
- 邮箱中的字符识别
- 邮箱和手机号分割包含其他字符,如“;”
- 邮箱识别不准确,需要训练模型
