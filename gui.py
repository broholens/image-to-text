from tkinter import Label, Tk, Frame
from PIL import Image, ImageTk
from convertor import Convertor

width, height = 350, 280

root = Tk()
root.geometry('{}x{}'.format(width, height))
root.resizable(False, False)

global img

def load_image(img_name='tmp.png'):
    img = Image.open(img_name)
    return ImageTk.PhotoImage(img)

def recognize():
    global img
    result = c.extract()
    if result:    
        img = load_image()
        img_label.config(image=img)
        txt_label.config(text=result, bg='red')
    # timer
    root.after(300, recognize)

# bg_frame = Frame(root)
# image = load_image('bg.jpg')
# canvas = Canvas(bg_frame, width=width, height=height)
# canvas.pack(expand=YES)
# canvas.create_image(0, 0, image=image)

# bg_frame.pack()

# weight_frame = Frame(bg_frame)
img_label = Label(root)
img_label.pack(expand=1)
txt_label = Label(root)
txt_label.pack(expand=2)
# Label(weight_frame).pack()
# weight_frame.pack()

root.title('Picture Information Extractor')
root.iconbitmap('pig.ico')
c = Convertor()

root.after(0, recognize)
root.mainloop()
