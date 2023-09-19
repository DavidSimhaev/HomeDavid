import datetime
class Timer:
    def __init__(self,HOUR, MINUTE, SECOND ):
        self.HOUR = HOUR
        self.MINUTE = MINUTE
        self.SECOND = SECOND
        
    def __str__(self):
        if int(self.HOUR) < 10:
            self.HOUR = "0" + str(self.HOUR)
        if int(self.MINUTE) < 10:
            self.MINUTE = "0" + str(self.MINUTE)
        if int(self.SECOND) < 10:
            self.SECOND = "0" + str(self.SECOND)
        
        my_date = f"{self.HOUR}{self.MINUTE}{self.SECOND}"
        
        return my_date[:2] + ':' + my_date[2:4] + ':' + my_date[4:6]
    
    
    def next_second(self):
        self.HOUR = int(self.HOUR )
        self.MINUTE = int(self.MINUTE)
        self.SECOND = int(self.SECOND)
        
        self.SECOND +=1
        
        if self.SECOND == 60:
            self.SECOND = 0
            self.MINUTE +=1
            
        if self.MINUTE == 60:
            self.MINUTE = 0
            self.HOUR+=1
            
        if self.HOUR == 24:
            self.HOUR = 0
       
        pass
    def prev_second(self):
        
        self.HOUR = int(self.HOUR )
        self.MINUTE = int(self.MINUTE)
        self.SECOND = int(self.SECOND)
        
        self.SECOND -=1
        
        if self.SECOND == -1:
            self.SECOND = 59
            self.MINUTE -=1
            
        if self.MINUTE == -1:
            self.MINUTE = 59
            self.HOUR-=1
            
        if self.HOUR == -1:
            self.HOUR = 23
        
        
        #
        # Write code here
        #
"""%Y означает год
%m означает месяц
%d означает день
%H означает часы
%M означает минуты
%С означает секунды."""
#datetime.strftime(“%Y-%m-%d-%H:%M:%S”)

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)