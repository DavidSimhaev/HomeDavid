class QueueError(IndexError):
    def __init__(self):
        super.__init__(self)
        self.check_q = False
    def show_Error(self):
        return IndexError
        
class Queue:
    def  __init__(self):
        self.queue = []
        
    
    def put(self,elem):
        self.queue.insert(0,elem)
    
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            if self.queue == []:
                self.check_q = False
            return elem
    
        else:
            return QueueError.show_Error(self)

class SuperQueue(Queue):
    def __init__(self) -> None:
        super().__init__()

    def put(self,elem):
        self.check_q = True
        self.queue.insert(0,elem)


    def isempty(self):
        return self.check_q

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if que.isempty():
        print(que.get())
    else:
        print("Queue empty")