# Project
An application that reads the weekly timesheets of employees of a greek organisation that cover a month from excel files and creates a new excel file with two sheets: 
- The first sheet, called "ShiftWork", concentrates the following monthly shift work of every employee:
    1) night work hours
    2) Sunday (night) work hours
    3) total Sunday work hours
    4) number of days of illness
    5) number of days off
    6) holiday (night) work hours, provided that there is a holiday in the month.
  These shift works are of interest because they result in a payroll increase. 
- The second sheet, called "Ημερομηνίες Αδειών", concentrates the dates of days off for every employee within the month.

# Idea and Implementation
The application was a request from the accountant [Panagopoulos Konstantinos](https://taxinfo.gr). It is designed to work on the basis of a specific format of excel files that you can find in a folder named "excel_files". This folder contains the generated excel file as well. Both weekly timesheet excel files and the generated excel file are written in greek.

# Execution
By downloading the repo, you can simply double-click the ShiftWork.bat.
You can also run the program on Command Prompt:
```sh
$ python demo.py
```
A Graphical User Interface will appear written in greek language. It includes two questions from which we will get the month and the holiday, if it has one. After that, the user can load the excel files. The generated excel file will be saved in the same location path as the chosen ones.

# Note
The program is using xlrd and xlwt python libraries for reading from and writing to excel files. So, it is necessary these libraries to be installed in your PC before running the program.

# Implementation Details
There are three work hours in the weekly timesheets:
1) 06:00-14:00
2) 14:00-22:00
3) 22:00-06:00

The night work hours (3) receive different payroll increase in weekends. On Saturdays, we count 2 hours of night work hours and 6 hours of Sunday night work hours. On Sundays, we count 2 hours of Sunday night work hours and 6 hours of night work hours.
As for the number of days of illness, the program tracks the cells that mention "ΑΝΑΡΡΩΤΙΚΗ ΑΔΕΙΑ". Respectively, the program tracks the cells that mention "ΑΔΕΙΑ" for the number of days off.

# ShiftWork as an app for accountants
ShiftWork could be an application that generates the monthly shift work of employees of any organisation or company. To accomplish that, the GUI should contain questions to obtain the information needed to make the program work, such as the work hours, the segments of employees, the dates that cover every weekly timesheet etc.
