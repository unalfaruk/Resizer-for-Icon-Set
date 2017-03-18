#!/usr/bin/env python3
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
import os, sys

root= Tk()
root.title("Resizer for Icon Set")
root.minsize(250,250)
root.resizable(0,0)
filename=""

def showImage(filename):
    #print(filename)
    image = Image.open(filename)
    width, height = image.size
    print(str(width) +" "+ str(height))
    if(width > 600 or height >600):
        image=image.resize((600,600), Image.ANTIALIAS)
    else:
        if(width<height):
            image=image.resize((width,width), Image.ANTIALIAS)
        else:
            image=image.resize((height,height), Image.ANTIALIAS)
    #print(type(image))
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image=photo

def convert():
    error=0
    if(filename!=""):
        #print("Nice!")
        newWidth=256
        newHeight=256
        #print(type(newWidth))
        for size in range(1,6):
            img=Image.open(filename)
            newWidth=newWidth/2
            newHeight=newHeight/2
            try:
                img=img.resize((int(newWidth),int(newHeight)), Image.ANTIALIAS)
                img.save(os.path.split(filename)[0]+"/"+str(int(newWidth))+"_"+os.path.split(filename)[1])
            except:
                error=error+1

        if(error==0):
            tkinter.messagebox.showinfo("Operation Completed!", "Congrulation! Successfull.")
        elif(error>0):
            tkinter.messagebox.showinfo("Operation Not Completed!", "Ooops! Not successfull, there is an error.")

    else:
        print("Please, select an image file.")

def chooseAFile():
    global filename
    filename = askopenfilename(initialdir="~",title="Select an Image File", filetypes=(("JPEG Files","*.jpg"),("PNG Files", "*.png"),("GIF Files","*.gif"),("All Files","*.*")))
    checkMime(filename)

def checkMime(path):
    if(type(path)==str):
        if(filename.find(".jpg") != -1 or filename.find(".png") != -1 or filename.find(".gif") != -1):
            showImage(filename)
            buttonConvert.config(state="normal")
        else:
            print("Please, select an image file!")

frameImage= Frame(root)

image=PhotoImage()
label=Label(frameImage,image=None)
label.grid(row=0,column=0,padx=5,pady=5)


frameButtons = Frame(root)

buttonBrowse = Button(frameButtons, text="Browse", command=chooseAFile)
buttonBrowse.grid(row=0,column=0,padx=5,pady=5)

buttonConvert= Button(frameButtons, text="Convert", command=convert, state=DISABLED)
buttonConvert.grid(row=0,column=1,padx=5, pady=5)


frameImage.pack(side=TOP,fill=X)
frameButtons.pack(side=BOTTOM, fill=X)

if len(sys.argv)>1:
    filename=sys.argv[1]
    checkMime(filename)

root.mainloop()
