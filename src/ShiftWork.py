class Settings:
    def __init__(self):
        self.month = ""
        self.holidays = []
        self.files_path = []

    def set_month(self, m): self.month = m
    def set_holidays(self, h): self.holidays = h
    def set_files_path(self, fp): self.files_path.append(fp)

s = Settings()

import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.iconbitmap("app/sw.ico")
window.geometry('700x200')
window.configure(background = "#181717")
window.title("ShiftWork")
lbl = ttk.Label(window, text = " ", background = "#181717")
lbl.grid(row = 0)

#Question 1
txt = "Επίλεξε μήνα"
lbl = ttk.Label(window, text = txt, font = ("Arial", 12), foreground = "#BFCFE2", background = "#181717")
lbl.grid(column = 0, row = 1)

# This will create style object 
style = ttk.Style()
style.configure('TCombobox', foreground = "#181717", bg = "red") 
default_values = ["Ιανουάριος","Φεβρουάριος","Μάρτιος","Απρίλιος","Μάιος","Ιούνιος","Ιούλιος","Αύγουστος","Σεπτέμβριος","Οκτώβριος","Νοέμβριος","Δεκέμβριος"]

combo = ttk.Combobox(window, values = default_values, style = 'TCombobox', width = 12 )
combo.master.option_add( '*TCombobox*Listbox.background', '#181717')
combo.master.option_add( '*TCombobox*Listbox.foreground', '#BFCFE2')
combo.master.option_add( '*TCombobox*Listbox.selectBackground','#BFCFE2') #does not work
combo.master.option_add( '*TCombobox*Listbox.selectForeground','#181717') #does not work  
combo.grid(column = 1, row = 1)
def set_values():
    s.set_month(combo.get())
    window.destroy()

#Question 2
txt_holidays = "    Οι αργίες 01/01, 06/01, 25/03, 01/05, 15/08, 28/10, 25/12, 26/12 υπολογίζονται αυτόματα."
lbl = ttk.Label(window, text = txt_holidays, font = ("Arial", 12), foreground = "#BFCFE2", background = "#181717")
lbl.grid(column = 0, columnspan = 12, row = 3)

txt = "Έχει ο μήνας επιπλέον αργίες;"
lbl = ttk.Label(window, text = txt, font = ("Arial", 12), foreground = "#BFCFE2", background = "#181717")
lbl.grid(column = 0, columnspan = 2, row = 4)

def get_holidays():
    txt = "Γράψε τις αργίες:"
    lbl = ttk.Label(window, text=txt, font=("Arial", 12), foreground="#BFCFE2", background="#181717")
    lbl.grid(column = 0, row = 5)

    holidays_input = tk.StringVar()

    def set_holidays():
        selected_holidays = [holiday.strip() for holiday in holidays_input.get().split(",")]
        s.set_holidays(selected_holidays)

    holidays_entry = tk.Entry(window, textvariable = holidays_input, font=("Arial", 12), width = 6)
    holidays_entry.grid(column = 1, row = 5)

    holiday_button = tk.Button(window, 
                               text='OK',
                               font=("Calibri", 10, "bold"),
                               foreground="#181717",
                               background="#BFCFE2",
                               width=4,
                               command=set_holidays)  # set holiday
    holiday_button.grid(column=2, row = 5)

def toggle_holidays():
    if holidaySelected.get() == 1:  # If the checkbox is selected
        get_holidays()
    else:  # If the checkbox is deselected
        for widget in window.grid_slaves(row=5):
            widget.grid_remove()  # Hide all widgets in row 5

holidaySelected = tk.IntVar()
check1 = tk.Checkbutton(window,
    text = "Ναι",
    font = ("Arial", 12),
    foreground = "#BFCFE2", 
    background = "#181717",
    variable = holidaySelected,
    command = toggle_holidays)
check1.grid(column = 2, row = 4)

#Question 3
from tkinter.filedialog import askopenfiles

def open_files():
    files = askopenfiles(mode ='r', filetypes =[('Excel Files', '*.xls')])
    x = 0
    while x < len(files):
        s.set_files_path(files[x].name)
        x += 1
    txt = "Τα αρχεία είναι έτοιμα!"
    lbl = ttk.Label(window, text = txt, font = ("Arial", 12), foreground = "#BFCFE2", background = "#181717")
    lbl.grid(column = 0, row = 6)
    value_button = tk.Button(window, 
        text = 'OK',
        font = ("Calibri", 10, "bold"),
        foreground = "#181717",
        background = "#BFCFE2",
        width = 4,
        command = set_values)#set values
    value_button.grid(column = 1, row = 7)

files_button = tk.Button(window, 
    text = 'Upload files',
    activebackground = "#181717",
    activeforeground = "#BFCFE2",
    background = "#BFCFE2",
    foreground = "#181717",
    width = 11,
    command = open_files )
files_button.grid(column = 0, row = 7)

col_count, row_count = window.grid_size()
for row in range(1,row_count):
    window.grid_rowconfigure(row, minsize=20)
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

import xl_parsing

hasHoliday = False

for x in s.files_path:
    if (xl_parsing.read_xl(x, months[s.month], s.holidays)):
        hasHoliday = True

import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet("ShiftWork")
ws.col(0).width = 256 * 20  # 20 characters wide (-ish)
ws.col(1).width = 256 * 15  # 15 characters wide (-ish)
for col_idx in range(2, 9):
    ws.col(col_idx).width = 256 * 13
tall_style = xlwt.easyxf('font:height 720;') # 36pt
ws.row(0).set_style(tall_style)

header_style = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')
ws.write(0, 2 , "Νύκτα", header_style) # NightHours
ws.write(0, 3 , "Νύκτα Κυριακής", header_style) # SundayNightHours
ws.write(0, 4 , "Ημέρα Κυριακής", header_style) # SundayHours
ws.write(0, 5 , "Πλήθος Κυριακών", header_style) # TotalSunday
ws.write(0, 6 , "Μέρες ασθένειας", header_style) # NoSickness
ws.write(0, 7 , "Μέρες άδειας", header_style) # NoLicense

employeesList = []
for value in xl_parsing.employees_shiftwork.values():
    employeesList.append(value)

data_style = xlwt.easyxf('align: wrap on, vert centre, horiz center')
for row_idx in range(1, len(employeesList) + 1):
    ws.write(row_idx, 0, employeesList[row_idx - 1].name, data_style)
    ws.write(row_idx, 1, employeesList[row_idx - 1].surname, data_style)
    ws.write(row_idx, 2, employeesList[row_idx - 1].NightHours, data_style)
    ws.write(row_idx, 3, employeesList[row_idx - 1].SundayNightHours, data_style)
    ws.write(row_idx, 4, employeesList[row_idx - 1].SundayHours, data_style)
    ws.write(row_idx, 5, employeesList[row_idx - 1].TotalSunday, data_style)
    ws.write(row_idx, 6, employeesList[row_idx - 1].NoSickness, data_style)
    ws.write(row_idx, 7, employeesList[row_idx - 1].NoLicense, data_style)

if (hasHoliday):
    ws.write(0, 8 , "Ημέρα Αργίας", header_style) 
    ws.write(0, 9, "Νύκτα Αργίας", header_style) 
    ws.write(0, 10, "Σύνολο ημέρας Κυριακής-Αργίας", header_style) 
    ws.write(0, 11, "Σύνολο νύκτας Κυριακής-Αργίας", header_style) 
    for row_idx in range(1, len(employeesList) + 1):
        ws.write(row_idx, 8, employeesList[row_idx - 1].HolidayHours, data_style)
        ws.write(row_idx, 9, employeesList[row_idx - 1].HolidayNightHours, data_style)
        ws.write(row_idx, 10, employeesList[row_idx - 1].HolidayHours + employeesList[row_idx - 1].SundayHours, header_style)
        ws.write(row_idx, 11, employeesList[row_idx - 1].HolidayNightHours + employeesList[row_idx - 1].SundayNightHours, header_style)

ws2 = wb.add_sheet("Ημερομηνίες Άδειας")
ws2.col(0).width = 256 * 20  # 20 characters wide (-ish)
for col_idx in range(1, 7):
    ws2.col(col_idx).width = 256 * 13

for row_idx in range(0, len(employeesList)):
    ws2.write(row_idx, 0, employeesList[row_idx].name, data_style)
    ws2.write(row_idx, 1, employeesList[row_idx].surname, data_style)
    col_idx = 2
    for x in employeesList[row_idx].LicenseDates:
        ws2.write(row_idx, col_idx,  x.strftime("%x"), data_style)
        col_idx += 1

dir_path = s.files_path[0]
save_path = dir_path + "/../" + s.month + ".xls"
wb.save(save_path)