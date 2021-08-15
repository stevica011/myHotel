from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

from mysql.connector import cursor
from veza2 import Konekcija2

class RoomDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("   ")
        self.root.geometry("1620x770+307+300")

        self.var_roomNo=IntVar()
        self.var_floor=IntVar()
        self.var_roomtype=StringVar()
        self.var_status=StringVar()
        self.var_price=IntVar()

        lbl_title=Label(self.root,text="Hotel Rooms",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1620,height=50)

        img1=Image.open(r"roomsPhoto/room.jpg")
        img1=img1.resize((120,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage1.place(x=5,y=5,width=120,height=40)

        labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add New Room",font=("times new roman",12,"bold"),padx=2)
        labelFrameLeft.place(x=5,y=50,width=590,height=380)

        roomNoLbl=Label(labelFrameLeft,text="Room Number",font=("times new roman",15,"bold"),padx=2,pady=6)
        roomNoLbl.grid(row=0,column=0,sticky=W)

        roomNoEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_roomNo, font=("times new roman",13,"bold"),width=25)
        roomNoEntry.grid(row=0,column=1,sticky=W)

        floorLbl=Label(labelFrameLeft,text="Floor",font=("times new roman",15,"bold"),padx=2,pady=6)
        floorLbl.grid(row=1,column=0,sticky=W)

        floorEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_floor, font=("times new roman",14,"bold"),width=25)
        floorEntry.grid(row=1,column=1,sticky=W)

        roomtypeLbl=Label(labelFrameLeft,text="Room Type",font=("times new roman",14,"bold"),padx=2,pady=6)
        roomtypeLbl.grid(row=2,column=0,sticky=W)

        roomtypeEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_roomtype, font=("times new roman",14,"bold"),width=25)
        roomtypeEntry.grid(row=2,column=1,sticky=W)

        statusLbl=Label(labelFrameLeft,text="Status",font=("times new roman",14,"bold"),padx=2,pady=6)
        statusLbl.grid(row=3,column=0,sticky=W)

        statusEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_status, font=("times new roman",14,"bold"),width=25)
        statusEntry.grid(row=3,column=1,sticky=W)

        priceLbl=Label(labelFrameLeft,text="Price",font=("times new roman",14,"bold"),padx=2,pady=6)
        priceLbl.grid(row=4,column=0,sticky=W)

        priceEntry=ttk.Entry(labelFrameLeft,textvariable=self.var_price, font=("times new roman",14,"bold"),width=25)
        priceEntry.grid(row=4,column=1,sticky=W)
    
        descriptionLbl=Label(labelFrameLeft,text="Description",font=("times new roman",14,"bold"),padx=2,pady=6)
        descriptionLbl.grid(row=5,column=0,sticky=W)

        self.descriptionText=Text(labelFrameLeft,width=35,height=4,font=("verdana",12,"bold"))
        self.descriptionText.grid(row=5,column=1,sticky=W)

        btnFrame=Frame(labelFrameLeft)
        btnFrame.place(x=0,y=300,width=412,height=40)

        btnAdd=Button(btnFrame,text="Add",command=self.add, font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate =Button(btnFrame,text="Update ",command=self.update , font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate .grid(row=0,column=1,padx=1)

        btnDelete=Button(btnFrame,text="Delete",command=self.delete, font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btnFrame,text="Reset",command=self.reset, font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        TableFrame.place(x=600,y=50,width=1020,height=380)

        scrollX=ttk.Scrollbar(TableFrame,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(TableFrame,orient=VERTICAL)

        self.ispis=ttk.Treeview(TableFrame,columns=("room number","floor","room type","status","description","price"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.ispis.xview)
        scrollY.config(command=self.ispis.yview)

        self.ispis.heading("room number",text="Room number")
        self.ispis.heading("floor",text="floor")
        self.ispis.heading("room type",text="Room type")
        self.ispis.heading("status",text="Status")
        self.ispis.heading("description",text="Description")
        self.ispis.heading("price",text="Price")
        self.ispis['show']="headings"
        self.ispis.column("room number",width=100)
        self.ispis.column("floor",width=100)
        self.ispis.column("room type",width=100)
        self.ispis.column("status",width=100)
        self.ispis.column("description",width=100)
        self.ispis.column("price",width=100)
        self.ispis.pack(fill=BOTH,expand=1)
        self.ispis.bind("<ButtonRelease-1>",self.data)

        databtn=Button(labelFrameLeft,text="Room",command=self.catch_data,font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        databtn.place(x=530,y=10,width=50,height=40)

        #ttk.Style().configure("Treeview", background="red2", foreground="white", fieldbackground="red2")

        img2=Image.open(r"roomsPhoto/room.jpg")
        img2=img2.resize((810,340),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=0,y=430,width=810,height=340)

        img3=Image.open(r"roomsPhoto/room3.jpg")
        img3=img3.resize((810,340),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblImage3=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblImage3.place(x=810,y=430,width=810,height=340)



    def add(self):
        if self.var_roomNo.get()=="" or self.var_floor.get()=="" or self.var_roomtype.get()=="" or self.var_status.get()=="" or self.var_price.get()=="":
            messagebox.showerror("Error","All fields must be filled!",parent=self.root)
        else:
            try:
                con=Konekcija2.getInstance()
                cursor=con.cursor()
                cursor.execute("INSERT INTO sobe VALUES(%s,%s,%s,%s,%s,%s)",(
                self.var_roomNo.get(),
                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_status.get(),
                self.descriptionText.get("1.0",END),
                self.var_price.get()
          ))
                con.commit()
                messagebox.showinfo("Success","New room added successfully",parent=self.root)
                self.reset()
                self.catch_data()
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong : {es}",parent=self.root)

    def catch_data(self):
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM sobe")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.ispis.delete(*self.ispis.get_children())
            for i in rows:
                self.ispis.insert("",END,values=i)
            con.commit()


    def data(self,event=""):
        cursor_row=self.ispis.focus()
        content=self.ispis.item(cursor_row)
        row=content['values']

        self.var_roomNo.set(row[0])
        self.var_floor.set(row[1])
        self.var_roomtype.set(row[2])
        self.var_status.set(row[3])
        self.var_price.set(row[5])
        self.descriptionText.delete("1.0",END)
        self.descriptionText.insert(END,row[4])

    def update (self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="" or self.var_status.get()=="" or self.var_price.get()=="":
            messagebox.showerror(
                "Error", "You must enter all data!", parent=self.root)
        else:
            con=Konekcija2.getInstance()
            cursor = con.cursor()
            cursor.execute("UPDATE sobe SET sprat=%s,tip_sobe=%s,statusSobe=%s,opis=%s,cena=%s WHERE brojsobe=%s", (
                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_status.get(),
                self.descriptionText.get("1.0",END),
                self.var_price.get(),
                self.var_roomNo.get()
            ))
            con.commit()
            messagebox.showinfo("Success", "Rooms data updated successfully", parent=self.root)
            self.reset()
            self.catch_data()
            

    def delete(self):
        Delete=messagebox.askyesno("Hotel Rooms","Do You really want to delete this room?")
        if Delete>0:
            con=Konekcija2.getInstance()
            cursor=con.cursor()
            query=("DELETE FROM sobe WHERE brojsobe=%s")
            value=(self.var_roomNo.get(),)
            cursor.execute(query,value)
        elif  not Delete:
            return
        con.commit()
        messagebox.showinfo("OK", "Room deleted successfully", parent=self.root)
        self.reset()
        self.catch_data()
        

    def reset(self):
        self.var_roomNo.set(0)
        self.var_floor.set(0)
        self.var_roomtype.set("")
        self.var_status.set("")
        self.var_price.set(0)
        self.descriptionText.delete("1.0",END)
        self.ispis.delete(*self.ispis.get_children())
       

'''root=Tk()
object=RoomDetails(root)
root.mainloop()'''