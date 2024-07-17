from tkinter import*
from tkinter import ttk              
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recog:
    def __init__(self, root):       
        self.root = root            
        self.root.geometry("1200x680+0+0")
        self.root.title("ATTENDANCE AUTOMATION SYSTEM")

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
        
        title_lbl = Label(bg_lbl, text = "FACE  DETECTOR", font=("Times New Roman", 20, "bold"), bg = "white", fg = "#bd0d2f")
        title_lbl.place(x= -2, y= -2, width= 1200, height= 30)

        #CREATING FRAME
        main_frame = Frame(bg_lbl, bd = 2, bg= "white")
        main_frame.place(x= 285, y= 110, width= 600, height= 400)

        frame = LabelFrame(main_frame, bd=2, bg= "white", relief= RIDGE, text= "FACE DETECTOR", font=("Times New Roman", 12, "bold"))         
        frame.place(x= 8, y= 5, width= 577, height= 385)

        title_lbl = Label(frame, text = "******** WELCOME ********", font=("Times New Roman", 26, "bold"), bg = "white", fg = "#bd0d2f")
        title_lbl.place(x= 1, y= 30, width= 570, height= 30)
        
        title_lb2 = Label(frame, text = "Your face will be detected by clicking\non the button given below.", font=("Times New Roman", 17, "bold"), bg = "white", fg = "#bd0d2f")
        title_lb2.place(x= 1, y= 110, width= 570, height= 50)

        button = Button(frame, text= "DETECT", cursor= "hand2", command=self.Recog_Data, font=("Times New Roman", 25, "bold"), bg = "#FFD3D3", fg = "#bd0d2f")
        button.place(x= 170, y= 180, width= 230, height= 50)

        title_lb3 = Label(frame, text = "******* THANK YOU *******", font=("Times New Roman", 26, "bold"), bg = "white", fg = "#bd0d2f")
        title_lb3.place(x= 1, y= 300, width= 570, height= 30)


    #ATTENDANCE
    def Attendance(self, c, d, s, i, r, n):
        with open(r"attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            ID_list = [line.split(",")[3].strip() for line in myDataList if len(line.split(",")) > 3]  
            
            # Check if the student ID is not present
            if i not in ID_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{c}, {d}, {s}, {i}, {r}, {n}, {d1}, {dstring}, PRESENT")


    #FACE RECOGNIZATION
    def Recog_Data(self):
        def Draw_Boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            Gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(Gray_img, scaleFactor, minNeighbors)

            coord= []
            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                id, predict= clf.predict(Gray_img[y:y+h, x:x+w])
                confidence= int((100*(1-predict/300)))

                conn= mysql.connector.connect(host= os.getenv("MYSQL_HOST"), username= os.getenv("MYSQL_USER"), password= os.getenv("MYSQL_PASSWORD"), database= os.getenv("MYSQL_DB"))
                my_cursor= conn.cursor()

                my_cursor.execute("select Name from student where Id=" + str(id))
                n = my_cursor.fetchone()

                my_cursor.execute("select RollNo from student where Id=" + str(id))
                r = my_cursor.fetchone()

                my_cursor.execute("select Course from student where Id=" + str(id))
                c = my_cursor.fetchone()

                my_cursor.execute("select Dep from student where Id=" + str(id))
                d = my_cursor.fetchone()

                my_cursor.execute("select Id from student where Id=" + str(id))
                i = my_cursor.fetchone()

                my_cursor.execute("select Sec from student where Id=" + str(id))
                s = my_cursor.fetchone()

                # Check if any of the fetched values is None before using join
                if None not in (n, r, c, d, i, s):
                    n = "+".join(n)
                    r = "+".join(r)
                    c = "+".join(c)
                    d = "+".join(d)
                    i = "+".join(i)
                    s = "+".join(s)

                    if confidence>80:
                        cv2.putText(img, f"Name:{n}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 3)
                        cv2.putText(img, f"Roll No:{r}", (x,y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 3)
                        self.Attendance(c, d, s, i, r, n)
                    else:
                        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
                        cv2.putText(img, "UNKNOWN", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 3)

                coord= [x,y,w,h]
            
            return coord
        
        def Recog(img, clf, faceCascade):
            coord= Draw_Boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade= cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"classifier.xml")

        Video_cap= cv2.VideoCapture(0)
        while True:
            ret, img= Video_cap.read()
            img= Recog(img, clf, faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNIZATION", img)
            
            if cv2.waitKey(1) == 13:
                break
        Video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":               
    root = Tk()
    obj = Face_Recog(root)
    root.mainloop()