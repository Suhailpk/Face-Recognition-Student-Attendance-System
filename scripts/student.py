from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recogonition System')

        #================== Variables =========================================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        #first image
        img = Image.open(r"collected_imgs/istockphoto-1137558833-612x612.jpg")
        img = img.resize((500,80),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=80)

        #second image
        img1 = Image.open(r"collected_imgs/facialrecognition.png")
        img1 = img1.resize((500,80),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=80)

        #third image
        img2 = Image.open(r"collected_imgs/1_183 Stanford University Stock Photos - Free &_yyt.jpg")
        img2 = img2.resize((500,80),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=80)

        #bg image
        img3 = Image.open(r"collected_imgs/26-266158_nature-hd-wallpaper-landscape-wallpapers-nature-landscape-best.jpg")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=80,width=1530,height=710)

        #heading
        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=25)

        #main frame
        main_frame = Frame(bg_img,bd=2,bg = 'white')
        main_frame.place(x=3,y=30,width=1350,height=583)

        #left frame
        left_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student details',font=('times new roman',12,'bold'))
        left_frame.place(x=10,y=10,width=730,height=570)

        #left frame image
        img_left = Image.open(r"collected_imgs/panoramic-shot-smiling-multicultural-students-laptop-university-192593492.jpg")
        img_left = img_left.resize((720,80),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=715,height=80)

        #current course frame
        current_course_frame = LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text='Current course information',font=('times new roman',12,'bold'))
        current_course_frame.place(x=5,y=80,width=715,height=150)

        #Department
        dep_label = Label(current_course_frame,text='Department',font=('times new roman',12,'bold'),bg='white')
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=('times new roman',12,'bold'),state='readonly',width=20)
        dep_combo['values'] = ('Select Department','CSE','Civil','Mech','EEE')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label = Label(current_course_frame,text='Course',font=('times new roman',12,'bold'),bg='white')
        course_label.grid(row=0,column=2,padx=10)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=('times new roman',12,'bold'),state='readonly',width=20)
        course_combo['values'] = ('Select Course','FE','SE','TE','BE')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label = Label(current_course_frame,text='Year',font=('times new roman',12,'bold'),bg='white')
        year_label.grid(row=1,column=0,padx=10)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=('times new roman',12,'bold'),state='readonly',width=20)
        year_combo['values'] = ('Select Year','2020-21','2021-22','2022-23','2023-24')
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label = Label(current_course_frame,text='Semseter',font=('times new roman',12,'bold'),bg='white')
        sem_label.grid(row=1,column=2,padx=10)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=('times new roman',12,'bold'),state='readonly',width=20)
        sem_combo['values'] = ('Select Semseter','Semester 1','Semester 2')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame = LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text='Class student information',font=('times new roman',12,'bold'))
        class_student_frame.place(x=5,y=230,width=720,height=315)

        #student id label
        studentid_label = Label(class_student_frame,text='Student ID:',font=('times new roman',12,'bold'),bg='white')
        studentid_label.grid(row=0,column=0,padx=10)

        studentid_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=('times new roman',12,'bold'))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentname_label = Label(class_student_frame,text='Student Name:',font=('times new roman',12,'bold'),bg='white')
        studentname_label.grid(row=0,column=2,padx=10)

        studentname_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=('times new roman',12,'bold'))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        classdivision_label = Label(class_student_frame,text='Class Division:',font=('times new roman',12,'bold'),bg='white')
        classdivision_label.grid(row=1,column=0,padx=10)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=('times new roman',12,'bold'),state='readonly',width=18)
        div_combo['values'] = ('Select Division','A','B','C','D')
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        rollno_label = Label(class_student_frame,text='Roll No:',font=('times new roman',12,'bold'),bg='white')
        rollno_label.grid(row=1,column=2,padx=10)

        rollno_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=('times new roman',12,'bold'))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label = Label(class_student_frame,text='Gender:',font=('times new roman',12,'bold'),bg='white')
        gender_label.grid(row=2,column=0,padx=10)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=('times new roman',12,'bold'),state='readonly',width=18)
        gender_combo['values'] = ('Select Gender','Male','Female')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label = Label(class_student_frame,text='DOB:',font=('times new roman',12,'bold'),bg='white')
        dob_label.grid(row=2,column=2,padx=10)

        dob_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=('times new roman',12,'bold'))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label = Label(class_student_frame,text='Email:',font=('times new roman',12,'bold'),bg='white')
        email_label.grid(row=3,column=0,padx=10)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=('times new roman',12,'bold'))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No
        phoneno_label = Label(class_student_frame,text='Phone No:',font=('times new roman',12,'bold'),bg='white')
        phoneno_label.grid(row=3,column=2,padx=10)

        phoneno_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=('times new roman',12,'bold'))
        phoneno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label = Label(class_student_frame,text='Address:',font=('times new roman',12,'bold'),bg='white')
        address_label.grid(row=4,column=0,padx=10)

        address_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=('times new roman',12,'bold'))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teacher_label = Label(class_student_frame,text='Teacher Name:',font=('times new roman',12,'bold'),bg='white')
        teacher_label.grid(row=4,column=2,padx=10)

        teacher_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=('times new roman',12,'bold'))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radiobutton1
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,text='Take Photo Sample',value='Yes',variable=self.var_radio1)
        radiobtn1.grid(row=5,column=0)

        #radiobutton2
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='No. of Photo Sample',value='No')
        radiobtn2.grid(row=5,column=1)

        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=715,height=90)

        save_btn = Button(btn_frame,width=15,text='Save',command=self.add_data,font=('times new roman',12,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,width=15,text='Update',command=self.update_data,font=('times new roman',12,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,width=15,text='Delete',command=self.delete_data,font=('times new roman',12,'bold'),bg='blue',fg='white')
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,width=15,text='Reset',command=self.reset_data,font=('times new roman',12,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)

        btn_frame2 = Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame2.place(x=0,y=230,width=715,height=90)

        take_btn = Button(btn_frame2,width=34,height=3,command=self.generate_dataset,text='Take photo sample',font=('times new roman',12,'bold'),bg='blue',fg='white')
        take_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame2,width=34,height=3,text='Update photo sample',font=('times new roman',12,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)


        #right frame
        right_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student details',font=('times new roman',12,'bold'))
        right_frame.place(x=750,y=10,width=590,height=570)

        #right frame image
        img_right = Image.open(r"collected_imgs/istockphoto-1166773849-612x612.jpg")
        img_right = img_right.resize((580,80),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=580,height=80)

        #class student information
        search_frame = LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE,text='Search System',font=('times new roman',12,'bold'))
        search_frame.place(x=5,y=85,width=580,height=60)

        #Search
        search_label = Label(search_frame,text='Search By:',font=('times new roman',12,'bold'),bg='red',fg='white')
        search_label.grid(row=0,column=0,padx=2,pady=2)


        sem_combo = ttk.Combobox(search_frame,font=('times new roman',12,'bold'),state='readonly',width=12)
        sem_combo['values'] = ('Select','Roll No','Phone No')
        sem_combo.current(0)
        sem_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)


        teacher_entry = ttk.Entry(search_frame,width=12,font=('times new roman',12,'bold'))
        teacher_entry.grid(row=0,column=2,padx=2,pady=2,sticky=W)


        search_btn = Button(search_frame,width=6,text='Search',font=('times new roman',12,'bold'),bg='blue',fg='white')
        search_btn.grid(row=0,column=3,padx=7,pady=2)

        showall_btn = Button(search_frame,width=6,text='Show all',font=('times new roman',12,'bold'),bg='blue',fg='white')
        showall_btn.grid(row=0,column=4,padx=2,pady=2)

        #Table frame
        table_frame = LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=145,width=580,height=400)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=('dep','course','year','sem','id','name','div','roll','gender','dob','email','phone','address','teacher','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading('dep',text='Department')
        self.student_table.heading('course',text='Course')
        self.student_table.heading('year',text='Year')
        self.student_table.heading('sem',text='Sem')
        self.student_table.heading('id',text='Id')
        self.student_table.heading('name',text='Name')
        self.student_table.heading('div',text='Div')
        self.student_table.heading('roll',text='Roll')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('dob',text='DOB')
        self.student_table.heading('email',text='Email')
        self.student_table.heading('phone',text='Phone')
        self.student_table.heading('address',text='Address')
        self.student_table.heading('teacher',text='Teacher')
        self.student_table.heading('photo',text='PhotoSampleStatus')
        self.student_table['show'] = 'headings'


        self.student_table.column('dep',width=100)
        self.student_table.column('course',width=100)
        self.student_table.column('year',width=100)
        self.student_table.column('sem',width=100)
        self.student_table.column('id',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('div',width=100)
        self.student_table.column('roll',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('phone',width=100)
        self.student_table.column('address',width=100)
        self.student_table.column('teacher',width=100)
        self.student_table.column('photo',width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()

    #================== function declaration================================
    def add_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_std_name.get() == '' or self.var_std_id.get() == '':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='137952427',database='attendance')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_std_id.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get()


                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Sucess','Succesfully added student details',parent=self.root)

            except Exception as e:
                messagebox.showerror('Error',f'Due to : {str(e)}',parent=self.root)


    #=================== fetch data ========================================
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='137952427',database='attendance')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from student')
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    #========================= get cursor =========================================
    def get_cursor(self,event=''):
        focus = self.student_table.focus()
        content = self.student_table.item(focus)
        data = content['values']

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #==================== update details ========================================
    def update_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_std_name.get() == '' or self.var_std_id.get() == '':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update = messagebox.askyesno('Update','Do you want to update',parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='137952427',database='attendance')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get(),
                                                                                    self.var_std_id.get()                                                                     
                                                                                                                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo('Success','Successfully updated the details',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror('Error',f'{str(e)}',parent=self.root)

    #======================= delete data ======================================
    def delete_data(self):
        if self.var_std_id.get() == '':
            messagebox.showerror('Student id','Student id must be required',parent=self.root)
        else:
            try:
                delete = messagebox.askyesno('Delete','are you want to delete student details')
                if delete > 0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='137952427',database='attendance')
                    my_cursor = conn.cursor()
                    sql = 'delete from student where Student_id = %s'
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                messagebox.showinfo('Success','Sucessfully deleted student details',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror('Error',f'{str(e)}',parent=self.root)

#================================== reset data =========================
    def reset_data(self):
        reset = messagebox.askyesno('Reset','Are you sure to reset the details',parent=self.root)
        if reset>0:
            self.var_dep.set('Select Department'),
            self.var_course.set('Select Course'),
            self.var_year.set('Select Year'),
            self.var_semester.set('Select Semester'),
            self.var_std_id.set(''),
            self.var_std_name.set(''),
            self.var_div.set('Select Division'),
            self.var_roll.set(''),
            self.var_gender.set('Select Gender'),
            self.var_dob.set(''),
            self.var_email.set(''),
            self.var_phone.set(''),
            self.var_address.set(''),
            self.var_teacher.set(''),
            self.var_radio1.set('')
        else:
            if not reset:
                return
    
    #reset data for datasample
    def reset_data_photosample(self):
        self.var_dep.set('Select Department'),
        self.var_course.set('Select Course'),
        self.var_year.set('Select Year'),
        self.var_semester.set('Select Semester'),
        self.var_std_id.set(''),
        self.var_std_name.set(''),
        self.var_div.set('Select Division'),
        self.var_roll.set(''),
        self.var_gender.set('Select Gender'),
        self.var_dob.set(''),
        self.var_email.set(''),
        self.var_phone.set(''),
        self.var_address.set(''),
        self.var_teacher.set(''),
        self.var_radio1.set('')

#======================= generate dataset or collecting image ======================
    def generate_dataset(self):
        if self.var_dep.get() == 'Select Department' or self.var_std_name.get() == '' or self.var_std_id.get() == '':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='137952427',database='attendance')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student')
                my_result = my_cursor.fetchall()
                id = 0      
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get(),
                                                                                    self.var_std_id.get()==id+1                                                                     
                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data_photosample()
                conn.close()

                # load haarscascade xml file

                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3
                    #Minimum neighbour 5

                    for (x,y,w,h) in faces:
                        face_croped = img[y:y+h,x:x+w]
                        return face_croped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True: 
                    ret,myframe = cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(myframe),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path = 'data/user.'+str(id)+'.'+str(img_id)+'.jpg'
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo('Success','Generating dataset completed')

            except Exception as e:
                messagebox.showerror('Error',f'{str(e)}',parent=self.root)








if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
