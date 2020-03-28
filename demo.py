class Settings:
    def __init__(self):
        self.no_work_timesheets = 0
        self.day_start = 1
        self.day_end = 1
        self.no_segments = 0
        self.lines = {}

    def get_no_work_timesheets(self):
        return self.no_work_timesheets

    def set_wt(self, n): self.no_work_timesheets = n
    def set_days_start(self, ds): self.day_start = ds
    def set_days_end(self, de): self.day_end = de
    def set_segments(self, ns): self.no_segments = ns
    def set_lines(self, lines):
        i = 0
        for x in lines.values():
            self.lines[i] = x
            i += 1
    def print_data(self):
        txt = "WT= {}\nDay Start= {}\nDay End= {}\nSegments= {}\nLines:"
        print(txt.format(self.no_work_timesheets, self.day_start, self.day_end, self.no_segments))
        for x in self.lines:
            print(x)
            value = self.lines[x]
            for y in value:
                print(y)

s = Settings()

def clicked_wt1():
    s.set_wt(4)
    s.print_data()
def clicked_wt2():
    s.set_wt(5)
    s.print_data()
def clicked_wt3():
    s.set_wt(6)
    s.print_data()
def set_values():
    s.set_days_start(combo1.get())
    s.set_days_end(combo2.get())
    s.set_segments(combo3.get())
    s.print_data()

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
txt = "How many weekly work timesheets has this month?"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 4)
rad1 = Radiobutton(window, text = 4, value = 1, command = clicked_wt1)
rad2 = Radiobutton(window, text = 5, value = 2, command = clicked_wt2)
rad3 = Radiobutton(window, text = 6, value = 3, command = clicked_wt3)
rad1.grid(column = 0, row = 5)
rad2.grid(column = 1, row = 5)
rad3.grid(column = 2, row = 5)


#Question 2
txt = "What are the dates that cover the weekly work timesheets?"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 9)

lbl = Label(window, text = "From: ", font = ("Arial", 12))
lbl.grid(column = 0, row = 10)

combo1 = Combobox(window, width = 2)
combo1['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
combo1.current(0) #set the selected item
combo1.grid(column=1, row=10)

lbl = Label(window, text = "/", font = ("Arial", 12))
lbl.grid(column = 2, row = 10)

combo = Combobox(window, width = 2)
combo['values']= (1,2,3,4,5,6,7,8,9,10,11,12)
combo.current(0) #set the selected item
combo.grid(column=3, row=10)

lbl = Label(window, text = "to: ", font = ("Arial", 12))
lbl.grid(column = 4, row = 10)

combo2 = Combobox(window, width = 2)
combo2['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
combo2.current(0) #set the selected item
combo2.grid(column=5, row=10)

lbl = Label(window, text = "/", font = ("Arial", 12))
lbl.grid(column = 6, row = 10)

combo = Combobox(window, width = 2)
combo['values']= (1,2,3,4,5,6,7,8,9,10,11,12)
combo.current(0) #set the selected item
combo.grid(column=7, row=10)

#Question 3
txt = "How many segments of employees exist?"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 11)

combo3 = Combobox(window, width = 2)
combo3['values']= (1,2,3,4,"Text")
combo3.current(0) #set the selected item
combo3.grid(column=0, row=12)

#Question 4
txt = "At which row in every excel file begin and end the segments of employees?"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 13)

def checked_diff():
    x = 0
    print(s.get_no_work_timesheets())
    i = 0
    while x < s.get_no_work_timesheets():
        txt = "Excel file #{} :"
        lbl = Label(window, text = txt.format(x + 1), font = ("Arial", 12))
        lbl.grid(column = 0, row = 15 + x + i*int(combo3.get()))
        i = 0
        while i < int(combo3.get()):
            txt = "Segment #{} begins at row "
            lbl = Label(window, text = txt.format(i + 1), font = ("Arial", 12))
            lbl.grid(column = 1, row = 15 + x + i + 1)

            txt = Entry(window, width= 3)
            txt.grid(column=2, row = 15 + i)

            txt = " and ends at row "
            lbl = Label(window, text = txt.format(i), font = ("Arial", 12))
            lbl.grid(column = 3, row = 15 + x + i + 1)

            txt = Entry(window, width= 3)
            txt.grid(column=4, row = 15 + x + i + 1)
            i += 1
        x += 1

list_segments = []
def clicked(i):
    list_segments.append(entry1.get())
    list_segments.append(entry2.get())
    checked_same(i + 1)

def checked_same(i):
    if i < int(combo3.get()):
        txt = "Segment #{} begins at row "
        lbl = Label(window, text = txt.format(i+1), font = ("Arial", 12))
        lbl.grid(column = 0, row = 15 + i)

        global entry1
        entry1 = Entry(window, width= 3)
        entry1.grid(column=1, row = 15 + i)

        txt = " and ends at row "
        lbl = Label(window, text = txt, font = ("Arial", 12))
        lbl.grid(column = 2, row = 15 + i)

        global entry2
        entry2 = Entry(window, width= 3)
        entry2.grid(column=3, row = 15 + i)

        ok_button = Button(window, text='OK', width = 4, command = lambda : clicked(i))
        ok_button.grid(column=4, row=15 + i)
        print(i)
        s.lines["Excel1"] = list_segments
    else:
        txt = "OK"
        lbl = Label(window, text = txt.format(i+1), font = ("Arial", 12))
        lbl.grid(column = 0, row = 15 + i)

chk_state_same = IntVar()
chk_state_same.set(0) #set uncheck
chk_state_diff = IntVar()
chk_state_diff.set(0) #set uncheck
chk = Checkbutton(window, text='Same in every excel file', width = 25, var=chk_state_same, command = lambda : checked_same(0))
chk.grid(column=0, row=14)
chk = Checkbutton(window, text='Different in every excel file', width = 25, var=chk_state_diff, command = checked_diff)
chk.grid(column=1, row=14)

#set values
value_button = Button(window, text = 'Ready! Set Settings', width = 20, command = set_values)
value_button.grid(column = 0, row = 30)


s.print_data()
window.mainloop()

