weekdays = {
    "Monday" : 2,
    "Tuesday" : 3,
    "Wednesday" : 4,
    "Thursday" : 5,
    "Friday" : 6,
    "Saturday" : 7,
    "Sunday" : 8
}

class Employee:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
        self.NightHours = 0
        self.SundayHours = 0
        self.SundayNightHours = 0
        self.TotalSunday = 0
        self.NoSickness = 0
        self.NoLicense = 0
        self.HolidayHours = 0
        self.HolidayNightHours = 0
        self.LicenseDates = []

    def add_info(self, cell, day, holiday, date):
        if holiday:
            if cell == "06:00 - 14:00" or cell == "14:00 - 22:00": self.HolidayHours += 8
            elif cell == "22:00 - 06:00" and day == weekdays["Saturday"]:
                self.SundayNightHours += 6
                self.HolidayNightHours += 2
                self.TotalSunday += 1
            elif cell == "22:00 - 06:00":
                self.NightHours += 8
                self.HolidayNightHours += 2
            elif cell == "ΑΝΑΡ. ΑΔΕΙΑ" or cell == "ΑΣΘΕΝΕΙΑ" or cell == "ΑΔΕΙΑΣ ΚΥΗΣΗΣ" : self.NoSickness += 1
            elif cell == "ΑΔΕΙΑ":
                self.NoLicense += 1
                self.LicenseDates.append(date)
            else: pass
        else:
            if day == weekdays["Sunday"]:
                if cell == "06:00 - 14:00" or cell == "14:00 - 22:00":
                    self.SundayHours += 8
                    self.TotalSunday += 1
                elif cell == "22:00 - 06:00":
                    self.NightHours += 8
                    self.SundayNightHours += 2
                    self.TotalSunday += 1
                elif cell == "ΑΝΑΡ. ΑΔΕΙΑ" or cell == "ΑΣΘΕΝΕΙΑ" or cell == "ΑΔΕΙΑΣ ΚΥΗΣΗΣ" : self.NoSickness += 1
                elif cell == "ΑΔΕΙΑ":
                    self.NoLicense += 1
                    self.LicenseDates.append(date)
                else: pass
            elif day == weekdays["Saturday"] and cell == "22:00 - 06:00":
                self.NightHours += 8
                self.SundayNightHours +=6
                self.TotalSunday += 1
            else:
                if cell == "22:00 - 06:00": self.NightHours += 8
                elif cell == "ΑΝΑΡ. ΑΔΕΙΑ" or cell == "ΑΣΘΕΝΕΙΑ" or cell == "ΑΔΕΙΑΣ ΚΥΗΣΗΣ": self.NoSickness += 1
                elif cell == "ΑΔΕΙΑ":
                    self.NoLicense += 1
                    self.LicenseDates.append(date)
                else: pass