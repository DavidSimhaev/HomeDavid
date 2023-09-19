class WeekDayError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
	

class Weeker:
    #
    # Write code here.
    #

    list_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    def __init__(self, day):
        self.day = day
        if day not in self.list_days:
            raise WeekDayError
        
    def __str__(self):
        return self.day
    
    def add_days(self, n):
        index_day = self.list_days.index(self.day)
        res = index_day + n
        while True:
            try:
                self.day = self.list_days[res]
                break
            except:
                res = res - 7 
            
    def subtract_days(self, n):
        index_day = self.list_days.index(self.day)
        res = index_day - n
        while True:
            try:
                self.day = self.list_days[res]
                break
            except:
                res = res + 7 
            
        #
        # Write code here.
        #
        pass

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
