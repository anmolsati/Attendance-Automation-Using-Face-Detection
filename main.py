from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from st_details import Student_Details
from train import Train
from faceRecog import Face_Recog
from developer import Developer
from help import Help
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class Face_Recog_System:
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
        

        title_lbl = Label(bg_lbl, text = "ATTENDANCE  AUTOMATION  SOFTWARE", font=("Times New Roman", 20, "bold"), bg = "white", fg = "#bd0d2f")
        title_lbl.place(x= -2, y= -2, width= 1200, height= 30)
        
        #student button
        img_3 = Image.open(r"button_1.png")
        img_3 = img_3.resize((150, 120), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        button_1 = Button(bg_lbl, image= self.photoimg_3, command= self.Stuuu, cursor= "hand2")
        button_1.place(x= 310, y= 170, width= 150, height= 120)

        button_1_1 = Button(bg_lbl, text= "Student Details", cursor= "hand2", command= self.Stuuu, font=("Times New Roman", 15, "bold"), bg = "#FFD3D3", fg = "#bd0d2f")
        button_1_1.place(x= 310, y= 280, width= 150, height= 40)
        

        #face detection button
        img_4 = Image.open(r"button_2.png")
        img_4 = img_4.resize((150, 120), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        button_1 = Button(bg_lbl, image= self.photoimg_4, command= self.Faceee, cursor= "hand2")
        button_1.place(x= 520, y= 170, width= 150, height= 120)
        button_1_1 = Button(bg_lbl, text= "Face Detector", cursor= "hand2", command= self.Faceee, font=("Times New Roman", 15, "bold"), bg = "#FFD3D3", fg = "#bd0d2f")
        button_1_1.place(x= 520, y= 280, width= 150, height= 40)


        #train data button
        img_6 = Image.open(r"button_4.png")
        img_6 = img_6.resize((150, 120), Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        button_1 = Button(bg_lbl, image= self.photoimg_6, cursor= "hand2", command= self.Trainnn)
        button_1.place(x= 710, y= 170, width= 150, height= 120)
        button_1_1 = Button(bg_lbl, text= "Train Data", cursor= "hand2", command= self.Trainnn, font=("Times New Roman", 15, "bold"), bg = "#FFD3D3", fg = "#bd0d2f")
        button_1_1.place(x= 710, y= 280, width= 150, height= 40)
        

        #developer button
        img_8 = Image.open(r"button_6.png")
        img_8 = img_8.resize((150, 120), Image.ANTIALIAS)
        self.photoimg_8 = ImageTk.PhotoImage(img_8)

        button_1 = Button(bg_lbl, image= self.photoimg_8, cursor= "hand2")
        button_1.place(x= 310, y= 360, width= 150, height= 120)
        button_1_1 = Button(bg_lbl, text= "Developer", cursor= "hand2", command= self.Devppp, font=("Times New Roman", 15, "bold"), bg = "#FFD3D3", fg = "#bd0d2f")
        button_1_1.place(x= 310, y= 470, width= 150, height= 40)

        #help desk button
        img_9 = Image.open(r"button_7.png")
        img_9 = img_9.resize((150, 120), Image.ANTIALIAS)
        self.photoimg_9 = ImageTk.PhotoImage(img_9)

        button_1 = Button(bg_lbl, image= self.photoimg_9, cursor= "hand2")
        button_1.place(x= 520, y= 360, width= 150, height= 120)
        button_1_1 = Button(bg_lbl, text= "Help Desk", cursor= "hand2", command= self.Helppp, font=("Times New Roman", 15, "bold"), bg = "#FFD3D3", fg = "#bd0d2f")
        button_1_1.place(x= 520, y= 470, width= 150, height= 40)

        #exit button
        img_10 = Image.open(r"button_8.png")
        img_10 = img_10.resize((150, 120), Image.ANTIALIAS)
        self.photoimg_10 = ImageTk.PhotoImage(img_10)

        button_1 = Button(bg_lbl, image= self.photoimg_10, cursor= "hand2")
        button_1.place(x= 710, y= 360, width= 150, height= 120)
        button_1_1 = Button(bg_lbl, text= "Exit", cursor= "hand2", command= self.Exittt, font=("Times New Roman", 15, "bold"), bg = "#FFD3D3", fg = "#bd0d2f")
        button_1_1.place(x= 710, y= 470, width= 150, height= 40)


    def Stuuu(self): 
        self.new_window= Toplevel(self.root)
        self.app= Student_Details(self.new_window)

    def Trainnn(self): 
        self.new_window= Toplevel(self.root)
        self.app= Train(self.new_window)

    def Faceee(self): 
        self.new_window= Toplevel(self.root)
        self.app= Face_Recog(self.new_window)

    def Devppp(self): 
        self.new_window= Toplevel(self.root)
        self.app= Developer(self.new_window)

    def Helppp(self): 
        self.new_window= Toplevel(self.root)
        self.app= Help(self.new_window)

    def Exittt(self): 
        self.Exittt= messagebox.askyesno("EXIT", "Are you sure you want to exit ?")
        if self.Exittt > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recog_System(root)
    root.mainloop()