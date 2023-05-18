from tomato import Tomato
class TomatoBush():
    
    def __init__(self, numberOfTomatoes):
        self.tomatoes = [ Tomato() for _ in range(numberOfTomatoes) ]
        
    def growall(self):
        for tomato in self.tomatoes:
            tomato.grow()
    
    def all_are_ripe(self):
        return all(map(lambda x: x.state == x.laststate, self.tomatoes))
    
    def no_are_ripe(self):
        return all(map(lambda x: x.state != x.laststate, self.tomatoes))
            
    def give_away_all(self):
        self.tomatoes.clear()
        
    def number_of_tomatoes(self):
        return len(self.tomatoes)


d = TomatoBush(3)
for _ in range(5): # 5 попыток апргейда из 12 кустиков! 
    d.growall() 
    
print(d.all_are_ripe()) # Если один из них становится спелым, то возращает True , в противном случаи False


