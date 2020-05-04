# Project
An application that reads the weekly timesheets of employees of a greek organisation that cover a month from excel files and creates a new excel file with two sheets: 
- The first sheet, called "ShiftWork", has concentrated the shift work of every employee within a month. Specifically, the night work hours, the (night) work hours on Sunday, the total work hours on Sunday, the numbers of days of illness and of days of licenses and the (night) work hours of holiday, if there is a holiday in the month. These shift works are interested because they receive payrolls increases. 
- The second sheet, called "Ημερομηνίες Αδειών", has concentrated the dates of licenses for every employee within the month.

# Idea and Implementation
The application was a request from accountant [Panagopoulos Konstantinos](https://taxinfo.gr). It is designed to work on the basis of a specific format of excel files that you can find in folder named "excel_files". This folder contains the generated excel file as well. Both weekly timesheets excel files and the generated excel file is written in greek language.

# Execution
By downloading the repo, you can simply double-click the ShiftWork.bat.
You can also run the program on Command Prompt:
```sh
$ python demo.py
```
A Graphical User Interface will open written in greek language. The month for which we want to get the shift works and if the month has holiday are requested. The GUI includes two questions.