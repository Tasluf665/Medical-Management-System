from tkinter import *
from tkinter import Button
from tkinter import ttk
from tkinter import messagebox
from DoctorPage import Doctor
from PatientPage import Patient
from Center import CenterPage
import sqlite3
from Pharmacy import pharmacyPage

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from doctor """)
DoctorList = cursor.fetchall()
cursor.execute(""" select * from patient """)
PatientList = cursor.fetchall()
cursor.execute(""" select * from pharmacy """)
PharmacyList = cursor.fetchall()

conn.commit()
conn.close()


class LoginPage:
    def __init__(self):
        y = 80
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")

        Label(self.root, text="Login Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=40)
        Label(self.root, text="ID", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=200, y=y+30)
        self.entry_id = ttk.Entry(self.root, width=30)
        self.entry_id.place(x=205, y=y+60)
        Label(self.root, text="Password", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=200, y=y+100)
        self.entry_password = ttk.Entry(self.root, width=30, show="*")
        self.entry_password.place(x=205, y=y+130)
        Button(self.root, text="Login", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                            command=self.getIdPassword
                            ).place(x=270, y=y+180)

        CenterPage(self.root)
        self.root.mainloop()


    def getIdPassword(self):
        id = self.entry_id.get()
        password = self.entry_password.get()
        self.Authentication(id, password)

    def Authentication(self, id, password):
        id_first = id.split("-")
        if id_first[0] == "191":
            for i in DoctorList:
                if i[0] == id and i[2] == password:
                    self.root.destroy()
                    Doctor(id)
                    return
            else:
                messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        elif id_first[0] == "192":
            for i in PatientList:
                if i[0] == id and i[2] == password:
                    self.root.destroy()
                    Patient(id)
                    return
            else:
                messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        elif id_first[0] == "193":
            for i in PharmacyList:
                if i[0] == id and i[2] == password:
                    self.root.destroy()
                    pharmacyPage(id, i[1])
                    return
            else:
                messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        else:
            messagebox.showinfo(title='Error', message="Id or Password is incorrect")


if __name__ == '__main__':
    LoginPage()

