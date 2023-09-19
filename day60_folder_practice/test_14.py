class QueueError(BaseException):  # Choose base class for the new exception.
    def __init__(self) -> None:
        BaseException.__init__(self)
    
    #
    #  Write code here
    #


class Queue:
    def __init__(self):
        self.queue = []
        # Write code here
        #

    def put(self, elem):
        self.queue.append(elem)
        #
        # Write code here
        #

    def get(self):
        
        person = self.queue[0]
        del self.queue[0]
        return person
        
        #
        # Write code here
        #


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for _ in range(4):
        print(que.get())
except:
    print("Queue error")