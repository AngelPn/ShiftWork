class Settings:
    def __init__(self):
        self.month = ""
        self.files_path = []

    def set_month(self, m): self.month = m
    def set_files_path(self, fp): self.files_path.append(fp)

s = Settings()

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('600x400')
window.title("Welcome to ShiftWork app")

#Intro
txt = "Εφαρμογή που υπολογίζει τα μηνιαία shift works των υπαλλήλων"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 0)

#Question 1
txt = "Ποιος είναι ο μήνας του οποίου θέλετε να υπολογιστεί το shift work;"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 2)

combo = Combobox(window, width = 15)
combo['values']= ("Ιανουάριος","Φεβρουάριος","Μάρτιος","Απρίλιος","Μάιος","Ιούνιος","Ιούλιος","Αύγουστος","Σεπτέμβριος","Οκτώβριος","Νοέμβριος","Δεκέμβριος")
combo.current(0) #set the selected item
combo.grid(column=0, row=3)
def set_values():
    s.set_month(combo.get())
    window.destroy()

#Question 2
from tkinter.filedialog import askopenfiles

def open_files():
    files = askopenfiles(mode ='r', filetypes =[('Excel Files', '*.xls')])
    x = 0
    while x < len(files):
        s.set_files_path(files[x].name)
        x += 1
    txt = "Τα αρχεία είναι έτοιμα!"
    lbl = Label(window, text = txt, font = ("Arial", 12))
    lbl.grid(column = 0, row = 5)
    value_button = Button(window, text = 'OK', width = 4, command = set_values)#set values
    value_button.grid(column = 1, row = 5)

files_button = Button(window, text = 'Επίλεξε τα αρχεία', width = 20, command = open_files)
files_button.grid(column = 0, row = 4)

window.mainloop()

months = {
    "Ιανουάριος" : "01",
    "Φεβρουάριος": "02",
    "Μάρτιος" : "03",
    "Απρίλιος" : "04",
    "Μάιος" : "05",
    "Ιούνιος" : "06",
    "Ιούλιος" : "07",
    "Αύγουστος" : "08",
    "Σεπτέμβριος" : "09",
    "Οκτώβριος" : "10",
    "Νοέμβριος" : "11",
    "Δεκέμβριος" : "12"
}

import ShiftWork

for x in s.files_path:
    ShiftWork.read_xl(x, months[s.month])

ShiftWork.print_data()

import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet("WorkShift")
ws.write(0, 2 , "Νυχτερινές ώρες")
ws.write(0, 3 , "Ώρες Κυριακής")
ws.write(0, 4 , "Ημέρες αναρρωτικής άδειας")
ws.write(0, 5 , "Ημέρες άδειας")

employeesList = []
for value in ShiftWork.employees_shiftwork.values():
    employeesList.append(value)
    
for row_idx in range(1, len(employeesList)-1):
    ws.write(row_idx, 0, employeesList[row_idx - 1].name)
    ws.write(row_idx, 1, employeesList[row_idx - 1].surname)
    ws.write(row_idx, 2, employeesList[row_idx - 1].NightHours)
    ws.write(row_idx, 3, employeesList[row_idx - 1].SundayHours)
    ws.write(row_idx, 4, employeesList[row_idx - 1].NoSickness)
    ws.write(row_idx, 5, employeesList[row_idx - 1].NoLicense)

wb.save("shiftwork.xls")

