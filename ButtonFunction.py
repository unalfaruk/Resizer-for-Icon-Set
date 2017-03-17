from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

root= Tk()
root.title("Faruk")

def showImage(filename):
    print(filename)
    image = Image.open(filename)
    print(type(image))
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image=photo


def printName():
    print("Selam")

def chooseAFile():
    filename = askopenfilename()
    showImage(filename)


frameImage= Frame(root)
frameButtons = Frame(root)

buttonBrowse = Button(frameButtons, text="Browse", command=chooseAFile)
buttonBrowse.grid(row=0,column=0,padx=5,pady=5)

buttonConvert= Button(frameButtons, text="Convert", command=printName)
buttonConvert.grid(row=0,column=1,padx=5, pady=5)

image=PhotoImage()
label=Label(frameImage,image=None)
label.grid(row=0,column=0)

frameImage.pack(side=TOP,fill=X)
frameButtons.pack(side=BOTTOM)
#frame.grid(row=0,column=1)

root.mainloop()
