from tkinter import *
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
from Center import CenterPage
import sqlite3
from jsonFileHandeler import jsonfilehandeler

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from patient """)
PatientList = cursor.fetchall()
conn.commit()
conn.close()

class Addrecord:
    entry_Problem = None
    entry_Date = None
    entry_Medicine = None
    entry_Note = None

    def __init__(self, id, doctorId):
        self.id = id
        self.name = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        x = 50
        y = 5
        Label(self.root, text="Add record", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=260, y=y+15)
        for i in PatientList:
            if i[0] == self.id:
                self.name = i[1]

        Label(self.root, text=self.name, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=300, y=y + 50)
        Label(self.root, text="Problem title", font=("Ubuntu", 10), fg="#707070", bg="white").place(x=x, y=y + 90)
        self.entry_Problem = ttk.Entry(self.root, width=30)
        self.entry_Problem.place(x=x+5, y=y + 120)
        Label(self.root, text="Date", font=("Ubuntu", 10), fg="#707070", bg="white").place(x=390, y=y + 90)
        self.entry_Date = ttk.Entry(self.root, width=30)
        self.entry_Date.place(x=x+345, y=y + 120)
        Label(self.root, text="Medicine", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=y + 170)
        self.entry_Medicine = Text(self.root, height=4, width=50, bd=2)
        self.entry_Medicine.place(x=x + 85, y=y + 170)
        Label(self.root, text="Note", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=y + 260)
        self.entry_Note = Text(self.root, height=5, width=50, bd=2)
        self.entry_Note.place(x=x + 85, y=y + 270)
        Button(self.root, text="Add", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=self.add_details
                   ).place(x=290, y=y + 390)

    def add_details(self):
        record = dict()
        record["DesName"] = self.entry_Problem.get()
        record["Date"] = self.entry_Date.get()
        record["Medicine"] = self.entry_Medicine.get("1.0", END)
        record["note"] = self.entry_Note.get("1.0", END)
        if record["DesName"] == "":
            messagebox.showinfo(title='Error', message="Please Enter Diseases name")
        elif record["Date"] == "":
            messagebox.showinfo(title='Error', message="Please Enter Date")
        else:
            jsonfilehandeler(record, self.id, self. name)
            self.root.destroy()


if __name__ == '__main__':
    Addrecord("192-65443")