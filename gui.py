from tkinter import Label, Tk, Canvas

from PIL import Image, ImageTk

from convertor import Convertor

width, height = 350, 280

root = Tk()
root.geometry('{}x{}'.format(width, height))
root.resizable(False, False)
root.config(bg='#FFC1C1')

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
        txt_label.config(text=result, fg='black', font=("Arial", 14))
    # timer
    root.after(300, recognize)

img_label = Label(root, borderwidth=0)
img_label.pack(expand=1)
canvas = Canvas(root, width=width, height=0, borderwidth=0)
canvas.create_line(0, height/2, width, height/2)
canvas.pack()
txt_label = Label(root, borderwidth=0)
txt_label.pack(expand=2)

root.title('Picture Information Extractor')
root.iconbitmap('pig.ico')
c = Convertor()

root.after(0, recognize)
root.mainloop()
