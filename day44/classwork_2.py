class Time:
    def __init__(self, hour =0, minute = 0, second = 0):
        self._hour = hour # 0-23
        self._minute = minute # 0-59
        self._second = second # 0-59
        
         
         
    @property
    def hour(self):
        return self._hour
    
    @hour.setter
    def hour(self, hour):
        if not 0<=hour<24:
            raise ValueError(f"Час {hour} должен быть в диапозоне 0-23")
        
    @property
    def minute(self):
        return self._minute
    
    @minute.setter
    def minute(self, minute):
        if not 0<=minute<59:
            raise ValueError(f"Минуты {minute} должны быть в диапозоне 0-59")
        
    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self, second):
        if not 0<=second<59:
            raise ValueError (f"Секунды {second} должны быть в диапозоне 0-59")
        
    def set_time(self, hour =0, minute = 0, second = 0):
        self._hour = hour # 0-23
        self._minute = minute # 0-59
        self._second = second # 0-59
    
    def __repr__(self):
        return f"Time(hour= {self.hour}, minute= {self.minute} second= {self.second}))"
    
    def __str__(self):
        return (("12" if self.hour in (0,12) else str(self.hour%12))+
                (f":{self.minute:0>2}:{self.second:0>2}")+
                (" AM" if self.hour <= 12 and self.minute == 0 else " PM"))
d = Time(12,43,54)

print(d)


    
d.hour