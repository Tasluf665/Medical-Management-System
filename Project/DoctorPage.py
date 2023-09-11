from tkinter import *
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
from Center import CenterPage
from PreRecord import Prerecord
from AddRecord import Addrecord

import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from doctor where password='admin' """)
DoctorList = cursor.fetchall()
cursor.execute(""" select * from patient where password='admin' """)
PatientList = cursor.fetchall()
conn.commit()
conn.close()


class Doctor:
    def __init__(self, id):
        self.entry_id = None
        self.entry_password = None

        self.id = id
        self.name = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="White")
        self.y = 60
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        Label(self.root, text="Doctor Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=20)
        for i in DoctorList:
            if i[0] == self.id:
                self.name = i[1]
        Label(self.root, text="Name: " + self.name, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=150, y=self.y + 40)
        Label(self.root, text="Doctor Id: " + self.id, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=150, y=self.y + 70)

        Label(self.root, text="Patient ID", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=150, y=self.y + 110)
        self.entry_id = ttk.Entry(self.root, width=30)
        self.entry_id.place(x=250, y=self.y + 115)

        Label(self.root, text="Password", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=150, y=self.y + 160)
        self.entry_password = ttk.Entry(self.root, width=30, show="*")
        self.entry_password.place(x=250, y=self.y + 165)

        Button(self.root, text="Pre Record", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=lambda: self.getIdPassword("pre")
                   ).place(x=180, y=self.y + 240)

        Button(self.root, text="Add Record", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=lambda: self.getIdPassword("add")
                   ).place(x=330, y=self.y + 240)

    def getIdPassword(self, track):
        id = self.entry_id.get()
        password = self.entry_password.get()
        self.Authentication(id, password, track)

    def Authentication(self, id, password, track):
        id_first = id.split("-")
        if id_first[0] == "192":
            for i in PatientList:
                if i[0] == id and i[2] == password:
                    if track == "pre":
                        self.root.destroy()
                        Prerecord(id)
                    elif track == "add":
                        Addrecord(id, self.id)
                    return
            else:
                messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        else:
            messagebox.showinfo(title='Error', message="Id or Password is incorrect")

if __name__ == '__main__':
    Doctor("191-45042")