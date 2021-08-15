from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
from datetime import date, datetime
import datetime
from time import strftime 
from guests import Guests
from roomReservation import RoomReservation
from rooms import RoomDetails
from restaurant import Restaurant
from staff import Staff
from veza import Konekcija


class Hotel:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Menadžment")
        self.root.geometry("1850x1050+0+0")
    

        img1=Image.open(r"hotelsPhoto/hotel.jpg")
        img1=img1.resize((1850,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=0,y=0,width=1850,height=140)

        img2=Image.open(r"hotelsPhoto/hotel4.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=0,y=0,width=230,height=140)

        titleLbl=Label(self.root,text="Hotel Management",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        titleLbl.place(x=0,y=140,width=1850,height=70)

        self.lbl = Label(self.root, font = ('calibri', 15, 'bold'),
        foreground = 'gold',background="black")
        self.lbl.place(x=10,y=160,width=300)
        self.date()

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=210,width=1850,height=850)

        listaLbl=Label(main_frame,text="LIST",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        listaLbl.place(x=0,y=0,width=230)

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=45,width=228,height=220)

        btn1=Button(btn_frame,text="GUESTS",command=self.guestDetails,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        btn1.grid(row=0,column=0,pady=1)
        btn2=Button(btn_frame,text="RESERVATION",command=self.check,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        btn2.grid(row=1,column=0,pady=1)
        btn3=Button(btn_frame,text="ROOMS",command=self.rooms, width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        btn3.grid(row=2,column=0,pady=1)
        btn4=Button(btn_frame,text="RESTAURANT",command=self.check2, width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        btn4.grid(row=3,column=0,pady=1)
        btn5=Button(btn_frame,text="STAFF",command=self.staff, width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        btn5.grid(row=4,column=0,pady=1)
        btn6=Button(btn_frame,text="SIGN OUT",command=self.signOut, width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        btn6.grid(row=5,column=0,pady=1)


        img3=Image.open(r"hotelsPhoto/hotel3.jpg")
        img3=img3.resize((1620,800),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblImage3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblImage3.place(x=225,y=0,width=1620,height=800)

        img4=Image.open(r"hotelsPhoto/hotel2.jpg")
        img4=img4.resize((228,290),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblImage4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblImage4.place(x=0,y=265,width=228,height=290)

        img5=Image.open(r"hotelsPhoto/hotel5.jpg")
        img5=img5.resize((228,290),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblImage5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblImage5.place(x=0,y=520,width=228,height=280)


    def date(self):
        now = strftime("%Y-%m-%d %H:%M:%S")
        self.lbl.config(text = now)
        self.lbl.after(1000, self.date)


    def guestDetails(self):
        self.new_window=Toplevel(self.root)
        self.app=Guests(self.new_window)

    def roomReservation(self):
        self.new_window2=Toplevel(self.root)
        self.app=RoomReservation(self.new_window2)

    def rooms(self):
        self.new_window3=Toplevel(self.root)
        self.app=RoomDetails(self.new_window3)

    def staff(self):
        self.new_window5=Toplevel(self.root)
        self.app=Staff(self.new_window5)
    
    def billRestaurant(self):
        self.new_window6=Toplevel(self.root)
        self.app=Restaurant(self.new_window6)


    def check(self):
        self.root2 = Toplevel()
        self.root2.title("   ")
        self.root2.geometry("228x220+0+285")

        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_idsection=IntVar()

        frame=Frame(self.root2,bd=2,bg="black")
        frame.place(x=10,y=0,width=228,height=220)

        titleLbl = Label(frame, text="Log In", font=("times new roman", 13, "bold"), fg="white", bg="black")
        titleLbl.place(x=0, y=0)

        emailLbl = Label(frame, text="E-mail", font=("times new roman", 12, "bold"), fg="white", bg="black")
        emailLbl.place(x=10, y=40)

        textEmail = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 12, "bold"))
        textEmail.place(x=30, y=70, width=110)

        passwordLbl = Label(frame, text="Password", font=("times new roman", 12, "bold"), fg="white", bg="black")
        passwordLbl.place(x=10, y=100)

        textpassword = ttk.Entry(frame, textvariable=self.var_password, show="*", font=("times new roman", 12, "bold"))
        textpassword.place(x=30, y=130, width=110)

        sectionLbl = Label(frame, text="Section", font=("times new roman", 12, "bold"), fg="white", bg="black")
        sectionLbl.place(x=10, y=160)

        textsection = ttk.Entry(frame, textvariable=self.var_idsection, font=("times new roman", 12, "bold"))
        textsection.place(x=30, y=190, width=50)

        btnDodajLog=Button(frame,text="Log in",command=self.log, font=("times new roman",10,"bold"),bg="black",fg="gold",width=7)
        btnDodajLog.place(x=110,y=180)

    def log(self):
        from veza2 import Konekcija2
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT email,lozinka,idodeljenje FROM zaposleni WHERE email=%s", (
            self.var_email.get(),
        ))
        kolone = cursor.fetchall()
        for kolona in kolone:
            if kolona[1]!=self.var_password.get():
                messagebox.showerror("Error","Wrong password")
            elif  kolona[2]!=self.var_idsection.get():
                messagebox.showerror("Error","Wrong section")
            else:
                if kolona[2]==3 or kolona[2]==1:
                    self.roomReservation()
                    self.root2.destroy()
                else:
                    messagebox.showerror("Error","Non-existent section")
            con.commit()

    def check2(self):
        self.root2 = Toplevel()
        self.root2.title("   ")
        self.root2.geometry("228x220+0+285")

        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_idsection=IntVar()

        frame=Frame(self.root2,bd=2,bg="black")
        frame.place(x=10,y=0,width=228,height=220)

        titleLbl = Label(frame, text="Log In", font=("times new roman", 13, "bold"), fg="white", bg="black")
        titleLbl.place(x=0, y=0)

        emailLbl = Label(frame, text="E-mail", font=("times new roman", 12, "bold"), fg="white", bg="black")
        emailLbl.place(x=10, y=40)

        textEmail = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 12, "bold"))
        textEmail.place(x=30, y=70, width=110)

        passwordLbl = Label(frame, text="Password", font=("times new roman", 12, "bold"), fg="white", bg="black")
        passwordLbl.place(x=10, y=100)

        textpassword = ttk.Entry(frame, textvariable=self.var_password, show="*", font=("times new roman", 12, "bold"))
        textpassword.place(x=30, y=130, width=110)

        sectionLbl = Label(frame, text="Section", font=("times new roman", 12, "bold"), fg="white", bg="black")
        sectionLbl.place(x=10, y=160)

        textsection = ttk.Entry(frame, textvariable=self.var_idsection, font=("times new roman", 12, "bold"))
        textsection.place(x=30, y=190, width=50)

        btnDodajLog=Button(frame,text="Log in",command=self.log2, font=("times new roman",10,"bold"),bg="black",fg="gold",width=7)
        btnDodajLog.place(x=110,y=180)

    def log2(self):
        con=Konekcija.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT email,lozinka,idodeljenje FROM zaposleni WHERE email=%s", (
            self.var_email.get(),
        ))
        kolone = cursor.fetchall()
        for kolona in kolone:
            if kolona[1]!=self.var_password.get():
                messagebox.showerror("Error","Wrong password")
            elif  kolona[2]!=self.var_idsection.get():
                messagebox.showerror("Error","Wrong section")
            else:
                if kolona[2]==4 or kolona[2]==1:
                    self.billRestaurant()
                    self.root2.destroy()
                else:
                    messagebox.showerror("Error","Non-existent section")
            con.commit()


    def signOut(self):
        response=messagebox.askyesno('Exit','Are you sure yo want to exit?',parent=self.root)
        if response:
            self.root.destroy()

    


'''root=Tk()
object=Hotel(root)
mainloop()'''