
from time import sleep
from tomatobush import TomatoBush, Tomato
import random
class Gardener():
    
    def __init__(self, name, number_of_bushes):
        self.name = name
        self.__plants = [ TomatoBush(Tomato._random.randint(1,35)) for _ in range(number_of_bushes)]
        self.all_tomato = []
        self.no_ripe = []
    def work(self):
        for plant in self.__plants:
            plant.growall()
    
    def if_not_bushes_harvested(self):
        return any(map(lambda x: x.number_of_tomatoes() ,self.__plants))
    
    
    def if_not_bushes_ripe(self):
        return any(map)
                
    def harvest(self):    
        if len(self.__plants) == 0:
            return "All is done"
        noready = list(filter(lambda p: p.no_are_ripe(), self.__plants))        
        ready = list(filter(lambda p: p.all_are_ripe(), self.__plants))
        
        if len(ready) == 0:
            return 'Nothing is ready!'
        
        
        for bush in noready:
            self.no_ripe.append(bush)
            
        for bush in ready:
            if bush.number_of_tomatoes() != 0:
                self.all_tomato.append(bush.number_of_tomatoes())
                print(f"С куста собранно: {bush.number_of_tomatoes()}. {self.name} собрал/a помидоры!")
            
                
            bush.give_away_all()
        
        if not self.if_not_bushes_harvested():
                print(f"Все помидоры собранны. Всего зрелых {sum(self.all_tomato)} и незрелых {len(self.no_ripe)}")
            

g= Gardener("VLADIMIR", 10 ) 

while g.if_not_bushes_harvested():
    g.work()
    g.harvest()
    sleep(0.5)
