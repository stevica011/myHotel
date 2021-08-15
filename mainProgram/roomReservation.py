from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from mysql.connector import cursor
from veza2 import Konekcija2

class RoomReservation:
    def __init__(self,root):
        self.root=root
        self.root.title("   ")
        self.root.geometry("1620x770+307+300")


        self.var_billNo=IntVar()
        self.var_idguest=IntVar()
        self.var_roomNo=IntVar()
        self.var_checkIn=StringVar()
        self.var_checkOut=StringVar()
        self.var_availableRoom=StringVar()
        self.var_roomType=StringVar()
        self.var_daysNo=IntVar()
        self.var_roomPrice=IntVar()
        self.var_price=IntVar()
        self.var_addPrice=IntVar()
        self.var_bill=IntVar()
        self.var_status=StringVar()
        self.var_reservationDay=IntVar()

        self.var_total=IntVar()
        self.var_day=IntVar()
        self.var_statusD=StringVar()

        self.var_searchBy=StringVar()
        self.var_searchText=StringVar()
        
        lbltitle=Label(self.root,text="Room Reservation",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbltitle.place(x=0,y=0,width=1620,height=50)

        img1=Image.open(r"roomsPhoto/room.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=5,y=3,width=100,height=42)

        self.labelFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Reservation Details",font=("times new roman",12,"bold"),padx=2)
        self.labelFrameLeft.place(x=5,y=50,width=505,height=490)

        billNoLbl=Label(self.labelFrameLeft,text="Bill Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        billNoLbl.grid(row=0,column=0,sticky=W)

        billNoEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_billNo, font=("times new roman",13,"bold"),width=15,state="readonly")
        billNoEntry.grid(row=0,column=1)

        idguestLbl=Label(self.labelFrameLeft,text="Id guest",font=("times new roman",12,"bold"),padx=2,pady=6)
        idguestLbl.grid(row=1,column=0,sticky=W)

        idguestEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_idguest, font=("times new roman",13,"bold"),width=15)
        idguestEntry.grid(row=1,column=1)

        btnShowGuest=Button(self.labelFrameLeft,command=self.ShowGuest, text="Show Guest",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnShowGuest.place(x=390,y=35)

        roomNoLbl=Label(self.labelFrameLeft,text="Room Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        roomNoLbl.grid(row=2,column=0,sticky=W)

        roomNoEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_roomNo, font=("times new roman",13,"bold"),width=15)
        roomNoEntry.grid(row=2,column=1)

        checkInLbl=Label(self.labelFrameLeft,text="Check-In",font=("times new roman",12,"bold"),padx=2,pady=6)
        checkInLbl.grid(row=3,column=0,sticky=W)

        checkInEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_checkIn, font=("times new roman",13,"bold"),width=15)
        checkInEntry.grid(row=3,column=1)

        checkOutLbl=Label(self.labelFrameLeft,text="Check-Out",font=("times new roman",12,"bold"),padx=2,pady=6)
        checkOutLbl.grid(row=4,column=0,sticky=W)

        checkOutEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_checkOut, font=("times new roman",13,"bold"),width=15)
        checkOutEntry.grid(row=4,column=1)

        availableRoomLbl=Label(self.labelFrameLeft,text="Available Room",font=("times new roman",12,"bold"),padx=2,pady=6)
        availableRoomLbl.grid(row=5,column=0,sticky=W)
        
        self.availableRoom()

        btnavailableRoom=Button(self.labelFrameLeft,text="Room",command=self.read, font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnavailableRoom.place(x=300,y=168)

        btnRefresh=Button(self.labelFrameLeft,text="Refresh",command=self.availableRoom, font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnRefresh.place(x=400,y=167)

        typeroomLbl=Label(self.labelFrameLeft,text="Type room",font=("times new roman",12,"bold"),padx=2,pady=6)
        typeroomLbl.grid(row=6,column=0,sticky=W)

        typeroomEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_roomType, font=("times new roman",13,"bold"),width=15)
        typeroomEntry.grid(row=6,column=1)

        daysNoLbl=Label(self.labelFrameLeft,text="Days Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        daysNoLbl.grid(row=7,column=0,sticky=W)

        daysNoEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_daysNo, font=("times new roman",13,"bold"),width=15)
        daysNoEntry.grid(row=7,column=1)

        roomPriceLbl=Label(self.labelFrameLeft,text="Room Price",font=("times new roman",12,"bold"),padx=2,pady=6)
        roomPriceLbl.grid(row=8,column=0,sticky=W)

        roomPriceEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_roomPrice, font=("times new roman",13,"bold"),width=15)
        roomPriceEntry.grid(row=8,column=1)

        btnPayment=Button(self.labelFrameLeft,text="Price",command=self.payment, font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnPayment.grid(row=9,column=0,padx=1,sticky=W)

        priceEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_price, font=("times new roman",13,"bold"),width=15)
        priceEntry.grid(row=9,column=1)

        btnPayment2=Button(self.labelFrameLeft,text="Add Price",command=self.payment2, font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnPayment2.grid(row=9,column=2,padx=1,sticky=W)

        priceAddEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_addPrice, font=("times new roman",13,"bold"),width=15)
        priceAddEntry.grid(row=9,column=3)

        btnbill=Button(self.labelFrameLeft,text="Payment",command=self.paybill, font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)

        totalEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_bill, font=("times new roman",13,"bold"),width=15)
        totalEntry.grid(row=10,column=1)

        statusbillLbl=Label(self.labelFrameLeft,text="Bill Status",font=("times new roman",12,"bold"),padx=2,pady=6)
        statusbillLbl.grid(row=11,column=0,sticky=W)

        statusbillEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_status, font=("times new roman",13,"bold"),width=15)
        statusbillEntry.grid(row=11,column=1)

        reservationDayLbl=Label(self.labelFrameLeft,text="DayR",font=("times new roman",12,"bold"),padx=2,pady=6)
        reservationDayLbl.grid(row=12,column=0,sticky=W)

        reservationDayEntry=ttk.Entry(self.labelFrameLeft,textvariable=self.var_reservationDay, font=("times new roman",13,"bold"),width=15)
        reservationDayEntry.grid(row=12,column=1)


        btnFrame=Frame(self.labelFrameLeft)
        btnFrame.place(x=0,y=430,width=448,height=36)

        btnReserve=Button(btnFrame,text="Reserve",command=self.AddReservation, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnReserve.grid(row=0,column=0,padx=1)

        btnChange=Button(btnFrame,text="Change",command=self.changeReservation, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnChange.grid(row=0,column=1,padx=1)

        btnDelete=Button(btnFrame,text="Delete",command=self.delete, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btnFrame,text="Reset",command=self.reset, font=("times new roman",12,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)


        img2=Image.open(r"roomsPhoto/room.jpg")
        img2=img2.resize((700,230),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=900,y=55,width=700,height=230)


        TableFrame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Look at the details and search for reservation",font=("times new roman",12,"bold"),padx=2)
        TableFrame.place(x=505,y=280,width=1110,height=260)

        searchLbl=Label(TableFrame,text="Search",font=("times new roman",15,"bold"),bg="gold",fg="black")
        searchLbl.grid(row=0,column=0,sticky=W)

        searchCombo=ttk.Combobox(TableFrame,textvariable=self.var_searchBy, font=("times new roman",15,"bold"),width=24,state="readonly")
        searchCombo['value']=("idgosti","brojsobe")
        searchCombo.current()
        searchCombo.grid(row=0,column=1,padx=2)

        searchTextEntry=ttk.Entry(TableFrame,textvariable=self.var_searchText, font=("times new roman",15,"bold"),width=24)
        searchTextEntry.grid(row=0,column=2,padx=2)

        btnSearch=Button(TableFrame,text="Search",command=self.search, font=("times new roman",15,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(TableFrame,text="Show All",command=self.showReservation, font=("times new roman",15,"bold"),bg="black",fg="gold",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)


        detailsTable=Frame(TableFrame,bd=2,relief=RIDGE)
        detailsTable.place(x=0,y=50,width=1100,height=180)

        scrollX=ttk.Scrollbar(detailsTable,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(detailsTable,orient=VERTICAL)

        self.roomTable=ttk.Treeview(detailsTable,columns=("billNo","idguest","roomNo","checkIn","checkOut","currentprice","total","status","day"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.roomTable.xview)
        scrollY.config(command=self.roomTable.yview)

        self.roomTable.heading("billNo",text="Bill Number")
        self.roomTable.heading("idguest",text="ID Guest")
        self.roomTable.heading("roomNo",text="Room Number")
        self.roomTable.heading("checkIn",text="Check-In")
        self.roomTable.heading("checkOut",text="Check-Out")
        self.roomTable.heading("currentprice",text="Payment")
        self.roomTable.heading("total",text="Bill Total")
        self.roomTable.heading("status",text="Bill Status")
        self.roomTable.heading("day",text="Day")
        self.roomTable['show']="headings"
        self.roomTable.column("billNo",width=100)
        self.roomTable.column("idguest",width=100)
        self.roomTable.column("roomNo",width=100)
        self.roomTable.column("checkIn",width=100)
        self.roomTable.column("checkOut",width=100)
        self.roomTable.column("currentprice",width=100)
        self.roomTable.column("total",width=100)
        self.roomTable.column("status",width=100)
        self.roomTable.column("day",width=100)
     
        self.roomTable.pack(fill=BOTH,expand=1)
        self.roomTable.bind("<ButtonRelease-1>",self.get_data)


        frametotal=Frame(self.root)
        frametotal.place(x=10,y=550,width=400,height=200)

        totalLbl=Label(frametotal,text="Total",font=("times new roman",12,"bold"),pady=6,width=6)
        totalLbl.grid(row=1,column=0)

        totalEntry=ttk.Entry(frametotal,textvariable=self.var_total)
        totalEntry.grid(row=1,column=1,padx=20)

        dayLbl=Label(frametotal,text="Day",font=("times new roman",12,"bold"),pady=6,width=6)
        dayLbl.grid(row=2,column=0)

        dayEntry=ttk.Entry(frametotal,textvariable=self.var_day)
        dayEntry.grid(row=2,column=1,padx=20)

        statusDlbl=Label(frametotal,text="Status",font=("times new roman",12,"bold"),pady=6,width=6)
        statusDlbl.grid(row=3,column=0)

        statusEntry=ttk.Entry(frametotal,textvariable=self.var_statusD)
        statusEntry.grid(row=3,column=1)

        buttontotal=Button(frametotal,text="Signing up",command=self.signingupBill,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        buttontotal.grid(row=1,column=3,padx=1)

        buttondays=Button(frametotal,text="Days",command=self.ShowAlldays, font=("times new roman",10,"bold"),bg="black",fg="gold",width=8)
        buttondays.grid(row=2,column=3,padx=1)

        buttontoday=Button(frametotal,text="Today",command=self.showToday, font=("times new roman",10,"bold"),bg="black",fg="gold",width=8)
        buttontoday.grid(row=3,column=3,padx=1)


        detailsTable2=Frame(self.root)
        detailsTable2.place(x=390,y=550,width=300,height=200)

        scroll_x2 = Scrollbar(detailsTable2,orient=HORIZONTAL)
        scroll_y2 = Scrollbar(detailsTable2,orient=VERTICAL)
        self.ispis2=ttk.Treeview(detailsTable2,columns=("day","cashbox","status"),xscrollcommand=scroll_x2.set,yscrollcommand=scroll_y2.set)
        scroll_x2.pack(side=BOTTOM,fill=X)
        scroll_y2.pack(side=RIGHT,fill=Y)
        scroll_x2.config(command=self.ispis2.xview) 
        scroll_y2.config(command=self.ispis2.yview)
        self.ispis2.heading("day",text="Day")
        self.ispis2.heading("cashbox",text="Cashbox")
        self.ispis2.heading("status",text="Status")
        self.ispis2['show']='headings'  
        self.ispis2.column("day",width=100)
        self.ispis2.column("cashbox",width=100)
        self.ispis2.column("status",width=100)
        self.ispis2.bind("<ButtonRelease-1>",self.get_data2)
        self.ispis2.pack(fill=BOTH,expand=1)

        buttonOff=Button(self.root,text="Conection Off",command=self.off, font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        buttonOff.place(x=1490,y=735,width=130,height=30)


    def ShowAlldays(self):
        con=Konekcija2.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM pazar")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.ispis2.delete(*self.ispis2.get_children())
            for row in rows:
                self.ispis2.insert('',END,values=row)
                con.commit()

    def showToday(self):
        con=Konekcija2.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM pazar WHERE status='otvoren'")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.ispis2.delete(*self.ispis2.get_children())
            for row in rows:
                self.ispis2.insert('',END,values=row)
                con.commit()

    
    def get_data2(self,event):
        cursor_row = self.ispis2.focus()
        contents = self.ispis2.item(cursor_row)
        row = contents['values']

        self.var_day.set(row[0])
        self.var_total.set(row[1])
        self.var_statusD.set(row[2])

    def signingupBill(self):
        if self.var_statusD.get()!="otvoren":
            messagebox.showerror("Error", "This day is finished,choose today!", parent=self.root)
        elif self.var_reservationDay.get()==0:
            messagebox.showerror("Error", "This reservation is not charged!", parent=self.root)
        else:
            if self.var_status.get()=="naplaćen":
                con=Konekcija2.getInstance()
                cur=con.cursor()
                cur.execute("UPDATE pazar SET kasa=%s WHERE dan=%s",(self.var_total.get()+self.var_bill.get(),self.var_day.get(),))
                cur.execute("UPDATE rezervacija SET status='upisan u kasu' WHERE brojračuna=%s",(self.var_billNo.get(),))
                con.commit()
                messagebox.showinfo("OK","Total magnified successfully ",parent=self.root)
                self.reset()
                self.showToday()
                self.showReservation()           
            elif self.var_status.get()=="upisan u kasu":
                messagebox.showerror("Error", "Bill is already written in", parent=self.root)
            else:
                messagebox.showerror("Error", "Bill is not charged", parent=self.root)


    def AddReservation(self):
        if self.var_idguest.get()==0 or self.var_roomNo.get()==0 or self.var_checkIn.get()=="" or self.var_checkOut.get()=="" or self.var_price.get()==0:
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                con=Konekcija2.getInstance()
                cursor=con.cursor()
                self.var_status.set("otvoren")
                cursor.execute("INSERT INTO rezervacija(idgosti,brojsobe,prijava,odjava,trenutnacena,total,status,dan) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_idguest.get(),
                self.var_roomNo.get(),
                self.var_checkIn.get(),
                self.var_checkOut.get(),
                self.var_price.get(),
                self.var_bill.get(),
                self.var_status.get(),
                self.var_reservationDay.get()
          ))
                cursor.execute("UPDATE sobe SET statusSobe='zauzeta' WHERE brojsobe=%s",(self.var_roomNo.get(),))
                con.commit()
                messagebox.showinfo("Success","Room reserved successfully",parent=self.root)
                self.reset()
                self.showReservation() 
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{es}",parent=self.root)

    def changeReservation(self):
        if self.var_status.get()!="otvoren":
            messagebox.showerror("Error", "You can not change reservation,bill is already charged!", parent=self.root)
        elif self.var_checkIn.get()=="" or self.var_checkOut.get()=="":
            messagebox.showerror("Error", "Enter dates", parent=self.root)
        else:
            con=Konekcija2.getInstance()
            cursor = con.cursor()
            cursor.execute("UPDATE rezervacija SET prijava=%s,odjava=%s,trenutnacena=%s  WHERE brojračuna=%s", (
                self.var_checkIn.get(),
                self.var_checkOut.get(),
                self.var_price.get(),
                self.var_billNo.get()
            ))
            con.commit()
            messagebox.showinfo("Change", "Reservation changed successfully", parent=self.root)
            self.reset()
            self.showReservation()
            

    
    def delete(self):
        if self.var_bill.get()!=0:
            messagebox.showerror("Error", "Bill is already charged", parent=self.root)
        else:
            Delete=messagebox.askyesno("Hotel Management","Do You really want to delete this reservation?")
            if Delete>0:
                con=Konekcija2.getInstance()
                cursor=con.cursor()
                query="DELETE FROM rezervacija WHERE brojračuna=%s"
                value=(self.var_billNo.get(),)
                cursor.execute(query,value)
                cursor.execute("UPDATE sobe SET statuSobe='slobodna' WHERE brojsobe=%s",(self.var_roomNo.get(),))
            else:
                return
            con.commit()
            messagebox.showinfo("Success","Reservation deleted successfully",parent=self.root)
            self.reset()
            self.showReservation()

    def reset(self):
        self.var_idguest.set(0)
        self.var_roomNo.set(0)
        self.var_checkIn.set("")
        self.var_checkOut.set("")
        self.var_availableRoom.set("")
        self.var_roomType.set("")
        self.var_daysNo.set(0)
        self.var_roomPrice.set(0)
        self.var_addPrice.set(0)
        self.var_price.set(0)
        self.var_bill.set(0)
        self.var_status.set("")
        self.var_billNo.set(0)
        if self.var_statusD.get()!="otvoren":
            self.var_total.set(0)
            self.var_day.set(0)
            self.var_statusD.set("")
        self.var_reservationDay.set(0)
        self.roomTable.delete(*self.roomTable.get_children())

    def reset2(self):
        self.var_idguest.set(0)
        self.var_checkIn.set("")
        self.var_checkOut.set("")
        self.var_availableRoom.set("")
        self.var_daysNo.set(0)
        self.var_addPrice.set(0)
        self.var_price.set(0)
        self.var_bill.set(0)
        self.var_status.set("")
        self.var_billNo.set(0)
        if self.var_statusD.get()!="otvoren":
            self.var_total.set(0)
            self.var_day.set(0)
            self.var_statusD.set("")
        self.var_reservationDay.set(0)
        self.roomTable.delete(*self.roomTable.get_children())

    def payment(self):
        self.var_price.set(self.var_roomPrice.get()*self.var_daysNo.get())

    def payment2(self):
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT tip_sobe,cena FROM sobe WHERE brojsobe=%s",(self.var_roomNo.get(),))
        soba=cursor.fetchone()
        self.var_roomType.set(soba[0])
        self.var_roomPrice.set(soba[1])
        self.var_addPrice.set(self.var_daysNo.get()*self.var_roomPrice.get())
        self.var_price.set(self.var_price.get()+self.var_addPrice.get())
        con.commit()

    def paybill(self):
        if self.var_price.get()==0:
            messagebox.showerror("Error","No debit",parent=self.root)
        elif self.var_bill.get()!=0:
            messagebox.showerror("Error", "Bill is already charged", parent=self.root)
        elif self.var_statusD.get()!="otvoren":
            messagebox.showerror("Error", "Day is already finished,choose today!", parent=self.root)
        else:
            con=Konekcija2.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE rezervacija SET total=%s,dan=%s,status='naplaćen' WHERE brojračuna=%s",(self.var_price.get(),self.var_day.get(),self.var_billNo.get()))
            cursor.execute("UPDATE sobe SET statusSobe='slobodna' WHERE brojsobe=%s",(self.var_roomNo.get(),))
            if self.var_price.get()>15000:
                cursor.execute("UPDATE gosti SET bodovi=bodovi+200,brojrezervacija=brojrezervacija+1  WHERE idgosti=%s",(self.var_idguest.get(),))
                con.commit()
                messagebox.showinfo("Payment", "Bill is charged successfully", parent=self.root)
                self.reset()
                self.showReservation()
            elif self.var_price.get()>10000 and self.var_price.get()<=15000:
                cursor.execute("UPDATE gosti SET bodovi=bodovi+100,brojrezervacija=brojrezervacija+1  WHERE idgosti=%s",(self.var_idguest.get(),))
                con.commit()
                messagebox.showinfo("Payment", "Bill is charged successfully", parent=self.root)
                self.reset()
                self.showReservation()
            else:
                cursor.execute("UPDATE gosti SET bodovi=bodovi+50,brojrezervacija=brojrezervacija+1  WHERE idgosti=%s",(self.var_idguest.get(),))
                con.commit()
                messagebox.showinfo("Payment", "Bill is charged successfully", parent=self.root)
                self.reset()
                self.showReservation()
                
            
    def search(self): 
        con=Konekcija2.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM rezervacija WHERE "+str(self.var_searchBy.get())+" = "+self.var_searchText.get())
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.roomTable.delete(*self.roomTable.get_children())
            for i in rows: 
                self.roomTable.insert('',END,values=i)
                con.commit()
        else:
            self.roomTable.delete(*self.roomTable.get_children())    

    def showReservation(self):
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM rezervacija")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.roomTable.delete(*self.roomTable.get_children())
            for i in rows:
                self.roomTable.insert("",END,values=i)
            con.commit()

    def get_data(self,event=""):
        cursor_row=self.roomTable.focus()
        content=self.roomTable.item(cursor_row)
        row=content['values']

        self.var_billNo.set(row[0]),
        self.var_idguest.set(row[1]),
        self.var_roomNo.set(row[2]),
        self.var_checkIn.set(row[3]),
        self.var_checkOut.set(row[4]),
        self.var_price.set(row[5]),
        self.var_bill.set(row[6]),
        self.var_status.set(row[7])
        self.var_reservationDay.set(row[8])

        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT tip_sobe,cena FROM sobe WHERE brojsobe=%s",(self.var_roomNo.get(),))
        soba=cursor.fetchone()
        self.var_roomType.set(soba[0])
        self.var_roomPrice.set(soba[1])
        con.commit()

    def read(self):
        self.var_roomNo.set(self.var_availableRoom.get()[0:4])
        if self.var_availableRoom.get()[5:13]=="Apartman":
            self.var_roomType.set(self.var_availableRoom.get()[5:13])
            self.var_roomPrice.set(self.var_availableRoom.get()[14:])
        elif self.var_availableRoom.get()[5:9]=="Dubl":
            self.var_roomType.set(self.var_availableRoom.get()[5:9])
            self.var_roomPrice.set(self.var_availableRoom.get()[10:])
        else:
            self.var_roomType.set(self.var_availableRoom.get()[5:10])
            self.var_roomPrice.set(self.var_availableRoom.get()[11:])
        self.reset2()
    
    def ShowGuest(self):
        if self.var_idguest.get()==0:
            messagebox.showerror("Error","Please,enter Guest ID",parent=self.root)
        else:
            con=Konekcija2.getInstance()
            cur=con.cursor()
            query=("SELECT ime FROM gosti WHERE idgosti=%s")
            value=(self.var_idguest.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","This ID does not exist!",parent=self.root)
            else:

                displayFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                displayFrame.place(x=515,y=60,width=320,height=210)

                lblName=Label(displayFrame,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(displayFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                query=("SELECT  prezime FROM gosti WHERE idgosti=%s")
                value=(self.var_idguest.get(),)
                cur.execute(query,value)
                row=cur.fetchone()

                lblLastName=Label(displayFrame,text="Last Name:",font=("arial",12,"bold"))
                lblLastName.place(x=0,y=30)

                lbl2=Label(displayFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                query=("SELECT  email FROM gosti WHERE idgosti=%s")
                value=(self.var_idguest.get(),)
                cur.execute(query,value)
                row=cur.fetchone()

                lblEmail=Label(displayFrame,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3=Label(displayFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                query=("SELECT  telefon FROM gosti WHERE idgosti=%s")
                value=(self.var_idguest.get(),)
                cur.execute(query,value)
                row=cur.fetchone()

                lblPhone=Label(displayFrame,text="Phone:",font=("arial",12,"bold"))
                lblPhone.place(x=0,y=90)

                lbl4=Label(displayFrame,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                query=("SELECT  godine FROM gosti WHERE idgosti=%s")
                value=(self.var_idguest.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
           
                lblYears=Label(displayFrame,text="Years:",font=("arial",12,"bold"))
                lblYears.place(x=0,y=120)

                lbl5=Label(displayFrame,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)

                query=("SELECT  bodovi FROM gosti WHERE idgosti=%s")
                value=(self.var_idguest.get(),)
                cur.execute(query,value)
                row=cur.fetchone()

                lblPoints=Label(displayFrame,text="Points:",font=("arial",12,"bold"))
                lblPoints.place(x=0,y=150)

                lbl5=Label(displayFrame,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=150)

                con.commit()

    def availableRoom(self):
        con=Konekcija2.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT brojsobe,tip_sobe,cena FROM sobe WHERE statusSobe='slobodna'")
        soba=cursor.fetchall()
        availableRoomCombo=ttk.Combobox(self.labelFrameLeft,textvariable=self.var_availableRoom,font=("times new roman",13,"bold"),width=18,state="readonly")
        availableRoomCombo.current()
        availableRoomCombo['value']=soba
        availableRoomCombo.grid(row=5,column=1,padx=1,sticky=W)
        con.commit()

    def off(self):
        con=Konekcija2.getInstance()
        messagebox.showinfo("Off","Log-Out successfully!")
        con.close()

    def again(self):
        self.root.destroy()
        root=Tk()
        object=RoomReservation(root)
        mainloop()


'''root=Tk()
object=RoomReservation(root)
mainloop()'''

