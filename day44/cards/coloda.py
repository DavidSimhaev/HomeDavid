from card import Card
import random

class Coloda:
    
    NUMBRES_OF_CARDS = 52
    
    def __init__(self):
        self._current_card = 0
        self._coloda = []
        
        for count in range(Coloda.NUMBRES_OF_CARDS):
            self._coloda.append(Card(Card.FACES[count%13], Card.SUITS[count//13]))


    def shuffle(self):
        self._current_card = 0
        random.shuffle(self._coloda)
        
        
    def deal_card(self):
        for next_card in self._coloda:
            yield next_card
        
    
        
        
        
        
    def __str__(self):
        s = ""
        for index, _ in enumerate(self._coloda):
            s+= f"{self._coloda[index]:<14}"
            
            if (index+1)%4 == 0:
                s+="\n"
        return s
    
    