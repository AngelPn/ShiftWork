class Settings:
    def __init__(self):
        self.no_work_timesheets = 0
        self.day_start = 0
        self.day_end = 0
        self.no_segments = 0
        self.lines = ()

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
        txt = "WT= {}\nDay Start= {}\nDay End= {}\nSegments= {}\n"
        print(txt.format(self.no_work_timesheets, self.day_start, self.day_end, self.no_segments))

s = Settings()

def clicked_wt1():
    s.set_wt(4)
def clicked_wt2():
    s.set_wt(5)
def clicked_wt3():
    s.set_wt(6)

from tkinter import *

window = Tk()
window.geometry('700x600')
window.title("Welcome to ShiftWork app")

txt = "An application that calculates the monthly shift works of employees"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 0)

txt = "How many weekly work timesheets has this month?"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 4)
rad1 = Radiobutton(window, text = 4, value = 1, command = clicked_wt1)
rad2 = Radiobutton(window, text = 5, value = 2, command = clicked_wt2)
rad3 = Radiobutton(window, text = 6, value = 3, command = clicked_wt3)
rad1.grid(column = 0, row = 5)
rad2.grid(column = 1, row = 5)
rad3.grid(column = 2, row = 5)

txt = "What are the dates that cover the weekly work timesheets?"
lbl = Label(window, text = txt, font = ("Arial", 12))
lbl.grid(column = 0, row = 9)
lbl = Label(window, text = "From: ", font = ("Arial", 12))
lbl.grid(column = 0, row = 10)
spin = Spinbox(window, from_=1, to=31, width=3)
spin.grid(column = 1, row = 10)
print(spin.get())
s.set_days_start(spin.get())
lbl = Label(window, text = "/", font = ("Arial", 12))
lbl.grid(column = 2, row = 10)
spin = Spinbox(window, from_=1, to=12, width=3)
spin.grid(column = 3, row = 10)
lbl = Label(window, text = "to: ", font = ("Arial", 12))
lbl.grid(column = 4, row = 10)
spin = Spinbox(window, from_=1, to=31, width=3)
spin.grid(column = 5, row = 10)
s.set_days_end(spin.get())
lbl = Label(window, text = "/", font = ("Arial", 12))
lbl.grid(column = 6, row = 10)
spin = Spinbox(window, from_=1, to=12, width=3)
spin.grid(column = 7, row = 10)

s.print_data()
window.mainloop()

