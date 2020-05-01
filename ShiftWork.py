import xlrd
import Empl_mod

employees_shiftwork = {} #employees dictionary

import datetime

def create_holidays(year, month, holiday):
    return datetime.datetime(year, month, holiday)

def read_xl(filename, month, holiday):
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

    if date_start.strftime("%m") != month:
        col_start = Empl_mod.weekdays[datetime.datetime(year_end, int(month), 1).strftime("%A")]
        col_end = Empl_mod.weekdays["Sunday"]
        if bool(holiday): date_holiday = create_holidays(year_end, int(month), int(holiday))
    elif date_end.strftime("%m") != month:
        col_start = Empl_mod.weekdays["Monday"]
        col_end = Empl_mod.weekdays[datetime.datetime(year_start, int(month) + 1, 1).strftime("%A")] - 1
        if bool(holiday): date_holiday = create_holidays(year_start, int(month), int(holiday))
    else:
        col_start = Empl_mod.weekdays["Monday"]
        col_end = Empl_mod.weekdays["Sunday"]
        if bool(holiday): date_holiday = create_holidays(year_end, int(month), int(holiday))
    
    col_holiday = -1
    if bool(holiday) and date_holiday<=date_end and date_holiday>=date_start: col_holiday = Empl_mod.weekdays[date_holiday.strftime("%A")]
    print(col_holiday)

    for row_idx in range(7, xl_sheet.nrows):
        key = xl_sheet.cell_value(row_idx, 0) + xl_sheet.cell_value(row_idx, 1)
        if not key: break
        if not xl_sheet.cell_value(row_idx, 1):
            row_idx += 1
            continue
        if key not in employees_shiftwork:
            employees_shiftwork[key] = Empl_mod.Employee(xl_sheet.cell_value(row_idx, 0), xl_sheet.cell_value(row_idx, 1))
        for col_idx in range(col_start, col_end+1):
            cell_value = xl_sheet.cell_value(row_idx, col_idx)  # Get cell object by row, col
            employees_shiftwork[key].add_info(cell_value, col_idx, col_idx == col_holiday)
        row_idx += 1