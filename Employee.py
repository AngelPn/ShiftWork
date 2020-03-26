class Employee:
    def __init__(self, name, surname)
        self.name = name 
        self.surname = surname
        self.NightHours = 0
        self.SundayHours = 0
        self.NoSickness = 0
        self.NoLicense = 0

    def add_info(nighthours, sundayhours, nosickness, nolicense)
        self.NightHours += nighthours
        self.SundayHours += sundayhours
        self.NoSickness += nosickness
        self.NoLicense += nolicense

    def convert_info(cell, day)
        if day == "Sunday":
            if cell == "06:00 - 14:00" or cell == "14:00 - 22:00":
                self.SundayHours += 8
            elif cell == "22:00 - 06:00":
                self.NightHours += 8
                self.SundayHours += 2
            elif cell == "ΑΝΑΡ. ΑΔΕΙΑ":
                self.NoSickness += 1
            elif cell == "ΑΔΕΙΑ":
                self.NoLicense += 1
            else:
                pass
        elif day == "Saturday" and cell == "22:00 - 06:00":
            self.NightHours += 8
            self.SundayHours +=6
        else:
            if cell == "22:00 - 06:00":
                self.NightHours += 8
            elif cell == "ΑΝΑΡ. ΑΔΕΙΑ":
                self.NoSickness += 1
            elif cell == "ΑΔΕΙΑ":
                self.NoLicense += 1
            else:
                pass

    def print_employee()
        txt = "Name: {}\nSurname: {}\nNight Hours: {}\nSunday Hours: {}\nSickness Days: {}\nLicense Days: {}\n"
        print(txt.format(self.name, self.surname, self.NightHours, self.SundayHours, self.NoSickness, self.NoLicense))