from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import numpy as np
import cv2
from tkinter import messagebox



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Train')

        #heading
        title_lbl = Label(self.root,text="TRAINING THE DATA",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #top image
        top_img = Image.open(r"collected_imgs/artificial-intelligence-deep-learning-neural-networks-ai-1.jpg")
        top_img = top_img.resize((1530,300),Image.ANTIALIAS)
        self.phototop_img = ImageTk.PhotoImage(top_img)

        f_lbl = Label(self.root,image=self.phototop_img)
        f_lbl.place(x=0,y=47,width=1530,height=300)

        #Train button
        b1_txt = Button(self.root,text='TRAIN DATA',cursor='hand2',command=self.train_data,font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_txt.place(x=0,y=340,width=1530,height=60)

        #bottom image
        bottom_img = Image.open(r"collected_imgs/neural-network.jpg")
        bottom_img = bottom_img.resize((1530,300),Image.ANTIALIAS)
        self.photobottom_img = ImageTk.PhotoImage(bottom_img)

        f_lbl = Label(self.root,image=self.photobottom_img)
        f_lbl.place(x=0,y=400,width=1530,height=300)



    def train_data(self):
        data_dir = 'data'
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #convert to gray
            img = np.array(img,'uint8')

            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(img)
            ids.append(id)
            cv2.imshow('Training',img)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        #Train the data and save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Result','Training datasets completed !!',parent=self.root)






if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()
