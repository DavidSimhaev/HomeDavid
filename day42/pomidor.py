import datetime


class Pomidor():
    states = ["Несозревшие","Цветение","Зеленый","Спелый"] 
    def __init__(self, index):
        self.index = index
        self.state =  self.states[0]
    
    def grow(self):
        if self.state > 0 and self.state < 10:
            return self.states[0]
        elif self.state > 10 and self.state < 20:
            return self.states[1]
        elif self.state > 20 and self.state < 30:
            return self.states[3]
        elif self.state > 30 and self.state < 40:
           return self.states[4]
    


p = Pomidor(1).state
print(p)