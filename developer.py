from tkinter import*
from tkinter import ttk                                                       
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
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
        

        title_lbl = Label(bg_lbl, text = "DEVELOPER   DETAILS", font=("Times New Roman", 20, "bold"), bg = "white", fg = "#bd0d2f")
        title_lbl.place(x= -2, y= -2, width= 1200, height= 30)

        #CREATING FRAME
        main_frame = Frame(bg_lbl, bd = 2, bg= "white")
        main_frame.place(x= 285, y= 110, width= 600, height= 400)

        frame = LabelFrame(main_frame, bd=2, bg= "white", relief= RIDGE, text= "DETAILS", font=("Times New Roman", 12, "bold"))       
        frame.place(x= 8, y= 5, width= 577, height= 385)

        title_lbl = Label(frame, text = "******** WELCOME ********", font=("Times New Roman", 26, "bold"), bg = "white", fg = "#bd0d2f")
        title_lbl.place(x= 1, y= 30, width= 570, height= 30)
        
        title_lb2 = Label(frame, text = "Anmol Sati\n2021101\nB. Tech [CSE]\nSec D, Roll No 14\nGraphic Era University", font=("Times New Roman", 20, "bold"), bg = "white", fg = "#bd0d2f")
        title_lb2.place(x= 1, y= 90, width= 570, height= 170)

        title_lb3 = Label(frame, text = "******* THANK YOU *******", font=("Times New Roman", 26, "bold"), bg = "white", fg = "#bd0d2f")
        title_lb3.place(x= 1, y= 300, width= 570, height= 30)


if __name__ == "__main__":  
    root = Tk()
    obj = Developer(root)
    root.mainloop()