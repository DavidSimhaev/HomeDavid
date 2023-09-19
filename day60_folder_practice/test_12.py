class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    
# Enter code here.
g = AddingStack()
g.push(1)
g.push(2)
g.push(3)
print(g.pop())
print(g.pop())
print(g.pop())