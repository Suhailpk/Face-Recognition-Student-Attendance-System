from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Developer')

        #heading
        title_lbl = Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #top image
        top_img = Image.open(r"collected_imgs/1_183 Stanford University Stock Photos - Free &_yyt.jpg")
        top_img = top_img.resize((1530,657),Image.ANTIALIAS)
        self.phototop_img = ImageTk.PhotoImage(top_img)

        f_lbl = Label(self.root,image=self.phototop_img)
        f_lbl.place(x=0,y=47,width=1530,height=657)

        #main frame
        main_frame = Frame(self.root,bd=2,bg = 'white')
        main_frame.place(x=370,y=125,width=600,height=500)

        #label
        label_lbl = Label(main_frame,text="Hello this is developer Suhail",font=("times new roman",15,"bold"),bg="white",fg="blue")
        label_lbl.place(x=0,y=30)

        #label
        label2_lbl = Label(main_frame,text="Contribute to our company and help us create a",font=("times new roman",15,"bold"),bg="white",fg="blue")
        label2_lbl.place(x=0,y=60)

                #label
        label3_lbl = Label(main_frame,text="dynamic and informative platform for everyone.",font=("times new roman",15,"bold"),bg="white",fg="blue")
        label3_lbl.place(x=0,y=90)

        #label
        label4_lbl = Label(main_frame,text="emailid - suhailpk24@gmail.com",font=("times new roman",15,"bold"),bg="white",fg="blue")
        label4_lbl.place(x=0,y=120)

        #top image
        inside_img = Image.open('collected_imgs/image1-4.jpg')
        inside_img = inside_img.resize((600,350),Image.ANTIALIAS)
        self.photoinside_img = ImageTk.PhotoImage(inside_img)

        f_lbl = Label(main_frame,image=self.photoinside_img)
        f_lbl.place(x=0,y=150,width=600,height=350)







if __name__ == '__main__':
    root = Tk()
    obj = Developer(root)
    root.mainloop()
