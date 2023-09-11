from tkinter import *
from tkinter import ttk
from Center import CenterPage
import jsonFileHandeler
PreRecordList = jsonFileHandeler.read_from_json()


class Prerecord:
    def __init__(self, id):
        self.id = id
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")
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
                Label(self.root, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=self.y)
                Label(self.root, text="This patient has no record", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=220, y=self.y + 50)
            else:
                frame = Frame(self.root, bg="white")
                frame.pack()

                Label(frame, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").pack(pady=10)
                Label(frame, text=record["Name"], font=("Ubuntu", 12), fg="#707070", bg="white").pack()

                main_frame = Frame(self.root, bg="white")
                main_frame.pack(fill=BOTH, expand=True, pady=15)
                second_frame = self.canva(main_frame)

                for i in record["RecordList"]:
                    Label(second_frame, text=i["DesName"], font=("Ubuntu Bold", 12), fg="#707070", bg="white").pack(side=TOP, padx=30, pady=5, anchor=NW)
                    Label(second_frame, text="Last Check Up date: " + i["Date"], font=("Ubuntu", 12), fg="#707070", bg="white").pack(side=TOP, padx=30, pady=3,
                                                                                      anchor=NW)
                    Label(second_frame, text="Medicine: " + "\n" + i["Medicine"], font=("Ubuntu", 12), fg="#707070", bg="white", justify=LEFT).pack(side=TOP, padx=30, pady=3, anchor=NW)
                    Label(second_frame, text="Note: " + "\n" + i["note"], font=("Ubuntu", 12), fg="#707070", bg="white", justify=LEFT, wraplength=550).pack(side=TOP, padx=30, anchor=NW)





    def canva(self, main_frame):
        my_canvas = Canvas(main_frame, bg="white")
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas, bg="white")
        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
        return second_frame


if __name__ == '__main__':
    Prerecord("192-65443")
