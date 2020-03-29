import xlrd
import Empl_mod

employees_shiftwork = {} #employees dictionary

import datetime

def read_xl(filename, range_start, range_end, month):
    xl_workbook = xlrd.open_workbook(filename) #get workbook
    xl_sheet = xl_workbook.sheet_by_index(0) #get sheet 0 from workbook

    txt = xl_sheet.cell_value(2, 0).lstrip("ΠΡΟΓΡΑΜΜΑ ΒΑΡΔΙΩΝ ΑΠO                              ").partition(" ΕΩΣ ")
    year_start = int(txt[0].rpartition("\\")[2])
    month_start = int(txt[0].rpartition("\\")[0].partition("\\")[2])
    day_start = int(txt[0].rpartition("\\")[0].partition("\\")[0])
    date_start = datetime.datetime(year_start, month_start, day_start)
    
    year_end = int(txt[2].rpartition("\\")[2])
    month_end = int(txt[2].rpartition("\\")[0].partition("\\")[2])
    day_end = int(txt[2].rpartition("\\")[0].partition("\\")[0])
    date_end = datetime.datetime(year_end, month_end, day_end)
    print(date_start)
    print(date_end)
    if date_start.strftime("%m") != month:
        day = datetime.datetime(year_end, int(month), 1).strftime("%A")
        col_start = Empl_mod.weekdays[day]
        col_end = Empl_mod.weekdays["Sunday"]
    elif date_end.strftime("%m") != month:
        col_start = Empl_mod.weekdays["Monday"]
        col_end = Empl_mod.weekdays[datetime.datetime(year_start, int(month) + 1, 1).strftime("%A")] - 1
    else:
        col_start = Empl_mod.weekdays["Monday"]
        col_end = Empl_mod.weekdays["Sunday"]

    for row_idx in range(range_start, range_end):
        key = xl_sheet.cell_value(row_idx, 0) + xl_sheet.cell_value(row_idx, 1)
        if key not in employees_shiftwork:
            employees_shiftwork[key] = Empl_mod.Employee(xl_sheet.cell_value(row_idx, 0), xl_sheet.cell_value(row_idx, 1))
        for col_idx in range(col_start, col_end):
            cell_value = xl_sheet.cell_value(row_idx, col_idx)  # Get cell object by row, col
            employees_shiftwork[key].add_info(cell_value, col_idx)

read_xl("program1.xls", 7, 14, "02")
read_xl("program1.xls", 17, 25, "02")

read_xl("program2.xls", 7, 14, "02")
read_xl("program2.xls", 17, 25, "02")

read_xl("program3.xls", 7, 14, "02")
read_xl("program3.xls", 17, 25, "02")

read_xl("program4.xls", 7, 14, "02")
read_xl("program4.xls", 17, 25, "02")

read_xl("program5.xls", 7, 14, "02")
read_xl("program5.xls", 17, 25, "02")

for x in employees_shiftwork:
    print(employees_shiftwork[x].print_employee())