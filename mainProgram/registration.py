from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
from mysql.connector import cursor
from veza import Konekcija

class Registration:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Program")
        self.root.geometry("1850x1050+0+0")

        self.var_name=StringVar()
        self.var_lastname=StringVar()
        self.var_idcity=IntVar()
        self.var_address=StringVar()
        self.var_phone=IntVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_passwordCommit=StringVar()
        self.var_idsection=IntVar()
        self.var_idprofession=IntVar()

        self.var_check=IntVar()


        img1=Image.open(r"beachPhoto/beach3.jpg")
        img1=img1.resize((1850,1050),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblImage1=Label(self.root,image=self.photoimg1)
        lblImage1.place(x=0,y=0,relwidth=1,relheight=1)

        img2=Image.open(r"beachPhoto/beach4.jpg")
        img2=img2.resize((470,690),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblImage2=Label(self.root,image=self.photoimg2)
        lblImage2.place(x=320,y=130,width=470,height=690)

        frame=Frame(self.root,bg="white")
        frame.place(x=740,y=130,width=800,height=690)

        RegistrationLbl=Label(frame,text="Register here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        RegistrationLbl.place(x=20,y=20)

        nameLbl=Label(frame,text="Name",font=("times new roman",15,"bold"),bg="white")
        nameLbl.place(x=50,y=100)

        nameEntry=ttk.Entry(frame,textvariable=self.var_name, font=("times new roman",15,"bold"))
        nameEntry.place(x=50,y=130,width=250)

        lastnameLbl=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lastnameLbl.place(x=370,y=100)

        lastnameEntry=ttk.Entry(frame,textvariable=self.var_lastname, font=("times new roman",15,"bold"))
        lastnameEntry.place(x=370,y=130,width=250)

        idcityLbl=Label(frame,text="Id City",font=("times new roman",15,"bold"),fg="black",bg="white")
        idcityLbl.place(x=50,y=170)

        idcityEntry=ttk.Entry(frame,textvariable=self.var_idcity, font=("times new roman",15,"bold"))
        idcityEntry.place(x=50,y=200,width=250)

        addressLbl=Label(frame,text="Address",font=("times new roman",15,"bold"),fg="black",bg="white")
        addressLbl.place(x=370,y=170)

        addressEntry=ttk.Entry(frame,textvariable=self.var_address, font=("times new roman",15,"bold"))
        addressEntry.place(x=370,y=200,width=250)

        phoneLbl=Label(frame,text="Phone",font=("times new roman",15,"bold"),fg="black",bg="white")
        phoneLbl.place(x=50,y=240)

        phoneEntry=ttk.Entry(frame,textvariable=self.var_phone, font=("times new roman",15,"bold"))
        phoneEntry.place(x=50,y=270,width=250)

        emailLbl=Label(frame,text="E-mail",font=("times new roman",15,"bold"),fg="black",bg="white")
        emailLbl.place(x=370,y=240)

        emailEntry=ttk.Entry(frame,textvariable=self.var_email, font=("times new roman",15,"bold"))
        emailEntry.place(x=370,y=270,width=250)

        securityQLbl=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityQLbl.place(x=50,y=310)

        securityQcombo=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman",15,"bold"),state="readonly")
        securityQcombo['values']=("Biraj","Mesto rodjenja","Kućni ljubimac","ime bake")
        securityQcombo.place(x=50,y=340,width=250)
        securityQcombo.current()

        securityALbl=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityALbl.place(x=370,y=310)

        securityAEntry=ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman",15,"bold"))
        securityAEntry.place(x=370,y=340,width=250)

        passwordLbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        passwordLbl.place(x=50,y=370)

        passwordEntry=ttk.Entry(frame,textvariable=self.var_password, font=("times new roman",15,"bold"))
        passwordEntry.place(x=50,y=410,width=250)

        passwordCommitLbl=Label(frame,text="Commit password",font=("times new roman",15,"bold"),fg="black",bg="white")
        passwordCommitLbl.place(x=370,y=370)

        passwordCommitEntry=ttk.Entry(frame,textvariable=self.var_passwordCommit, font=("times new roman",15,"bold"))
        passwordCommitEntry.place(x=370,y=410,width=250)

        idsectionLbl=Label(frame,text="Id Section",font=("times new roman",15,"bold"),fg="black",bg="white")
        idsectionLbl.place(x=50,y=440)

        idsectionEntry=ttk.Entry(frame,textvariable=self.var_idsection, font=("times new roman",15,"bold"))
        idsectionEntry.place(x=50,y=480,width=250)

        idprofessionLbl=Label(frame,text="Id Profession",font=("times new roman",15,"bold"),fg="black",bg="white")
        idprofessionLbl.place(x=370,y=440)

        idprofessionEntry=ttk.Entry(frame,textvariable=self.var_idprofession, font=("times new roman",15,"bold"))
        idprofessionEntry.place(x=370,y=480,width=250)

        btnCheck=Checkbutton(frame,variable=self.var_check, text="I accept the terms ",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        btnCheck.place(x=50,y=540)

        img3=Image.open(r"userLoginPhoto/register2.png")
        img3=img3.resize((200,50),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimg3,command=self.registration_data, borderwidth=0,cursor="hand2")
        b1.place(x=70,y=580,width=200)

        img4=Image.open(r"userLoginPhoto/login1.png")
        img4=img4.resize((200,50),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b2=Button(frame,image=self.photoimg4,command=self.backToLogIn, borderwidth=0,cursor="hand2")
        b2.place(x=390,y=580,width=200)


    def registration_data(self):
        if self.var_name.get()=="" or self.var_lastname.get()=="" or self.var_idcity.get()==0 or self.var_address.get()=="" or self.var_phone.get()==0 or self.var_email.get()=="" or self.var_securityQ.get()=="Biraj" or self.var_securityA.get()=="" or self.var_password.get()=="" or self.var_passwordCommit.get()=="" or self.var_idsection.get()==0 or self.var_idprofession.get()==0:
            messagebox.showerror("Error","All fields must be filled!")
        elif self.var_password.get()!= self.var_passwordCommit.get():
            messagebox.showerror("Error","Commit password and password are not the same!")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please,accept the terms")
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            query=("SELECT * FROM zaposleni WHERE email=%s")
            value=(self.var_email.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Wrong password,try again")
            else:
                cursor.execute("INSERT INTO zaposleni(ime,prezime,idgrad,adresa,telefon,email,security_question,security_answer,lozinka,idodeljenje,idzanimanje) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.var_name.get(),
            self.var_lastname.get(),
            self.var_idcity.get(),
            self.var_address.get(),
            self.var_phone.get(),
            self.var_email.get(),
            self.var_securityQ.get(),
            self.var_securityA.get(),
            self.var_password.get(),
            self.var_idsection.get(),
            self.var_idprofession.get(),
                ))
                con.commit()
                messagebox.showinfo("Success","Registration  is successful ")

    def backToLogIn(self):
        self.root.destroy()


'''root=Tk()
object=Registration(root)
mainloop()'''