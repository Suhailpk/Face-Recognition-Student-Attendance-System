from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import mysql.connector
import os
from time import strftime
import datetime
from tkinter import filedialog
from tkinter import messagebox



class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Train')

        #heading
        title_lbl = Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #left image
        left_img = Image.open(r"collected_imgs/face-600x900.png")
        left_img = left_img.resize((650,700),Image.ANTIALIAS)
        self.photoleft_img = ImageTk.PhotoImage(left_img)

        f_lbl = Label(self.root,image=self.photoleft_img)
        f_lbl.place(x=0,y=46,width=650,height=700)

        #rightimage
        right_img = Image.open(r"collected_imgs/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        right_img = right_img.resize((950,700),Image.ANTIALIAS)
        self.photoright_img = ImageTk.PhotoImage(right_img)

        f_lbl = Label(self.root,image=self.photoright_img)
        f_lbl.place(x=650,y=46,width=950,height=700)

        #Train button
        b1_txt = Button(self.root,text='FACE DECTECTOR',command=self.askopenfile,cursor='hand2',font=("times new roman",18,"bold"),bg="red",fg="white")
        b1_txt.place(x=1020,y=660,width=230,height=40)

        #create button
        b1_txt = Button(self.root,text='Create new file',command=self.create_file,cursor='hand2',font=("times new roman",18,"bold"),bg="red",fg="white")
        b1_txt.place(x=50,y=660,width=230,height=40)


    #===================== creating new file =====================
    def create_file(self):
        create_file = filedialog.asksaveasfilename(initialdir=os.path.join('Attendace_report_file'),title='Create CSV',filetypes=(('CSV File','*.csv'),('ALL File','*.*')))
        fob=open(create_file,'w')
        fob.write("")
        fob.close()
        messagebox.showinfo('Success','Successfully created the file')

    #======================= attendance save =================
    def mark_attendance(self,filename,i,r,n,d):
        with open('Attendace_report_file/'+filename,'r+',newline='\n') as f:
            mydatalist = f.readlines()
            name_list = []
            for line in mydatalist:
                entry = line.split((','))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.datetime.now()
                d1 = now.strftime('%d/%m/%Y')
                dtstring = now.strftime('%H:%M:%S')
                f.writelines(f'\n{i},{r},{n},{d},{dtstring},{d1},Present')





        
    #========================== face recognition =====================================
    def askopenfile(self):
            open = filedialog.askopenfilename(initialdir=os.path.join('Attendace_report_file'),title='Open CSV',filetypes=(('CSV File','*.csv'),('ALL File','*.*')))

            if open != () :
                open = open.split('/')[-1]
                self.face_recognition(filename=open)
            else:
                messagebox.showerror('File','Choose a file')

    
    

    def face_recognition(self,filename):
        def draw_boundary(img,classifier,scalefactor,minneigbour,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scalefactor,minneigbour)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host='localhost',username='root',password='137952427',database='attendance')
                my_cursor = conn.cursor()

                my_cursor.execute('select Name from student where Student_id='+str(id))
                n = my_cursor.fetchone()
                n = '+'.join(n)

                my_cursor.execute('select Roll from student where Student_id='+str(id))
                r = my_cursor.fetchone()
                r = '+'.join(r)

                my_cursor.execute('select Dep from student where Student_id='+str(id))
                d = my_cursor.fetchone()
                d = '+'.join(d)

                my_cursor.execute('select Student_id from student where Student_id='+str(id))
                i = my_cursor.fetchone()
                i = '+'.join(i)


                if confidence > 50:
                    cv2.putText(img,f'ID:{i}',(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f'Roll:{r}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f'Name:{n}',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                    cv2.putText(img,f'Department:{d}',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    self.mark_attendance(filename,i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3) 
                    cv2.putText(img,'Unknown Face',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord = [x,y,w,h]

            return coord    
        
        def recognize(img,clf,facecascade):
            coord = draw_boundary(img,facecascade,1.1,10,(255,25,255),'Face',clf)
            return img

        facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        cap = cv2.VideoCapture(0)

        
        
        while True:
            ret,img = cap.read()
            img = recognize(img,clf,facecascade)
            cv2.imshow('Face Recognition',img)
            if cv2.waitKey(1) & 0XFF == ord('q'):
                break

            elif cv2.waitKey(1)==13:
                break

        cap.release()
        cv2.destroyAllWindows()
            







if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
