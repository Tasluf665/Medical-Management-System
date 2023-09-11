from tkinter import *
from tkinter import ttk
from tkinter import Button
from Center import CenterPage
from PreRecord import Prerecord
from Medicien import MedicineClass
import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from patientDetails """)
PatientList = cursor.fetchall()
conn.commit()
conn.close()

class Patient:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")
        self.y = 30
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        Label(self.root, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=20)
        patient = dict()
        for i in PatientList:
            if i[0] == self.id:
                patient = i
        x = 50
        Label(self.root, text="Name: " + patient[1], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=self.y + 40)
        Label(self.root, text="Patient ID: " + patient[0], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=self.y + 70)
        Label(self.root, text="Blood Group: " + patient[2], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=self.y + 100)
        Label(self.root, text="Phone: " + patient[3], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=self.y + 130)
        Label(self.root, text="Height: " + patient[4], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=self.y + 160)
        Label(self.root, text="Weight: " + str(patient[5]) + " kg", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=self.y+190)
        Label(self.root, text="Current address: " + patient[6], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=self.y+220)
        Label(self.root, text="Permanent address: " + patient[7], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=self.y+250)
        Button(self.root, text="Pre Record", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=self.preRecord
                   ).place(x=x+110, y=self.y + 340)
        Button(self.root, text="Medicine", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=self.medicine
                   ).place(x=x + 300, y=self.y + 340)

    def preRecord(self):
        self.root.destroy()
        Prerecord(self.id)

    def medicine(self):
        self.root.destroy()
        MedicineClass(self.id)


if __name__ == '__main__':
    Patient("192-65442")

