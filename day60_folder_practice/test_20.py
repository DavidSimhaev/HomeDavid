class Sample:
    def __init__(self):
        self.name = Sample.__name__
        print
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)


obj = Sample()
obj.myself()