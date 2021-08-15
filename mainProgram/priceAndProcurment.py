from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
from time import strftime
from datetime import date, datetime
from veza import Konekcija

class PriceProcurment:
    def __init__(self,root):
        self.root=root
        self.root.title("    ")
        self.root.geometry("1850x1050+0+0")

        self.root.protocol('WM_DELETE_WINDOW',self.closeWindow)

        self.var_norms=IntVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity =StringVar()
        self.var_article=IntVar()

        self.var_item=IntVar()
        self.var_name2=StringVar()
        self.var_condition=StringVar()
        self.var_procurment=IntVar()
        self.var_limit=IntVar()

        self.var_findBy1=StringVar()
        self.var_findByText1=StringVar()
        self.var_findBy2=StringVar()
        self.var_findByText2=StringVar()



        img1=Image.open(r"restaurantsPhoto/restoran5.jpg")
        img1=img1.resize((620,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblImage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblImage.place(x=0,y=0,width=620,height=140)

        img2=Image.open(r"restaurantsPhoto/restoran3.jpg")
        img2=img2.resize((620,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblImage2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblImage2.place(x=620,y=0,width=620,height=140)

        img3=Image.open(r"restaurantsPhoto/restoran4.jpg")
        img3=img3.resize((610,140),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblImage3=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblImage3.place(x=1240,y=0,width=610,height=140)

        titleLbl=Label(self.root,text="Change Price and Procurment Articles",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        titleLbl.place(x=0,y=140,width=1850,height=70)

        self.lbl = Label(self.root, font = ('calibri', 15, 'bold'),
        foreground = 'gold',background="black")
        self.lbl.place(x=10,y=160,width=300)
        self.date()


        framePrice=LabelFrame(self.root,bd=2,relief=RIDGE,text="Check and change price",font=("times new roman",15,"bold"),padx=2)
        framePrice.place(x=10,y=210,width=920,height=800)

        idnormsLbl=Label(framePrice,text="ID article",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        idnormsLbl.grid(row=0,column=0)

        idnormsEntry=ttk.Entry(framePrice,textvariable=self.var_norms, font=("times new roman",12,"bold"))
        idnormsEntry.grid(row=0,column=1)

        nameLbl=Label(framePrice,text="Name",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        nameLbl.grid(row=1,column=0)

        nameEntry=ttk.Entry(framePrice,textvariable=self.var_name, font=("times new roman",12,"bold"))
        nameEntry.grid(row=1,column=1)

        priceLbl=Label(framePrice,text="Price",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        priceLbl.grid(row=2,column=0)

        priceEntry=ttk.Entry(framePrice,textvariable=self.var_price, font=("times new roman",12,"bold"))
        priceEntry.grid(row=2,column=1)

        quantityLbl=Label(framePrice,text="Quantity",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        quantityLbl.grid(row=3,column=0)

        quantityEntry=ttk.Entry(framePrice,textvariable=self.var_quantity, font=("times new roman",12,"bold"))
        quantityEntry.grid(row=3,column=1)

        itemIdLbl=Label(framePrice,text="ID Item",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        itemIdLbl.grid(row=4,column=0)

        itemIdEntry=ttk.Entry(framePrice,textvariable=self.var_article, font=("times new roman",12,"bold"))
        itemIdEntry.grid(row=4,column=1)

        btnFrame=Frame(framePrice)
        btnFrame.place(x=0,y=200,width=480,height=40)

        btnAddArticle=Button(btnFrame,text="Add Article",command=self.addNewArticle, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnAddArticle.grid(row=0,column=0,padx=1)

        btnchangeArticle=Button(btnFrame,text="Change Article",command=self.changeArticle, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnchangeArticle.grid(row=0,column=1,padx=1)

        btnDeleteArticle=Button(btnFrame,text="Delete Article",command=self.deleteArticle, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnDeleteArticle.grid(row=0,column=2,padx=1)

        btnReset=Button(btnFrame,text="Reset",command=self.reset, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnReset.grid(row=0,column=3,padx=1)

        TableFrame=Frame(framePrice,bd=2,relief=RIDGE)
        TableFrame.place(x=0,y=300,width=915,height=500)

        searchLbl=Label(TableFrame,text="Search By:",font=("times new roman",14,"bold"),bg="black",fg="yellow")
        searchLbl.grid(row=1,column=0,sticky=W)

        searchCombo=ttk.Combobox(TableFrame,textvariable=self.var_findBy1,font=("times new roman",12,"bold"),width=14,state="readonly")
        searchCombo['value']=("idnormativi","nazivArtikla")
        searchCombo.current()
        searchCombo.grid(row=1,column=1,padx=2)
   
        searchText=ttk.Entry(TableFrame,textvariable=self.var_findByText1, font=("times new roman",12,"bold"),width=14)
        searchText.grid(row=1,column=2,padx=2)

        btnsearch=Button(TableFrame,text="Search",command=self.searchArticle, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnsearch.grid(row=1,column=3,padx=1)

        btnshow=Button(TableFrame,text="Show All",command=self.showArticles, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnshow.grid(row=1,column=4,padx=1)

        detailsTable=Frame(TableFrame)
        detailsTable.place(x=0,y=70,width=910,height=400)
        
        scroll_x = Scrollbar(detailsTable,orient=HORIZONTAL)
        scroll_y = Scrollbar(detailsTable,orient=VERTICAL)
        self.print=ttk.Treeview(detailsTable,columns=("idnorms","nameArticle","price","quantity","itemId"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.print.xview) 
        scroll_y.config(command=self.print.yview)
        self.print.heading("idnorms",text="ID Norms")
        self.print.heading("nameArticle",text="Name")
        self.print.heading("price",text="Price")
        self.print.heading("quantity",text="Quantity")
        self.print.heading("itemId",text="ID Item")
        self.print['show']='headings' 
        self.print.column("idnorms",width=100) 
        self.print.column("nameArticle",width=100)
        self.print.column("price",width=100)
        self.print.column("quantity",width=100)
        self.print.column("itemId",width=100)
        self.print.bind("<ButtonRelease-1>",self.get_data)
        self.print.pack(fill=BOTH,expand=1)

        frameProcurment=LabelFrame(self.root,bd=2,relief=RIDGE,text="Procurment Items",font=("times new roman",15,"bold"),padx=2)
        frameProcurment.place(x=930,y=210,width=910,height=800)

        iditemLbl=Label(frameProcurment,text="ID Item",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        iditemLbl.grid(row=0,column=0)

        iditemEntry=ttk.Entry(frameProcurment,textvariable=self.var_item, font=("times new roman",12,"bold"))
        iditemEntry.grid(row=0,column=1)

        name2Lbl=Label(frameProcurment,text="Name",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        name2Lbl.grid(row=1,column=0)

        name2Entry=ttk.Entry(frameProcurment,textvariable=self.var_name2, font=("times new roman",12,"bold"))
        name2Entry.grid(row=1,column=1)

        conditionLbl=Label(frameProcurment,text="Condition",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        conditionLbl.grid(row=2,column=0)

        conditionEntry=ttk.Entry(frameProcurment,textvariable=self.var_condition, font=("times new roman",12,"bold"))
        conditionEntry.grid(row=2,column=1,padx=5)

        ProcurmentLbl=Label(frameProcurment,text="Procurment",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        ProcurmentLbl.grid(row=2,column=2)

        ProcurmentEntry=ttk.Entry(frameProcurment,textvariable=self.var_procurment, font=("times new roman",12,"bold"))
        ProcurmentEntry.grid(row=2,column=3)

        limitLbl=Label(frameProcurment,text="Limit",font=("times new roman",12,"bold"),padx=2,pady=3,width=10)
        limitLbl.grid(row=3,column=0)

        limitEntry=ttk.Entry(frameProcurment,textvariable=self.var_limit, font=("times new roman",12,"bold"))
        limitEntry.grid(row=3,column=1)

        btnFrame2=Frame(frameProcurment)
        btnFrame2.place(x=0,y=200,width=480,height=40)

        btnAddItem=Button(btnFrame2,text="Add Item",command=self.signingupNewItem, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnAddItem.grid(row=0,column=0,padx=1)

        btnchangeItem=Button(btnFrame2,text="Procurment",command=self.addCondition, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnchangeItem.grid(row=0,column=1,padx=1)

        btnDeleteItem=Button(btnFrame2,text="Delete Item",command=self.deleteItem, font=("times new roman",12,"bold"),bg="black",fg="gold",width=11)
        btnDeleteItem.grid(row=0,column=2,padx=1)

        TableFrame2=Frame(frameProcurment,bd=2,relief=RIDGE)
        TableFrame2.place(x=0,y=300,width=905,height=500)

        searchLbl2=Label(TableFrame2,text="Search By:",font=("times new roman",14,"bold"),bg="black",fg="yellow")
        searchLbl2.grid(row=1,column=0,sticky=W)

        searchCombo2=ttk.Combobox(TableFrame2,textvariable=self.var_findBy2,font=("times new roman",12,"bold"),width=14,state="readonly")
        searchCombo2['value']=("idartikli","naziv")
        searchCombo2.current()
        searchCombo2.grid(row=1,column=1,padx=2)
   
        searchText2=ttk.Entry(TableFrame2,textvariable=self.var_findByText2, font=("times new roman",12,"bold"),width=14)
        searchText2.grid(row=1,column=2,padx=2)

        btnsearch2=Button(TableFrame2,text="Search:",command=self.searchItem, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnsearch2.grid(row=1,column=3,padx=1)

        btnshow2=Button(TableFrame2,text="Show All",command=self.showItems, font=("times new roman",12,"bold"),bg="black",fg="gold",width=7)
        btnshow2.grid(row=1,column=4,padx=1)

        detailsTable2=Frame(TableFrame2)
        detailsTable2.place(x=0,y=70,width=900,height=400)
        
        scroll_x2 = Scrollbar(detailsTable2,orient=HORIZONTAL)
        scroll_y2 = Scrollbar(detailsTable2,orient=VERTICAL)
        self.print2=ttk.Treeview(detailsTable2,columns=("iditem","name","condition","limit"),xscrollcommand=scroll_x2.set,yscrollcommand=scroll_y2.set)
        scroll_x2.pack(side=BOTTOM,fill=X)
        scroll_y2.pack(side=RIGHT,fill=Y)
        scroll_x2.config(command=self.print2.xview) 
        scroll_y2.config(command=self.print2.yview)
        self.print2.heading("iditem",text="ID Item")
        self.print2.heading("name",text="Name")
        self.print2.heading("condition",text="Condition")
        self.print2.heading("limit",text="Limit")
        self.print2['show']='headings' 
        self.print2.column("iditem",width=100) 
        self.print2.column("name",width=100)
        self.print2.column("condition",width=100)
        self.print2.column("limit",width=100)
        self.print2.bind("<ButtonRelease-1>",self.get_data2)
        self.print2.pack(fill=BOTH,expand=1)


    def showArticles(self):
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM normativi")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.print.delete(*self.print.get_children())
            for row in rows:
                self.print.insert('',END,values=row)
            con.commit()

    def get_data(self,event):
        cursor_row = self.print.focus()
        contents = self.print.item(cursor_row)
        row = contents['values']

        self.var_norms.set(row[0])
        self.var_name.set(row[1])
        self.var_price.set(row[2])
        self.var_quantity.set(row[3])
        self.var_article.set(row[4])

    def searchArticle(self):
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM normativi WHERE "+str(self.var_findBy1.get())+" LIKE binary '%"+self.var_findByText1.get()+"%'") 
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.print.delete(*self.print.get_children())
            for i in rows: 
                self.print.insert('',END,values=i)
                con.commit()
        else:
            self.print.delete(*self.print.get_children()) 
    
    def showItems(self):
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM artikli")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.print2.delete(*self.print2.get_children())
            for row in rows:
                self.print2.insert('',END,values=row)
            con.commit()


    def get_data2(self,event):
        cursor_row = self.print2.focus()
        contents = self.print2.item(cursor_row)
        row = contents['values']

        self.var_item.set(row[0])
        self.var_name2.set(row[1])
        self.var_condition.set(row[2])
        self.var_limit.set(row[3])

    def searchItem(self):
        con=Konekcija.getInstance()
        cur=con.cursor()
        cur.execute("SELECT * FROM artikli WHERE "+str(self.var_findBy2.get())+" LIKE binary '%"+self.var_findByText2.get()+"%'") 
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.print2.delete(*self.print2.get_children())
            for i in rows: 
                self.print2.insert('',END,values=i)
                con.commit()
        else:
            self.print2.delete(*self.print2.get_children()) 


    def addNewArticle(self):
        if self.var_name.get()=="" or self.var_price.get()=="" or self.var_quantity.get()=="" or self.var_article.get()==0 :
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                con=Konekcija.getInstance()
                cursor=con.cursor()
                cursor.execute("INSERT INTO normativi(nazivArtikla,cena,količina,idartikli) VALUES(%s,%s,%s,%s)",(
            self.var_name.get(),
            float(self.var_price.get()),
            float(self.var_quantity.get()),
            self.var_article.get()))
                con.commit()
                messagebox.showinfo("OK","Article added successfully",parent=self.root)
                self.reset()
                self.showArticles()
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{es}",parent=self.root)

    def changeArticle(self):
        if self.var_norms.get()==0:
            messagebox.showerror("Error","Please,enter id article",parent=self.root)
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE normativi SET cena=%s,količina=%s  WHERE idnormativi=%s",(
                float(self.var_price.get()),
                float(self.var_quantity.get()),
                self.var_norms.get()
            ))
            con.commit()
            messagebox.showinfo("Success","Article changed successfully",parent=self.root)
            self.reset()
            self.showArticles()


    def deleteArticle(self):
        obriši=messagebox.askyesno("Restaurant","Do You really want to delete this article?")
        if obriši>0:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            query=("DELETE FROM normativi WHERE idnormativi=%s")
            value=(self.var_norms.get(),)
            cursor.execute(query,value)
        elif  not obriši:
            return
        con.commit()
        messagebox.showinfo("Success","Article deleted successfully",parent=self.root)
        self.reset()
        self.showArticles()


    def reset(self):
        self.var_norms.set(0)
        self.var_name.set("")
        self.var_price.set(0)
        self.var_quantity.set(0)
        self.var_article.set(0)
        self.var_findBy1.set("")
        self.var_findByText1.set(0)
        self.var_item.set(0)
        self.var_name2.set("")
        self.var_condition.set(0)
        self.var_limit.set(0)
        self.var_procurment.set(0)
        self.var_findBy2.set("")
        self.var_findByText2.set(0)
        self.print.delete(*self.print.get_children()),
        self.print2.delete(*self.print2.get_children())
    
    def signingupNewItem(self):
        if self.var_name2.get()=="" or self.var_condition.get()==0 or self.var_limit.get()==0:
            messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
            try:
                con=Konekcija.getInstance()
                cursor=con.cursor()
                cursor.execute("INSERT INTO artikli(naziv,stanjeKgLiKom,nabavkaRobe) VALUES(%s,%s,%s)",(
            self.var_name2.get(),
            self.var_condition.get(),
            self.var_limit.get()
            ))
                con.commit()
                messagebox.showinfo("OK","Item add successfully",parent=self.root)
                self.reset()
                self.showItems()

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong :{es}",parent=self.root)

    def addCondition(self):
        if self.var_item.get()==0:
            messagebox.showerror("Error","Please,enter id of item",parent=self.root)
        else:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            cursor.execute("UPDATE artikli SET stanjeKgLiKom=%s,nabavkaRobe=%s WHERE idartikli=%s",(
                float(self.var_condition.get())+(self.var_procurment.get()),
                self.var_limit.get(),
                self.var_item.get()
            ))
            self.var_condition.set(float(self.var_condition.get())+(self.var_procurment.get()))
            self.var_procurment.set(0)
            con.commit()
            messagebox.showinfo("OK","Procurment successfull",parent=self.root)
            self.showItems()

    
    def deleteItem(self):
        obriši=messagebox.askyesno("Restaurant","Do You really want to delete this item?")
        if obriši>0:
            con=Konekcija.getInstance()
            cursor=con.cursor()
            query=("DELETE FROM artikli WHERE idartikli=%s")
            value=(self.var_item.get(),)
            cursor.execute(query,value)
        elif  not obriši:
            return
        con.commit()
        messagebox.showinfo("Success","Item deleted successfully ",parent=self.root)
        self.reset()
        self.showItems()


    def date(self):
        now = strftime("%Y-%m-%d %H:%M:%S")
        self.lbl.config(text = now)
        self.lbl.after(1000, self.date)


    def closeWindow(self):
        response=messagebox.askyesno('Exit','Are you sure yo want to exit?',parent=self.root)
        if response:
            self.root.destroy()

'''root=Tk()
object=PriceProcurment(root)
mainloop()'''

