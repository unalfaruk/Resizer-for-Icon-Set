from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
import os

root= Tk()
root.title("Resizer for Icon Set")
filename=""

def showImage(filename):
    #print(filename)
    image = Image.open(filename)
    #print(type(image))
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image=photo


def printName():
    print("Selam")

def convert():
    if(filename!=""):
        print("Nice!")
        newWidth=256
        newHeight=256
        print(type(newWidth))
        for size in range(1,6):
            img=Image.open(filename)
            newWidth=newWidth/2
            newHeight=newHeight/2
            img=img.resize((int(newWidth),int(newHeight)), Image.ANTIALIAS)
            img.save(os.path.split(filename)[0]+"/"+str(int(newWidth))+"_"+os.path.split(filename)[1])

    else:
        print("Not work!")

def chooseAFile():
    global filename
    filename = askopenfilename()
    if(filename.find(".jpg") != -1 or filename.find(".png") != -1 or filename.find(".gif") != -1):
        showImage(filename)
    else:
        print("Please, select an image file!")

frameImage= Frame(root)
frameButtons = Frame(root)

buttonBrowse = Button(frameButtons, text="Browse", command=chooseAFile)
buttonBrowse.grid(row=0,column=0,padx=5,pady=5)

buttonConvert= Button(frameButtons, text="Convert", command=convert)
buttonConvert.grid(row=0,column=1,padx=5, pady=5)

image=PhotoImage()
label=Label(frameImage,image=None)
label.grid(row=0,column=0)

frameImage.pack(side=TOP,fill=X)
frameButtons.pack(side=BOTTOM)
#frame.grid(row=0,column=1)

root.mainloop()
