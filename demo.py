class Settings:
    def __init__(self):
        self.no_work_timesheets = 0
        self.month = ""
        self.files_path = []

    def set_wt(self, n): self.no_work_timesheets = n
    def set_month(self, m): self.month = m
    def set_files_path(self, fp): self.files_path.append(fp)
    def print_data(self):
        txt = "WT= {}\nMonth= {}\nFiles:"
        print(txt.format(self.no_work_timesheets, self.month))
        for x in self.files_path:
            print(x)

s = Settings()

def clicked_wt1(): s.set_wt(4)
def clicked_wt2(): s.set_wt(5)
def clicked_wt3(): s.set_wt(6)
def set_values(): s.set_month(combo.get())

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('900x600')
window.title("Welcome to ShiftWork app")

#Intro
txt = "An application that calculates the monthly shift works of employees"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 0)

#Question 1
txt = "Πόσες εβδομάδες έχει ο μήνας;"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 4)
rad1 = Radiobutton(window, text = 4, value = 1, command = clicked_wt1)
rad2 = Radiobutton(window, text = 5, value = 2, command = clicked_wt2)
rad3 = Radiobutton(window, text = 6, value = 3, command = clicked_wt3)
rad1.grid(column = 0, row = 5)
rad2.grid(column = 1, row = 5)
rad3.grid(column = 2, row = 5)

#Question 2
txt = "Ποιος είναι ο μήνας του οποίου θέλετε να υπολογιστεί το shift work;"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 9)

combo = Combobox(window, width = 15)
combo['values']= ("Ιανουάριος","Φεβρουάριος","Μάρτιος","Απρίλιος","Μάιος","Ιούνιος","Ιούλιος","Αύγουστος","Σεπτέμβριος","Οκτώβριος","Νοέμβριος","Δεκέμβριος")
combo.current(0) #set the selected item
combo.grid(column=1, row=10)

#Question 4
from tkinter.filedialog import askopenfiles

def open_files():
    files = askopenfiles(mode ='r', filetypes =[('Excel Files', '*.xls')])
    x = 0
    while x < len(files):
        s.set_files_path(files[x].name)
        x += 1

files_button = Button(window, text = 'Select Files', width = 10, command = open_files)
files_button.grid(column = 0, row = 11)

#set values
value_button = Button(window, text = 'Ready! Set Settings', width = 20, command = set_values)
value_button.grid(column = 0, row = 30)

window.mainloop()
s.print_data()

import ShiftWork

