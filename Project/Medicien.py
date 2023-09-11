from tkinter import *
from tkinter import ttk
from Center import CenterPage
from jsonFileHandeler import jsonfilehandeler
import jsonFileHandeler
PreRecordList = jsonFileHandeler.read_from_json()


class MedicineClass:
    def __init__(self, id):
        self.id = id
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="White")
        self.y = 20
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        if PreRecordList is None:
            Label(self.root, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=20)
            Label(self.root, text="No record is added", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=245, y=self.y + 50)
        else:
            record = None
            for i in PreRecordList:
                if i['ID'] == self.id:
                    record = i

            if record is None:
                Label(self.root, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250,
                                                                                                                y=self.y)
                Label(self.root, text="This patient has no record", font=("Ubuntu", 12), fg="#707070",
                      bg="white").place(x=220, y=self.y + 50)
            else:
                Label(self.root, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=20)
                Label(self.root, text=record["Name"], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=300, y=self.y + 50)
                Label(self.root, text="Current Medicine", font=("Ubuntu Bold", 12), fg="#707070", bg="white").place(x=30, y=self.y + 90)
                l = len(record["RecordList"]) - 1
                medicienList = record["RecordList"][l]["Medicine"].split('\n')
                gap = 130
                for i in medicienList:
                    Label(self.root, text=i, font=("Ubuntu", 12), fg="#707070", bg="white", justify=LEFT).place(x=30, y=self.y + gap)
                    gap += 30



if __name__ == '__main__':
    MedicineClass("192-65443")