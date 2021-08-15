from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from veza import Konekcija

class Staff:
    def __init__(self,root):
        self.root=root
        self.root.title("   ")
        self.root.geometry("1620x770+307+300")

        self.var_idstaff=IntVar()
        self.var_name=StringVar()
        self.var_lastname=StringVar()
        self.var_idcity=IntVar()
        self.var_address=StringVar()
        self.var_phone=IntVar()
        self.var_email=StringVar()
        self.var_idsection=IntVar()
        self.var_idprofession=IntVar()

        self.var_searchBy=StringVar()
        self.var_searchText=StringVar()


        titleLbl=Label(self.root,text="Staff",font=("times new roman",25,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        titleLbl.place(x=0,y=0,width=1620,height=50)

        img1=Image.open(r"hotelsPhoto/hotel.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=5,y=2,width=100,height=40)

        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Staff Details",font=("times new roman",12,"bold"),padx=2)
        labelFrameLeft.place(x=5,y=50,width=525,height=490)

        idstaffLbl=Label(labelFrameLeft,text="Id Staff",font=("times new roman",14,"bold"),padx=2,pady=6)
        idstaffLbl.grid(row=0,column=0,sticky=W)

        idstaffEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_idstaff,font=("times new roman",14,"bold"),width=35,state="readonly")
        idstaffEntry.grid(row=0,column=1)

        nameLbl=Label(labelFrameLeft,text="Name",font=("times new roman",14,"bold"),padx=2,pady=6)
        nameLbl.grid(row=1,column=0,sticky=W)

        nameEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_name, font=("times new roman",14,"bold"),width=35)
        nameEntry.grid(row=1,column=1)

        lastnameLbl=Label(labelFrameLeft,text="Last Name",font=("times new roman",14,"bold"),padx=2,pady=6)
        lastnameLbl.grid(row=2,column=0,sticky=W)

        lastnameEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_lastname, font=("times new roman",14,"bold"),width=35)
        lastnameEntry.grid(row=2,column=1)

        idcityLbl=Label(labelFrameLeft,text="Id city",font=("times new roman",14,"bold"),padx=2,pady=6)
        idcityLbl.grid(row=3,column=0,sticky=W)

        idcityEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_idcity, font=("times new roman",14,"bold"),width=35)
        idcityEntry.grid(row=3,column=1)

        addressLbl=Label(labelFrameLeft,text="Address",font=("times new roman",14,"bold"),padx=2,pady=6)
        addressLbl.grid(row=4,column=0,sticky=W)

        addressEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_address, font=("times new roman",14,"bold"),width=35)
        addressEntry.grid(row=4,column=1)

        phoneLbl=Label(labelFrameLeft,text="Phone",font=("times new roman",14,"bold"),padx=2,pady=6)
        phoneLbl.grid(row=5,column=0,sticky=W)

        phoneEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_phone, font=("times new roman",14,"bold"),width=35)
        phoneEntry.grid(row=5,column=1)

        emailLbl=Label(labelFrameLeft,text="Email",font=("times new roman",14,"bold"),padx=2,pady=6)
        emailLbl.grid(row=6,column=0,sticky=W)

        emailEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_email, font=("times new roman",14,"bold"),width=35)
        emailEntry.grid(row=6,column=1)

        idsectionLbl=Label(labelFrameLeft,text="Id Section",font=("times new roman",14,"bold"),padx=2,pady=6)
        idsectionLbl.grid(row=7,column=0,sticky=W)

        idsectionEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_idsection, font=("times new roman",14,"bold"),width=35)
        idsectionEntry.grid(row=7,column=1)

        idproffesionLbl=Label(labelFrameLeft,text="Proffesion",font=("times new roman",14,"bold"),padx=2,pady=6)
        idproffesionLbl.grid(row=8,column=0,sticky=W)

        idproffesionEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_idprofession, font=("times new roman",14,"bold"),width=35)
        idproffesionEntry.grid(row=8,column=1)

        btnFrame=Frame(labelFrameLeft)
        btnFrame.place(x=0,y=400,width=342,height=40)


        btnupdate=Button(btnFrame,text="Update",command=self.update,font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=0)

        btndelete=Button(btnFrame,text="Delete",command=self.delete, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=1,padx=1)

        btnreset=Button(btnFrame,text="Reset",command=self.reset, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=2,padx=1)

        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Search and look staff data",font=("times new roman",12,"bold"),padx=2)
        TableFrame.place(x=505,y=50,width=1110,height=490)

        searchLbl=Label(TableFrame,text="Search by:",font=("times new roman",15,"bold"),bg="gold",fg="black")
        searchLbl.grid(row=0,column=0,sticky=W)

        searchCombo=ttk.Combobox(TableFrame,textvariable=self.var_searchBy,font=("times new roman",15,"bold"),width=24,state="readonly")
        searchCombo['value']=("idzaposleni","ime")
        searchCombo.current()
        searchCombo.grid(row=0,column=1,padx=2)

        searchTextEntry=ttk.Entry(TableFrame,textvariable=self.var_searchText, font=("times new roman",15,"bold"),width=24)
        searchTextEntry.grid(row=0,column=2,padx=2)

        btnsearch=Button(TableFrame,text="search",command=self.search, font=("times new roman",15,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(TableFrame,text="Show All",command=self.showAll, font=("times new roman",15,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)

        detailsTable=Frame(TableFrame,bd=2,relief=RIDGE)
        detailsTable.place(x=0,y=50,width=1100,height=420)

        scrollX=ttk.Scrollbar(detailsTable,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detailsTable,orient=VERTICAL)

        self.staffData=ttk.Treeview(detailsTable,columns=("idstaff","name","lastname","idcity","address","phone","email","idsection","idproffesion"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command=self.staffData.xview)
        scrollY.config(command=self.staffData.yview)

        self.staffData.heading("idstaff",text="Id Staff")
        self.staffData.heading("name",text="Name")
        self.staffData.heading("lastname",text="Last Name")
        self.staffData.heading("idcity",text="Id City")
        self.staffData.heading("address",text="Address")
        self.staffData.heading("phone",text="phone")
        self.staffData.heading("email",text="Email")
        self.staffData.heading("idsection",text="Id Sectiona")
        self.staffData.heading("idproffesion",text="Id Profession")

        self.staffData['show']="headings"
        self.staffData.column("idstaff",width=100)
        self.staffData.column("name",width=100)
        self.staffData.column("lastname",width=100)
        self.staffData.column("idcity",width=100)
        self.staffData.column("address",width=100)
        self.staffData.column("phone",width=100)
        self.staffData.column("email",width=100)
        self.staffData.column("idsection",width=100)
        self.staffData.column("idproffesion",width=100)

        self.staffData.pack(fill=BOTH,expand=1)
        self.staffData.bind("<ButtonRelease-1>",self.get_data)

        img2=Image.open(r"hotelsPhoto/hotel.jpg")
        img2=img2.resize((1620,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=0,y=540,width=1620,height=230)


    def showAll(self):
        con=Konekcija.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT idzaposleni,ime,prezime,idgrad,adresa,telefon,email,idodeljenje,idzanimanje FROM zaposleni")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.staffData.delete(*self.staffData.get_children())
            for i in rows:
                self.staffData.insert("",END,values=i)
                con.commit()
        
        
    def get_data(self,event=""):
        cursor_row=self.staffData.focus()
        content=self.staffData.item(cursor_row)
        row=content['values']

        self.var_idstaff.set(row[0]),
        self.var_name.set(row[1]),
        self.var_lastname.set(row[2]),
        self.var_idcity.set(row[3]),
        self.var_address.set(row[4]),
        self.var_phone.set(row[5]),
        self.var_email.set(row[6]),
        self.var_idsection.set(row[7]),
        self.var_idprofession.set(row[8])

    def search(self): 
        con=Konekcija.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT idzaposleni,ime,prezime,idgrad,adresa,telefon,email,idodeljenje,idzanimanje FROM zaposleni WHERE "+str(self.var_searchBy.get())+" LIKE binary '%"+self.var_searchText.get()+"%'")
        rows = cursor.fetchall()
        if(len(rows)!=0):
            self.staffData.delete(*self.staffData.get_children())
            for i in rows: 
                self.staffData.insert('',END,values=i)
                con.commit()
        else:
            self.staffData.delete(*self.staffData.get_children()) 


    def update(self):
        if self.var_idstaff.get()=="":
            messagebox.showerror("Error","Please,enter staff ID whose data update",parent=self.root)
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE zaposleni SET idgrad=%s,adresa=%s,telefon=%s WHERE idzaposleni=%s",(
                self.var_idcity.get(),
                self.var_address.get(),
                self.var_phone.get(),
                self.var_idstaff.get()
            ))
            con.commit()
            messagebox.showinfo("Update","Staff details updated successfully",parent=self.root)
            self.showAll()

    
    def delete(self):
        delete=messagebox.askyesno("Hotel Management","Do You really want to delete staff?",parent=self.root)
        if delete>0:
            con=Konekcija.getInstance()
            cursor=con.cursor()   
            query="DELETE FROM zaposleni WHERE idzaposleni=%s"
            value=(self.var_idstaff.get(),)
            cursor.execute(query,value)
        elif  not delete:
            return
        con.commit()
        messagebox.showinfo("Delete","Staff deleted successfully",parent=self.root)
        self.showAll()


    def reset(self):
        self.var_idstaff.set(0)
        self.var_name.set("")
        self.var_lastname.set("")
        self.var_idcity.set(0)
        self.var_address.set("")
        self.var_phone.set(0)
        self.var_email.set("")
        self.var_idsection.set(0)
        self.var_idprofession.set(0)
        self.var_searchBy.set("")
        self.var_searchText.set("")
        self.staffData.delete(*self.staffData.get_children())


'''root=Tk()
object=Staff(root)
mainloop()'''