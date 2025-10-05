from tkinter import *
import ctypes,os
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename
import numpy as np
import PIL
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow import keras
import tkinter as tk
import cv2
from PIL import Image, ImageChops,ImageEnhance
from skimage.io import imread, imshow
from skimage.transform import resize

        
home = Tk()
home.title("Brain Stroke Classification")

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-450)
b= str(lt[1]//2-320)
home.geometry("900x653+"+a+"+"+b)
home.resizable(0,0)
file = ''


def Exit():
    global home
    result = tkMessageBox.askquestion(
        "Brain Stroke Classification", 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        home.destroy()
        exit()
    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the main screen')
        
def browse():
    
    global file,l1
    try:
        l1.destroy()
    except:
        pass
    file = askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=( ("images", ".png"),("images", ".jpg"),("images", ".jpeg")))



def about():
    about = Toplevel()
    about.title("Brain Stroke Classification")
    img = Image.open("images/about.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(about, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-450)
    b= str(lt[1]//2-320)
    about.geometry("900x653+"+a+"+"+b)
    about.resizable(0,0)
    about.mainloop()

def predict():
    global file,l1
    if file!='' or file!= None:

        class_names = ['Normal','Stroke']
        model = keras.models.load_model('C:/Users/hp/Desktop/Brain Stroke Classification Software/stroke_model.h5')

        image = cv2.imread(file)
        img = image
        image = cv2.resize(image,(128,128))
        image = image.reshape(-1,128,128,3)
        y_pred = model.predict(image)
        y_pred_class = np.argmax(y_pred, axis = 1)[0]
        result = class_names[y_pred_class]
        print(result)

        pValue = "Prediction: ",(result)      
        img = cv2.resize(img,(224,224))
        #imag = ImageTk.PhotoImage(Image.open(file))
        # im = PhotoImage(file)
        # label = tk.Label(home, image = im)
        # label.config(background='white')
        # label.pack()
        

        
        fig = plt.figure(figsize=(10, 7))
        rows = 1
        columns = 2

        fig.add_subplot(rows, columns, 1)
        plt.imshow(img)
        plt.axis('off')
        plt.title(pValue)
        plt.show()
	
        
        
        
        
        

img = Image.open("images/home.png")
img = ImageTk.PhotoImage(img)
panel = Label(home, image=img)
panel.pack(side="top", fill="both", expand="yes")

photo = Image.open("images/1.png")
img2 = ImageTk.PhotoImage(photo)
b1=Button(home, highlightthickness = 0, bd = 0,activebackground="#2b4b47", image = img2,command=browse)
b1.place(x=0,y=209)

photo = Image.open("images/2.png")
img3 = ImageTk.PhotoImage(photo)
b2=Button(home, highlightthickness = 0, bd = 0,activebackground="#2b4b47", image = img3, command=predict)
b2.place(x=0,y=282)

photo = Image.open("images/3.png")
img4 = ImageTk.PhotoImage(photo)
b3=Button(home, highlightthickness = 0, bd = 0,activebackground="#2b4b47", image = img4,command=about)
b3.place(x=0,y=354)

photo = Image.open("images/4.png")
img5 = ImageTk.PhotoImage(photo)
b4=Button(home, highlightthickness = 0, bd = 0,activebackground="#2b4b47", image = img5,command=Exit)
b4.place(x=0,y=426)

home.mainloop()