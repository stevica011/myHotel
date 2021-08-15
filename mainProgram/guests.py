from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from vipGuest import GuestPrediction
from veza import Konekcija

class Guests:
    def __init__(self,root):
        self.root=root
        self.root.title("   ")
        self.root.geometry("1620x770+307+300")


        self.var_idguest=IntVar()
        x=random.randint(1000,4999)
        self.var_idguest.set(int(x))
        self.var_name=StringVar()
        self.var_lastname=StringVar()
        self.var_gender=StringVar()
        self.var_years=IntVar()
        self.var_phone=IntVar()
        self.var_email=StringVar()
        self.var_idnumber=IntVar()
        self.var_iddocument=IntVar()
        self.var_reservationnumber=IntVar()
        self.var_points=IntVar()
        self.var_rezident=StringVar()
        self.var_vipguest=IntVar()

        self.SearchBy=StringVar()
        self.SearchText=StringVar()



        lbl_title=Label(self.root,text="Guest Base",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1620,height=50)

        img1=Image.open(r"hotelsPhoto/hotel.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=5,y=2,width=100,height=40)

        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Guest details",font=("times new roman",12,"bold"),padx=2)
        labelFrameLeft.place(x=5,y=50,width=542,height=530)

        idguestLbl=Label(labelFrameLeft,text="ID guest",font=("times new roman",14,"bold"),padx=2,pady=6)
        idguestLbl.grid(row=0,column=0,sticky=W)

        idguestEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_idguest,font=("times new roman",14,"bold"),width=20,state="readonly")
        idguestEntry.grid(row=0,column=1)

        nameLbl=Label(labelFrameLeft,text="Name",font=("times new roman",14,"bold"),padx=2,pady=6)
        nameLbl.grid(row=1,column=0,sticky=W)

        nameEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_name, font=("times new roman",14,"bold"),width=20)
        nameEntry.grid(row=1,column=1,padx=30)

        btnML=Button(labelFrameLeft,text="Prediction",command=self.prediction, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        btnML.grid(row=1,column=2,padx=1)

        lastnameLbl=Label(labelFrameLeft,text="Lastname",font=("times new roman",14,"bold"),padx=2,pady=6)
        lastnameLbl.grid(row=2,column=0,sticky=W)

        lastnameEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_lastname, font=("times new roman",14,"bold"),width=20)
        lastnameEntry.grid(row=2,column=1)

        genderLbl=Label(labelFrameLeft,text="Gender",font=("times new roman",14,"bold"),padx=2,pady=6)
        genderLbl.grid(row=3,column=0,sticky=W)

        genderCombo=ttk.Combobox(labelFrameLeft,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=18,state="readonly")
        genderCombo.current()
        genderCombo['value']=("Muški","Ženski")
        genderCombo.grid(row=3,column=1,padx=1)

        yearsLbl=Label(labelFrameLeft,text="Years",font=("times new roman",14,"bold"),padx=2,pady=6)
        yearsLbl.grid(row=4,column=0,sticky=W)

        yearsEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_years, font=("times new roman",14,"bold"),width=20)
        yearsEntry.grid(row=4,column=1)

        phoneLbl=Label(labelFrameLeft,text="Phone",font=("times new roman",14,"bold"),padx=2,pady=6)
        phoneLbl.grid(row=5,column=0,sticky=W)

        phoneEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_phone, font=("times new roman",14,"bold"),width=20)
        phoneEntry.grid(row=5,column=1)

        emailLbl=Label(labelFrameLeft,text="Email",font=("times new roman",14,"bold"),padx=2,pady=6)
        emailLbl.grid(row=6,column=0,sticky=W)

        emailEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_email, font=("times new roman",14,"bold"),width=20)
        emailEntry.grid(row=6,column=1)

        idnumberLbl=Label(labelFrameLeft,text="Id number",font=("times new roman",14,"bold"),padx=2,pady=6)
        idnumberLbl.grid(row=7,column=0,sticky=W)

        idnumberEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_idnumber, font=("times new roman",14,"bold"),width=20)
        idnumberEntry.grid(row=7,column=1)

        iddocumentLbl=Label(labelFrameLeft,text="Document",font=("times new roman",14,"bold"),padx=2,pady=6)
        iddocumentLbl.grid(row=8,column=0,sticky=W)

        iddocumentCombo=ttk.Combobox(labelFrameLeft,textvariable=self.var_iddocument,font=("times new roman",13,"bold"),width=18,state="readonly")
        iddocumentCombo.current()
        iddocumentCombo['value']=(1,2,3)
        iddocumentCombo.grid(row=8,column=1,padx=1)

        reservationnumberLbl=Label(labelFrameLeft,text="Number of reservation",font=("times new roman",14,"bold"),padx=2,pady=6)
        reservationnumberLbl.grid(row=9,column=0,sticky=W)

        reservationnumberEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_reservationnumber, font=("times new roman",14,"bold"),width=20)
        reservationnumberEntry.grid(row=9,column=1)

        pointsLbl=Label(labelFrameLeft,text="Points",font=("times new roman",14,"bold"),padx=2,pady=6)
        pointsLbl.grid(row=10,column=0,sticky=W)

        pointsEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_points, font=("times new roman",14,"bold"),width=20)
        pointsEntry.grid(row=10,column=1)

        btnML2=Button(labelFrameLeft,text="Status change",command=self.guestStatus, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnML2.grid(row=10,column=2,padx=1)

        rezidentLbl=Label(labelFrameLeft,text="Rezident",font=("times new roman",14,"bold"),padx=2,pady=6)
        rezidentLbl.grid(row=11,column=0,sticky=W)

        rezidentEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_rezident, font=("times new roman",14,"bold"),width=20)
        rezidentEntry.grid(row=11,column=1)

        vipguestLbl=Label(labelFrameLeft,text="VIP guest",font=("times new roman",14,"bold"),padx=2,pady=6)
        vipguestLbl.grid(row=12,column=0,sticky=W)

        vipguestEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_vipguest, font=("times new roman",14,"bold"),width=20)
        vipguestEntry.grid(row=12,column=1)

        btnFrame=Frame(labelFrameLeft)
        btnFrame.place(x=0,y=470,width=448,height=36)

        btnRegister=Button(btnFrame,text="Register",command=self.register, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnRegister.grid(row=0,column=0,padx=1)

        btnChange=Button(btnFrame,text="Change",command=self.change, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnChange.grid(row=0,column=1,padx=1)

        btnDelete=Button(btnFrame,text="Delete",command=self.delete, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btnFrame,text="Reset",command=self.reset, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)


        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Look and find the details about guests",font=("times new roman",12,"bold"),padx=2)
        TableFrame.place(x=545,y=50,width=1070,height=530)

        lblSearch=Label(TableFrame,text="Search by:",font=("times new roman",15,"bold"),bg="gold",fg="black")
        lblSearch.grid(row=0,column=0,sticky=W)

        
        comboSearch=ttk.Combobox(TableFrame,textvariable=self.SearchBy,font=("times new roman",15,"bold"),width=24,state="readonly")
        comboSearch['value']=("ime","prezime")
        comboSearch.current()
        comboSearch.grid(row=0,column=1,padx=2)

        tekstSearch=ttk.Entry(TableFrame,textvariable=self.SearchText, font=("times new roman",15,"bold"),width=24)
        tekstSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(TableFrame,text="Search",command=self.Search, font=("times new roman",15,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(TableFrame,text="Show All",command=self.showGuests, font=("times new roman",15,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)


        detailsTable=Frame(TableFrame,bd=2,relief=RIDGE)
        detailsTable.place(x=0,y=50,width=1070,height=460)

        scrollX=ttk.Scrollbar(detailsTable,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detailsTable,orient=VERTICAL)

        self.detailsTable=ttk.Treeview(detailsTable,columns=("idguest","name","lastname","gender","years","phone","email","idnumber","iddocument","reservationnumber","points","rezident","vipguest"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command=self.detailsTable.xview)
        scrollY.config(command=self.detailsTable.yview)

        self.detailsTable.heading("idguest",text="ID gosta")
        self.detailsTable.heading("name",text="Name")
        self.detailsTable.heading("lastname",text="Lastname")
        self.detailsTable.heading("gender",text="Gender")
        self.detailsTable.heading("years",text="Years")
        self.detailsTable.heading("phone",text="Phone")
        self.detailsTable.heading("email",text="Email")
        self.detailsTable.heading("idnumber",text="Doc. number.")
        self.detailsTable.heading("iddocument",text="ID doc.")
        self.detailsTable.heading("reservationnumber",text="Res. number")
        self.detailsTable.heading("points",text="Points")
        self.detailsTable.heading("rezident",text="Rezident")
        self.detailsTable.heading("vipguest",text="VIP")
        self.detailsTable['show']="headings"
        self.detailsTable.column("idguest",width=100)
        self.detailsTable.column("name",width=100)
        self.detailsTable.column("lastname",width=100)
        self.detailsTable.column("gender",width=100)
        self.detailsTable.column("years",width=100)
        self.detailsTable.column("phone",width=100)
        self.detailsTable.column("email",width=100)
        self.detailsTable.column("idnumber",width=100)
        self.detailsTable.column("iddocument",width=100)
        self.detailsTable.column("reservationnumber",width=100)
        self.detailsTable.column("points",width=100)
        self.detailsTable.column("rezident",width=100)
        self.detailsTable.column("vipguest",width=100)
        

        self.detailsTable.pack(fill=BOTH,expand=1)
        self.detailsTable.bind("<ButtonRelease-1>",self.get_data)


        img2=Image.open(r"hotelsPhoto/hotel.jpg")
        img2=img2.resize((1620,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=0,y=577,width=1620,height=200)


    def register(self):
        if self.var_idguest.get()==0 or self.var_name.get()=="" or self.var_lastname.get()=="" or self.var_gender.get()=="" or self.var_years.get()==0 or self.var_phone.get()==0 or self.var_email.get()=="" or self.var_idnumber.get()==0 or self.var_iddocument.get()==0 or self.var_rezident.get()=="":
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                con=Konekcija.getInstance()
                cursor=con.cursor()
                cursor.execute("INSERT INTO gosti VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.var_idguest.get(),
            self.var_name.get(),
            self.var_lastname.get(),
            self.var_gender.get(),
            self.var_years.get(),
            self.var_phone.get(),
            self.var_email.get(),
            self.var_idnumber.get(),
            self.var_iddocument.get(),
            self.var_reservationnumber.get(),
            self.var_points.get(),
            self.var_rezident.get(),
            self.var_vipguest.get()))
                con.commit()
                messagebox.showinfo("Success","Guest added successfully",parent=self.root)
                self.reset()
                self.showGuests()
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{es}",parent=self.root)

    def change(self):
        if self.var_idguest.get()==0:
            messagebox.showerror("Error","Please,enter ID of guest",parent=self.root)
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE gosti SET telefon=%s,email=%s WHERE idgosti=%s",(
                self.var_phone.get(),
                self.var_email.get(),
                self.var_idguest.get()
            ))
            con.commit()
            messagebox.showinfo("Success","Guest's data changed successfully",parent=self.root)
            self.reset()
            self.showGuests()

    def guestStatus(self):
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE gosti SET počasnigost=4 WHERE bodovi<1000")
            cursor.execute("UPDATE gosti SET počasnigost=3 WHERE bodovi>1000 and bodovi<2000" )
            cursor.execute("UPDATE gosti SET počasnigost=2 WHERE bodovi>2000 and bodovi<4000")
            cursor.execute("UPDATE gosti SET počasnigost=1 WHERE bodovi>4000")
            con.commit()
            messagebox.showinfo("Success","New guests status",parent=self.root)
            self.reset()
            self.showGuests()
            
    def delete(self):
        delete=messagebox.askyesno("Hotel System Management","Do You really want to delete this guest?")
        if delete>0:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            query=("DELETE FROM gosti WHERE idgosti=%s")
            value=(self.var_idguest.get(),)
            cursor.execute(query,value)
        elif  not delete:
            return
        con.commit()
        messagebox.showinfo("OK","Guests data deleted successfully",parent=self.root)
        self.reset()
        self.showGuests()
        

    def reset(self):
        self.var_name.set("")
        self.var_lastname.set("")
        self.var_gender.set("")
        self.var_years.set(0)
        self.var_phone.set(0)
        self.var_email.set("")
        self.var_idnumber.set(0)
        self.var_iddocument.set(0)
        self.var_reservationnumber.set(0)
        self.var_points.set(0)
        self.var_rezident.set("")
        self.var_vipguest.set(0)
        x=random.randint(1000,9999)
        self.var_idguest.set(str(x))
        self.detailsTable.delete(*self.detailsTable.get_children())


    def Search(self): 
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM gosti WHERE "+str(self.SearchBy.get())+" like binary '%"+self.SearchText.get()+"%'") 
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.detailsTable.delete(*self.detailsTable.get_children())
            for i in rows: 
                self.detailsTable.insert('',END,values=i)
                con.commit()
        else:
            self.detailsTable.delete(*self.detailsTable.get_children()) 

    def showGuests(self):
        con=Konekcija.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM gosti")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.detailsTable.delete(*self.detailsTable.get_children())
            for i in rows:
                self.detailsTable.insert("",END,values=i)
        con.commit()

    
    def get_data(self,event=""):
        cursor_row=self.detailsTable.focus()
        content=self.detailsTable.item(cursor_row)
        row=content['values']

        self.var_idguest.set(row[0]),
        self.var_name.set(row[1]),
        self.var_lastname.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_years.set(row[4]),
        self.var_phone.set(row[5]),
        self.var_email.set(row[6]),
        self.var_idnumber.set(row[7]),
        self.var_iddocument.set(row[8]),
        self.var_reservationnumber.set(row[9])
        self.var_points.set(row[10])
        self.var_rezident.set(row[11])
        self.var_vipguest.set(row[12])
        

    def prediction(self):
        self.new_window=Toplevel(self.root)
        self.app=GuestPrediction(self.new_window)



'''root=Tk()
object=Guests(root)
mainloop()'''