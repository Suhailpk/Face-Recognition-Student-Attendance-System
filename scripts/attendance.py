from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import csv
from tkinter import filedialog
from tkinter import messagebox

mydata = []
class AttendanceSystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recogonition System')

        #================================== text variables =================================

        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        #first image
        img = Image.open(r"collected_imgs/istockphoto-1137558833-612x612.jpg")
        img = img.resize((750,80),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=750,height=80)


        #second image
        img1 = Image.open(r"collected_imgs/facialrecognition.png")
        img1 = img1.resize((750,80),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=750,height=80)


        #bg image
        img3 = Image.open(r"collected_imgs/26-266158_nature-hd-wallpaper-landscape-wallpapers-nature-landscape-best.jpg")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=80,width=1530,height=710)

        #heading
        title_lbl = Label(bg_img,text="STUDENT ATTENDANCE SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=25)

        #main frame
        main_frame = Frame(bg_img,bd=2,bg = 'white')
        main_frame.place(x=3,y=30,width=1350,height=583)

        #left frame
        left_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student attendance details',font=('times new roman',12,'bold'))
        left_frame.place(x=10,y=10,width=730,height=570)

        #left frame image
        img_left = Image.open(r"collected_imgs/download (1).jpeg")
        img_left = img_left.resize((720,180),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=715,height=180)

        #current course frame
        current_course_frame = LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,font=('times new roman',12,'bold'))
        current_course_frame.place(x=5,y=180,width=715,height=370)

        #attendaceid
        attendanceid_label = Label(current_course_frame,text='AttendanceId:',font=('times new roman',12,'bold'),bg='white')
        attendanceid_label.grid(row=0,column=0,padx=10,pady=10)

        attendanceid_entry = ttk.Entry(current_course_frame,textvariable=self.var_id,width=20,font=('times new roman',12,'bold'))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label = Label(current_course_frame,text='Roll:',font=('times new roman',12,'bold'),bg='white')
        roll_label.grid(row=0,column=2,padx=10,pady=10)

        roll_entry = ttk.Entry(current_course_frame,width=18,textvariable=self.var_roll,font=('times new roman',12,'bold'))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #name
        name_label = Label(current_course_frame,text='Name:',font=('times new roman',12,'bold'),bg='white')
        name_label.grid(row=1,column=0,padx=10,pady=10)

        name_entry = ttk.Entry(current_course_frame,width=20,textvariable=self.var_name,font=('times new roman',12,'bold'))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #department
        department_label = Label(current_course_frame,text='Department:',font=('times new roman',12,'bold'),bg='white')
        department_label.grid(row=1,column=2,padx=10,pady=10)

        department_entry = ttk.Entry(current_course_frame,textvariable=self.var_dep,width=18,font=('times new roman',12,'bold'))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #time
        time_label = Label(current_course_frame,text='Time:',font=('times new roman',12,'bold'),bg='white')
        time_label.grid(row=2,column=0,padx=10,pady=10)

        time_entry = ttk.Entry(current_course_frame,width=20,textvariable=self.var_time,font=('times new roman',12,'bold'))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #date
        date_label = Label(current_course_frame,text='Date:',font=('times new roman',12,'bold'),bg='white')
        date_label.grid(row=2,column=2,padx=10,pady=10)

        date_entry = ttk.Entry(current_course_frame,width=18,textvariable=self.var_date,font=('times new roman',12,'bold'))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance status
        attendance_label = Label(current_course_frame,text='Attendance Status:',font=('times new roman',12,'bold'),bg='white')
        attendance_label.grid(row=3,column=0,padx=10)

        attendance_combo = ttk.Combobox(current_course_frame,textvariable=self.var_attendance,font=('times new roman',12,'bold'),state='readonly',width=18)
        attendance_combo['values'] = ('Status','Present','Absent')
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        btn_frame = Frame(current_course_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=313,width=710,height=55)

        importcsv_btn = Button(btn_frame,width=15,text='Import CSV',command=self.importcsv,font=('times new roman',12,'bold'),bg='blue',fg='white',height=3)
        importcsv_btn.grid(row=0,column=0)

        exportcsv_btn = Button(btn_frame,width=15,text='Export CSV',command=self.exportcsv,font=('times new roman',12,'bold'),bg='blue',fg='white',height=3)
        exportcsv_btn.grid(row=0,column=1)

        update_btn = Button(btn_frame,width=15,text='Update',font=('times new roman',12,'bold'),bg='blue',fg='white',height=3)
        update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,width=15,text='Reset',command=self.reset_data,font=('times new roman',12,'bold'),bg='blue',fg='white',height=3)
        reset_btn.grid(row=0,column=3)



        #right frame
        right_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Attendance details',font=('times new roman',12,'bold'))
        right_frame.place(x=750,y=10,width=590,height=570)

        scroll_x = ttk.Scrollbar(right_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_frame,orient=VERTICAL)

        self.attendance_report_table = ttk.Treeview(right_frame,columns=('id','roll','name','dep','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendance_report_table.xview)
        scroll_y.config(command=self.attendance_report_table.yview)

        self.attendance_report_table.heading('id',text='AttendanceId')
        self.attendance_report_table.heading('roll',text='Roll')
        self.attendance_report_table.heading('name',text='Name')
        self.attendance_report_table.heading('dep',text='Department')
        self.attendance_report_table.heading('time',text='Time')
        self.attendance_report_table.heading('date',text='Date')
        self.attendance_report_table.heading('attendance',text='Attendance')

        self.attendance_report_table['show'] = 'headings'

        self.attendance_report_table.column('id',width=100)
        self.attendance_report_table.column('roll',width=100)
        self.attendance_report_table.column('name',width=100)
        self.attendance_report_table.column('dep',width=100)
        self.attendance_report_table.column('time',width=100)
        self.attendance_report_table.column('date',width=100)
        self.attendance_report_table.column('attendance',width=100)

        self.attendance_report_table.pack(fill=BOTH,expand=1)

        self.attendance_report_table.bind('<ButtonRelease>',self.get_cursor)


    #============================ fetch data =============================

    def fetchdata(self,rows):
        self.attendance_report_table.delete(*self.attendance_report_table.get_children())
        for i in rows:
            self.attendance_report_table.insert('',END,values=i)

    #==================== import csv =============================

    def importcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.csv'),('ALL File','*.*')))
        with open(fln) as myfile:
            csvfile = csv.reader(myfile,delimiter=',')
            for i in csvfile:
                mydata.append(i)
            self.fetchdata(mydata)


    #====================== export csv =====================
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror('Error','No Data Found to Export',parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.csv'),('ALL File','*.*')))
            with open(fln,mode='w',newline='') as myfile:
                csv_writer = csv.writer(myfile,delimiter=',')
                for i in mydata:
                    csv_writer.writerow(i)
                messagebox.showinfo('Data Export','Your data exported to '+os.path.basename(fln)+ 'successfully')
            
        except Exception as es:
            messagebox.showerror('Error',f'{str(es)}',parent=self.root)

    #==================== get cursor ===================================

    def get_cursor(self,event=''):
       cursor_row = self.attendance_report_table.focus()
       content = self.attendance_report_table.item(cursor_row)
       rows = content['values']

       self.var_id.set(rows[0])
       self.var_roll.set(rows[1])
       self.var_name.set(rows[2])
       self.var_dep.set(rows[3])
       self.var_time.set(rows[4])
       self.var_date.set(rows[5])
       self.var_attendance.set(rows[6])


    # ======================= reset data ===========================
    def reset_data(self): 

       self.var_id.set('')
       self.var_roll.set('')
       self.var_name.set('')
       self.var_dep.set('')
       self.var_time.set('')
       self.var_date.set('')
       self.var_attendance.set('')

            
        
            







if __name__ == '__main__':
    root = Tk()
    obj = AttendanceSystem(root)
    root.mainloop()