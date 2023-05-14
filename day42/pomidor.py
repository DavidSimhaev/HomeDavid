import datetime
class Pomidor():
    states = ["Несозревшие ","Цветение ","Зеленый ","Спелый"] 
    def __init__(self ):
        self.quantity = 5
        self.getstate= self._genstate()
        self.state =  next(self.getstate)
    def _genstate(self):
        for state in self.states:
            yield state
        
        while(True):
            self.quantity =-1
            yield(self.states[-1])
    def grow(self):  
        self.state =  next(self.getstate)



class PomidorBush():
    def __init__(self, number):
        self.tomatoes = [ Pomidor().getstate for _ in range(number) ]
            
    def grow_all(self):
        
        for tomato in self.tomatoes:
            
            return next(tomato)
        
        
    def checkTrueOrFalse(self):
        if Pomidor().quantity <= 0:
            return "Все помидоры спелые!"  
        
c = PomidorBush(5).grow_all()
print(c)    
c =  PomidorBush(5).checkTrueOrFalse()
print(c)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    def check(self):
#        if self.fertilization < 10:
#            return f"Слишком мало добавленно удобрение, вы сорвали недозревшие сорты \nСтадия: {self.state}\nВсего: {self.bush} помидоров "
#        elif self.fertilization >= 10 and self.fertilization <= 20:
#            del self.states[0]
#            return f"Стадия: {self.state[0]}\nВсего: {self.bush} помидоров" 
#        elif self.fertilization >= 20 and self.fertilization < 30:
#            del self.states[0]
#            del self.states[0]
#            return f"Стадия: {self.state[0]}\nВсего: {self.bush} помидоров "
#        elif self.fertilization >= 30:
#            del self.states[0]
#            del self.states[0]
#            del self.states[0]            
#            return f"Стадия: {self.state[0]}! Можно сорвать\nВсего: {self.bush} помидоров"     
        