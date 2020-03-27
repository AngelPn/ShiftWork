import xlrd
import Empl_mod
import enum
class weekdays(enum.Enum):
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    Saturday = 7
    Sunday = 8

employees_shiftwork = {} #employees dictionary

def read_xl(filename, range_start, range_end):
    xl_workbook = xlrd.open_workbook(filename) #get workbook
    xl_sheet = xl_workbook.sheet_by_index(0) #get sheet 0 from workbook
    for row_idx in range(range_start, range_end):
        key = xl_sheet.cell_value(row_idx, 0) + xl_sheet.cell_value(row_idx, 1)
        if key not in employees_shiftwork:
            employees_shiftwork[key] = Empl_mod.Employee(xl_sheet.cell_value(row_idx, 0), xl_sheet.cell_value(row_idx, 1))
        for col_idx in range(2, xl_sheet.row_len(row_idx)):
            cell_value = xl_sheet.cell_value(row_idx, col_idx)  # Get cell object by row, col
            employees_shiftwork[key].add_info(cell_value, weekdays(col_idx).name)

read_xl("program1.xls", 7, 14)
read_xl("program1.xls", 17, 25)

read_xl("program2.xls", 7, 14)
read_xl("program2.xls", 17, 25)

read_xl("program3.xls", 7, 14)
read_xl("program3.xls", 17, 25)

read_xl("program4.xls", 7, 14)
read_xl("program4.xls", 17, 25)

read_xl("program5.xls", 7, 14)
read_xl("program5.xls", 17, 25)

for x in employees_shiftwork:
    print(employees_shiftwork[x].print_employee())