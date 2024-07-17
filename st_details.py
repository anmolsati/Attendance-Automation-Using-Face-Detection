from tkinter import*
from tkinter import ttk                                                         
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student_Details:
    def __init__(self, root):                                                                                                 
        self.root = root                
        self.root.geometry("1200x680+0+0")
        self.root.title("ATTENDANCE AUTOMATION SYSTEM")

        #VARIABLES
        self.var_dep= StringVar()
        self.var_course= StringVar()
        self.var_section= StringVar()
        self.var_year= StringVar()
        self.var_id = StringVar()
        self.var_name= StringVar()
        self.var_rollno= StringVar()
        self.var_gender= StringVar()
        self.var_email= StringVar()
        self.var_phoneno= StringVar()
        self.var_address= StringVar()
        self.var_dob= StringVar()

        #logo image
        img_1 = Image.open(r"logo1.png")                          
        img_1 = img_1.resize((1200, 80), Image.ANTIALIAS)                                                                      
        self.photoimg_1 = ImageTk.PhotoImage(img_1) 
        lbl_1 = Label(self.root, image = self.photoimg_1)
        lbl_1.place (x=0, y=0, width= 1200, height= 80)

        #background image
        img_2 = Image.open(r"bg.png")          
        img_2 = img_2.resize((1200, 600), Image.ANTIALIAS)                                               
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        bg_lbl = Label(self.root, image = self.photoimg_2)
        bg_lbl.place (x=0, y=80, width= 1200, height= 600)
        

        title_lbl = Label(bg_lbl, text = "STUDENT    DETAILS", font=("Times New Roman", 20, "bold"), bg = "white", fg = "#bd0d2f")
        title_lbl.place(x= -2, y= -2, width= 1200, height= 30)

        #CREATING FRAME
        main_frame = Frame(bg_lbl, bd = 2, bg= "white")
        main_frame.place(x= 11, y= 37, width= 1170, height= 550)

        #LEFT LABEL FRAME
        Left_frame = LabelFrame(main_frame, bd=2, bg= "white", relief= RIDGE, text= "STUDENT DETAILS", font=("Times New Roman", 12, "bold"))          
        Left_frame.place(x= 8, y= 5, width= 570, height= 535)

        img_left = Image.open(r"img_left.jpg")        
        img_left = img_left.resize((600, 150), Image.ANTIALIAS)                                               
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        bg_lbl = Label(Left_frame, image = self.photoimg_left)
        bg_lbl.place (x= 3, y= 1, width= 560, height= 120)

        #COURSE FRAME
        Course_frame = LabelFrame(Left_frame, bd=2, bg= "white", relief= RIDGE, text= "COURSE INFO", font=("Times New Roman", 12, "bold"))          
        Course_frame.place(x= 3, y= 125, width= 560, height= 100)

        #COURSE
        Course_label = Label(Course_frame, text="Course:", font=("Times New Roman", 12, "bold"), bg= "white")
        Course_label.grid(row= 0, column= 0, padx= 7, sticky= W)
        Course_combo = ttk.Combobox(Course_frame, textvariable=self.var_course, font=("Times New Roman", 12), width= 17, state= "readonly")
        Course_combo["values"]= ("Select Course", "B. Tech", "M. Tech", "BSc", "MSc", "BCA", "MCA", "BBA", "MBA")
        Course_combo.current(0)
        Course_combo.grid(row= 0, column= 1, padx= 2, pady= 5, sticky= W)

        #DEPARTMENT
        Dept_label = Label(Course_frame, text="  Department:", font=("Times New Roman", 12, "bold"), bg= "white")
        Dept_label.grid(row= 0, column= 2, padx= 7, sticky= W)
        Dept_combo = ttk.Combobox(Course_frame, textvariable=self.var_dep, font=("Times New Roman", 12), width= 17, state= "readonly")
        Dept_combo["values"]= ("Select Department", "CSE", "ECE", "EE", "Civil", "Mechanical", "Biotechnology", "Other")
        Dept_combo.current(0)
        Dept_combo.grid(row= 0, column= 3, padx= 2, pady= 5, sticky= W)

        #SECTION
        Sec_label = Label(Course_frame, text="Section:", font=("Times New Roman", 12, "bold"), bg= "white")
        Sec_label.grid(row= 2, column= 0, padx= 7, sticky= W)
        Sec_combo = ttk.Combobox(Course_frame, textvariable=self.var_section, font=("Times New Roman", 12), width= 17, state= "readonly")
        Sec_combo["values"]= ("Select Section", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'AI', 'ML', "Cyber Security", "IOT")
        Sec_combo.current(0)
        Sec_combo.grid(row= 2, column= 1, padx= 2, pady= 5, sticky= W)

        #GRADUATION YEAR
        Year_label = Label(Course_frame, text="  Graduation Year:", font=("Times New Roman", 12, "bold"), bg= "white")
        Year_label.grid(row= 2, column= 2, padx= 7, sticky= W)
        Year_combo = ttk.Combobox(Course_frame, textvariable=self.var_year, font=("Times New Roman", 12), width= 17, state= "readonly")
        Year_combo["values"]= ("Select Year", "2023", "2024", "2025", "2026")
        Year_combo.current(0)
        Year_combo.grid(row= 2, column= 3, padx= 2, pady= 5, sticky= W)

        #STUDENT INFO FRAME
        Stu_frame = LabelFrame(Left_frame, bd=2, bg= "white", relief= RIDGE, text= "STUDENT INFO", font=("Times New Roman", 12, "bold"))            
        Stu_frame.place(x= 3, y= 230, width= 560, height= 280)

        #STUDENT ID
        StuId_label = Label(Stu_frame, text="Student ID:", font=("Times New Roman", 12, "bold"), bg= "white")
        StuId_label.grid(row= 0, column= 0, padx= 7, pady= 5, sticky= W)

        Stu_entry = ttk.Entry(Stu_frame, textvariable=self.var_id, width= 18, font=("Times New Roman", 12))
        Stu_entry.grid(row= 0, column= 1, padx= 2, sticky= W)

        #STUDENT NAME
        StuName_label = Label(Stu_frame, text="  Student Name:", font=("Times New Roman", 12, "bold"), bg= "white")
        StuName_label.grid(row= 0, column= 2, padx= 7, pady= 5, sticky= W)

        StuName_entry = ttk.Entry(Stu_frame, textvariable=self.var_name, width= 18, font=("Times New Roman", 12))
        StuName_entry.grid(row= 0, column= 3, padx= 2, sticky= W)

        #ROLL NO
        Roll_label = Label(Stu_frame, text="Roll No:", font=("Times New Roman", 12, "bold"), bg= "white")
        Roll_label.grid(row= 2, column= 0, padx= 7, pady= 5, sticky= W)

        Roll_entry = ttk.Entry(Stu_frame, textvariable=self.var_rollno, width= 18, font=("Times New Roman", 12))
        Roll_entry.grid(row= 2, column= 1, padx= 2, sticky= W)

        #GENDER
        Gender_label = Label(Stu_frame, text="  Gender:", font=("Times New Roman", 12, "bold"), bg= "white")
        Gender_label.grid(row= 2, column= 2, padx= 8, sticky= W)

        Gender_combo = ttk.Combobox(Stu_frame, textvariable=self.var_gender, font=("Times New Roman", 12), width= 17, state= "readonly")
        Gender_combo["values"]= ("Select Gender", "Male", "Female", "Other")
        Gender_combo.current(0)
        Gender_combo.grid(row= 2, column= 3)

        #EMAIL
        email_label = Label(Stu_frame, text="Email:", font=("Times New Roman", 12, "bold"), bg= "white")
        email_label.grid(row= 3, column= 0, padx= 7, pady= 5, sticky= W)

        email_entry = ttk.Entry(Stu_frame, textvariable=self.var_email, width= 18, font=("Times New Roman", 12))
        email_entry.grid(row= 3, column= 1, padx= 2, sticky= W)

        #PHONE NUMBER
        Phn_label = Label(Stu_frame, text="Phone Number:", font=("Times New Roman", 12, "bold"), bg= "white")
        Phn_label.grid(row= 3, column= 2, padx= 17, pady= 5, sticky= W)

        Phn_entry = ttk.Entry(Stu_frame, textvariable=self.var_phoneno, width= 18, font=("Times New Roman", 12))
        Phn_entry.grid(row= 3, column= 3, padx= 2, sticky= W)

        #DOB
        Dob_label = Label(Stu_frame, text="DOB:", font=("Times New Roman", 12, "bold"), bg= "white")
        Dob_label.grid(row= 4, column= 0, padx= 7, pady= 5, sticky= W)

        Dob_entry = ttk.Entry(Stu_frame, textvariable=self.var_dob, width= 18, font=("Times New Roman", 12))
        Dob_entry.grid(row= 4, column= 1, padx= 2, sticky= W)

        #ADDREESS
        Add_label = Label(Stu_frame, text="Address:", font=("Times New Roman", 12, "bold"), bg= "white")
        Add_label.grid(row= 4, column= 2, padx= 17, pady= 5, sticky= W)

        Add_entry = ttk.Entry(Stu_frame, textvariable=self.var_address, width= 18, font=("Times New Roman", 12))
        Add_entry.grid(row= 4, column= 3, padx= 2, sticky= W)

        #BUTTONS FRAME
        Butt_frame = LabelFrame(Stu_frame, bd=2, bg= "white", relief= RIDGE)
        Butt_frame.place(x= 3, y= 145, width= 550, height= 55)

        self.var_radio= StringVar()
        Take_button = ttk.Radiobutton(Butt_frame, variable= self.var_radio, text= "Take Photo Sample", value= "Yes")
        Take_button.grid(row= 0, column= 0)

        
        No_button = ttk.Radiobutton(Butt_frame, variable= self.var_radio, text= "No Photo Sample", value= "No")
        No_button.grid(row= 0, column= 3)

        Save_button = Button(Butt_frame, text= "SAVE", command= self.add_data, width= 19, font=("Times New Roman", 11, "bold"), bg = "#bd0d2f", fg = "white")
        Save_button.grid(row= 1, column= 0)

        Delete_button = Button(Butt_frame, text= "DELETE", command= self.Delete_data, width= 19, font=("Times New Roman", 11, "bold"), bg = "#bd0d2f", fg = "white")
        Delete_button.grid(row= 1, column= 1)

        Reset_button = Button(Butt_frame, text= "RESET", command=self.Reset_data, width= 19, font=("Times New Roman", 11, "bold"), bg = "#bd0d2f", fg = "white")
        Reset_button.grid(row= 1, column= 3)

        #BUTTONS FRAME 2
        Butt_frame2 = LabelFrame(Stu_frame, bd=2, bg= "white", relief= RIDGE)
        Butt_frame2.place(x= 3, y= 201, width= 550, height= 54)

        TakeP_button = Button(Butt_frame2, text= "TAKE  PHOTO  SAMPLE", command= self.Generate_dataset, width= 53, font=("Times New Roman", 13, "bold"), bg = "#bd0d2f", fg = "white")
        TakeP_button.grid(row= 0, column= 0, padx= 3, pady= 8)
        


        #RIGHT LABEL FRAME
        Right_frame = LabelFrame(main_frame, bd=2, bg= "white", relief= RIDGE, text= "Student Details", font=("Times New Roman", 12, "bold"))             
        Right_frame.place(x= 590, y= 5, width= 570, height= 535)

        img_right = Image.open(r"img_left.jpg")        
        img_right = img_right.resize((600, 150), Image.ANTIALIAS)                                               
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        bg_lbl = Label(Right_frame, image = self.photoimg_right)
        bg_lbl.place (x= 3, y= 1, width= 560, height= 120)

        #TABLE FRAME
        Table_frame = Frame(Right_frame, bd=2, bg= "white", relief= RIDGE) 
        Table_frame.place(x= 3, y= 135, width= 560, height= 350)

        Scroll_x = ttk.Scrollbar(Table_frame, orient= HORIZONTAL)
        Scroll_y = ttk.Scrollbar(Table_frame, orient= VERTICAL)

        self.Student_table = ttk.Treeview(Table_frame, column= ("course", "dep", "section", "year", "id", "name", "roll", "gender", "email", "phone", "dob", "address", "photo"), xscrollcommand= Scroll_x.set, yscrollcommand= Scroll_y.set)
        Scroll_x.pack(side= BOTTOM, fill= X)
        Scroll_y.pack(side= RIGHT, fill= Y)
        Scroll_x.config(command=self.Student_table.xview) 
        Scroll_y.config(command=self.Student_table.yview)  

        self.Student_table.heading("course", text="COURSE")
        self.Student_table.heading("dep", text="DEPARTMENT")
        self.Student_table.heading("section", text="SECTION")
        self.Student_table.heading("year", text="GRADUATION YEAR")
        self.Student_table.heading("id", text="STUDENT ID")
        self.Student_table.heading("name", text="NAME")
        self.Student_table.heading("roll", text="ROLL NO")
        self.Student_table.heading("gender", text="GENDER")
        self.Student_table.heading("email", text="EMAIL")
        self.Student_table.heading("phone", text="PHONE NO")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("address", text="ADDRESS")
        self.Student_table.heading("photo", text="PHOTO SAMPLE")
        self.Student_table["show"]= "headings"

        self.Student_table.column("course", width= 100)
        self.Student_table.column("dep", width= 100)
        self.Student_table.column("section", width= 100)
        self.Student_table.column("year", width= 120)
        self.Student_table.column("id", width= 100)
        self.Student_table.column("name", width= 100)
        self.Student_table.column("roll", width= 100)
        self.Student_table.column("gender", width= 100)
        self.Student_table.column("email", width= 100)
        self.Student_table.column("phone", width= 100)
        self.Student_table.column("dob", width= 100)
        self.Student_table.column("address", width= 100)
        self.Student_table.column("photo", width= 100)

        self.Student_table.pack(fill= BOTH, expand= 1)
        self.Student_table.bind("<ButtonRelease>", self.Get_cursor)
        self.Fetch_data()

    def add_data(self):
        #validation
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_course.get() == "Select Course" or self.var_section.get() == "":
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED", parent= self.root)
        else :
            try:
                conn= mysql.connector.connect(host= os.getenv("MYSQL_HOST"), username= os.getenv("MYSQL_USER"), password= os.getenv("MYSQL_PASSWORD"), database= os.getenv("MYSQL_DB"))
                my_cursor= conn.cursor()                                                            #creating cursor, helps to execute mysql query
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                            self.var_course.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_rollno.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phoneno.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio.get()
                                                                                                        ))
                conn.commit()
                self.Fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully", parent= self.root)
            except Exception as es:
                messagebox.showerror("ERROR", f"Due to: {str(es)}", parent= self.root)
    
    #FETCH DATA
    def Fetch_data(self):
        conn= mysql.connector.connect(host= os.getenv("MYSQL_HOST"), username= os.getenv("MYSQL_USER"), password= os.getenv("MYSQL_PASSWORD"), database= os.getenv("MYSQL_DB"))
        my_cursor= conn.cursor()
        my_cursor.execute("select * from student")
        data= my_cursor.fetchall()

        if len(data) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("", END, values= i)
            conn.commit()
        conn.close()

    #GET DATA OR CURSOR
    def Get_cursor(self, event= ""):
        Cursor_focus= self.Student_table.focus()
        content= self.Student_table.item(Cursor_focus)
        data= content["values"]

        self.var_course.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_section.set(data[2]),
        self.var_year.set(data[3]),
        self.var_id .set(data[4]),
        self.var_name.set(data[5]),
        self.var_rollno.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phoneno.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio.set(data[12]),


    #DELETE DATA
    def Delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("ERROR", "Student id must be required", parent= self.root)
        else:
            try:
                delete= messagebox.askyesno("DELETE", "Do you want to delete this student details ?", parent= self.root)
                if delete>0:
                    conn= mysql.connector.connect(host= os.getenv("MYSQL_HOST"), username= os.getenv("MYSQL_USER"), password= os.getenv("MYSQL_PASSWORD"), database= os.getenv("MYSQL_DB"))
                    my_cursor= conn.cursor()
                    sql= "delete from student where Id= %s"
                    val= (self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.Fetch_data()
                conn.close()   
                messagebox.showinfo("DELETED", "Successfully deleted student details", parent= self.root)
            except Exception as es:
                messagebox.showerror("ERROR", f"Due to: {str(es)}", parent= self.root)

    
    #RESET DATA
    def Reset_data(self):
        self.var_course.set("Select Course")
        self.var_dep.set("Select Department")
        self.var_section.set("Select Section")
        self.var_year.set("Select Year")
        self.var_id .set("")
        self.var_name.set("")
        self.var_rollno.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_radio.set("")
        


    #GENERATE DATASET OR TAKE PHOTO SAMPLE
    def Generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_course.get() == "Select Course" or self.var_section.get() == "":
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED", parent= self.root)
        else :
            try:
                conn= mysql.connector.connect(host= os.getenv("MYSQL_HOST"), username= os.getenv("MYSQL_USER"), password= os.getenv("MYSQL_PASSWORD"), database= os.getenv("MYSQL_DB"))
                my_cursor= conn.cursor()
                my_cursor.execute("select * from student")
                myResult= my_cursor.fetchall()
                id= 0
                for x in myResult:
                    id+=1
                my_cursor.execute("update student set Course=%s, Dep=%s, Sec=%s, Year=%s, Name=%s, RollNo=%s, Gender=%s, Email=%s, PhoneNo=%s, DOB=%s, Address=%s, `Photo Sample`=%s where Id=%s",(
                                                                                                            self.var_course.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_rollno.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phoneno.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio.get(),
                                                                                                            self.var_id.get()==id+1
                                                                                                        ))
                conn.commit()
                self.Fetch_data()
                conn.close()
                
                #LOADING FRONTAL FACE FROM OPEN CV
                Face_classifier= cv2.CascadeClassifier(r"C:\Users\Lenovo\Desktop\Codes\Mini Project 3rd SEM\haarcascade_frontalface_default.xml")
                def Face_crop(img):
                    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces= Face_classifier.detectMultiScale(gray, 1.3, 5)       #SCALING FACTOR= 1.3(BY DEFAULT), MINIMUM NEIGHBOUR= 5

                    for (x,y,w,h) in faces:
                        Face_crop= img[y:y+h, x:x+w]
                        return Face_crop
                    
                Capture= cv2.VideoCapture(0)
                Img_id= 0
                while True:
                    ret, My_frame= Capture.read()
                    if Face_crop(My_frame) is not None:
                        Img_id+=1
                        face= cv2.resize(Face_crop(My_frame), (450,450))
                        face= cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        File_path= r"C:\Users\Lenovo\Desktop\Codes\Mini Project 3rd SEM\dataset/user.{}.{}.jpg".format(self.var_id.get(), Img_id)
                        cv2.imwrite(File_path, face)
                        cv2.putText(face, str(Img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2) 
                        cv2.imshow("CROPED FACE", face)

                    if cv2.waitKey(1) == 13 or int(Img_id) == 50:
                        break
                Capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("RESULT", "Dataset Generated Succesfully!", parent=self.root)

            except Exception as es:
                messagebox.showerror("ERROR", f"Due to: {str(es)}", parent= self.root)



if __name__ == "__main__":  
    root = Tk()
    obj = Student_Details(root)
    root.mainloop()