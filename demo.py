from tkinter import *

window = Tk()
window.geometry('700x600')
window.title("Welcome to ShiftWork app")

txt = "An application that calculates the monthly shift works of employees"
lbl = Label(window, text = txt, font = ("Arial", 16))
lbl.grid(column = 0, row = 0)



window.mainloop()