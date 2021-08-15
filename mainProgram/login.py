from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
from mysql.connector import cursor
from registration import Registration
from hotel import Hotel
from veza import Konekcija


def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Program")
        self.root.geometry("1850x1050+0+0")

        self.root.protocol('WM_DELETE_WINDOW', self.exit)

        self.var_email = StringVar()
        self.var_password = StringVar()

        img1 = Image.open(r"beachPhoto/beach.png")
        img1 = img1.resize((1850, 1050), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblImage1 = Label(self.root, image=self.photoimg1)
        lblImage1.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="blue")
        frame.place(x=760, y=220, width=340, height=450)

        img2 = Image.open(r"userLoginPhoto/user1.png")
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblImage2 = Label(image=self.photoimg2, bg="blue", borderwidth=0)
        lblImage2.place(x=880, y=225, width=100, height=100)

        titleLbl = Label(frame, text="Log In", font=("times new roman", 20, "bold"), fg="white", bg="blue")
        titleLbl.place(x=90, y=100)

        emailLbl = Label(frame, text="E-mail", font=("times new roman", 15, "bold"), fg="white", bg="blue")
        emailLbl.place(x=70, y=155)

        self.textEmail = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.textEmail.place(x=40, y=180, width=280)

        passwordLbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="blue")
        passwordLbl.place(x=70, y=225)

        self.textpassword = ttk.Entry(frame, textvariable=self.var_password, show="*", font=("times new roman", 15, "bold"))
        self.textpassword.place(x=40, y=250, width=270)

        img3 = Image.open(r"userLoginPhoto/user1.png")
        img3 = img3.resize((35, 35), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblImage3 = Label(image=self.photoimg3, bg="blue", borderwidth=0)
        lblImage3.place(x=767, y=367, width=35, height=35)

        img4 = Image.open(r"userLoginPhoto/user1.png")
        img4 = img4.resize((35, 35), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblImage4 = Label(image=self.photoimg4, bg="blue", borderwidth=0)
        lblImage4.place(x=767, y=439, width=35, height=35)

        btnLogin = Button(frame, text="Log In", command=self.login, font=("times new roman", 15, "bold"),bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="green", activebackground="yellow")
        btnLogin.place(x=110, y=300, width=120, height=35)

        btnRegister = Button(frame, text="Registration", command=self.registration_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="blue", activeforeground="white", activebackground="brown")
        btnRegister.place(x=15, y=350, width=160)

        btnRegister2= Button(frame, text="Forgotten  password", command=self.forgotten_password, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="blue", activeforeground="white", activebackground="brown")
        btnRegister2.place(x=15, y=380, width=160)


    def registration_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Registration(self.new_window)

    def login(self):
        if self.textEmail.get() == "" or self.textpassword.get() == "":
            messagebox.showerror("Error", "All fields must be filled!")
        else:
            con=Konekcija.getInstance()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM zaposleni WHERE email=%s and lozinka=%s", (
                self.var_email.get(),
                self.var_password.get()
            ))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Wrong data,try again")
            else:
                open_main = messagebox.askyesno("Yes No", "Acces to  main program")
                self.var_email.set("")
                self.var_password.set("")
                if open_main:  
                    self.new_window = Toplevel(self.root)
                    self.app = Hotel(self.new_window)
                else:
                    if not open_main:
                        return
            con.commit()

    def change_password(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select a security question ", parent=self.root2)
        elif self.security_A.get() == "":
            messagebox.showerror("Error", "Please,enter the answer", parent=self.root2)
        elif self.txt_newpassword.get() == "":
            messagebox.showerror("Error", "Enter the new password", parent=self.root2)
        else:
            con=Konekcija.getInstance()
            cursor = con.cursor()
            query = ("SELECT * FROM zaposleni WHERE email=%s and security_question=%s and security_answer=%s")
            value = (self.textEmail.get(),self.combo_security_Q.get(), self.security_A.get())
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please,enter the correct answer", parent=self.root2)
            else:
                query = ("UPDATE zaposleni SET lozinka=%s WHERE email=%s")
                value = (self.txt_newpassword.get(), self.textEmail.get())
                cursor.execute(query, value)
                con.commit()
                messagebox.showinfo("Info", "Your password has changed,Please login again", parent=self.root2)
                self.root2.destroy()
                self.var_email.set("")
                self.var_password.set("")

    def forgotten_password(self):
        if self.textEmail.get() == "":
            messagebox.showerror("Error", "Please,enter Your e-mail and Your password")
        else:
            con=Konekcija.getInstance()
            cursor = con.cursor()
            query = ("SELECT * FROM zaposleni WHERE email=%s")
            value = (self.textEmail.get(),)
            cursor.execute(query, value)
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter valid password")
            else:
                self.root2 = Toplevel()
                self.root2.title("Forgotten  password")
                self.root2.geometry("340x450+830+270")

                lbL = Label(self.root2, text="Forgotten  password", font=("times new roman", 20, "bold"), fg="blue", bg="white")
                lbL.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q['values'] = ("Select", "Mesto rodjenja", "Kućni ljubimac", "Ime bake")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current()

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_A.place(x=50, y=150)

                self.security_A = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.security_A.place(x=50, y=180, width=250)

                newpassword = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), fg="black", bg="white")
                newpassword.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Change", command=self.change_password, font=("times new roman", 15, "bold"), fg="white", bg="blue")
                btn.place(x=130, y=290)

    def exit(self):
        response = messagebox.askyesno("Exit", "Are you sure yo want to exit?",parent=self.root)
        if response:
            self.root.destroy()



main()
