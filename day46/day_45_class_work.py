

from pprint import pprint
import os

from anyio import sleep

class Board:
    
    vectors = [(0,1),(-1,0),(0,-1),(1,0)] # Первый гориз, второй вертикаль
    def __init__(self, n):
        self.__board = []
        self.__n = n
        self.__vector= 0
        for i in range(n):
            self.__board.append([0 for _ in range(n)])
            
    @property
    def n(self):
        return self.__n


    
##################################################################################################
    def startpoint(self, x, y):
        self.__point = x,y
        self.board = x,y
        
    @property
    def point(self):
        return self.__point
    
    def pointsum(self,point_X, point_Y):
        return (point_X[0]+point_Y[0], point_X[1]+point_Y[1])

    
    def bvalue(self, x , y):
        y = self.n -y 
        x = x - 1
        return self.__board[y][x] == 0
###################################################################################################
    def validate(self, x, y):
        if x<=self.n and y <= self.n and x>=0 and y >=0: # Вход в рамки
            
            if self.bvalue(x,y): # Проверка если последующий элемент равен нулю
                
                self.board = x,y # Смена кординат под новые 
                
                self.__point = (x,y) # Сохранение позиции
                
                
                pvector = (-1*self.vectors[self.__vector][1], # вектор y
                           self.vectors[self.__vector][0])# # Вектор x
                ppoint = self.pointsum((x,y), pvector)
                
                if not self.bvalue(ppoint[0],ppoint[1]):
                    return True
                if self.__vector ==3:
                    self.__vector = 0
                else:
                    self.__vector = self.__vector + 1    
                return True
        return False
        
        
    def move(self):
        for i in range(4):
            if self.__vector + i > 3:
                k = self.__vector + i -4
            else:
                k = self.__vector + i
            x, y = self.pointsum(self.vectors[k], self.__point)
            if self.validate(x,y):
                return True
        return False
    
    
                
    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, tuplexy:tuple ):
        y= self.n - tuplexy[1]
        x= tuplexy[0]-1
        self.__board[y][x] = 1
    ###################################################################################################    
b = Board(11)
b.board = 6,6
pprint(b.board)
b.startpoint(3,3)


while b.move():
    pprint(b.board)
    sleep(0.5)
    os.system("clear")
    
