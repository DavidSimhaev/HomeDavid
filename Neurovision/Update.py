from Frame_Recording import Recording
class Child(Recording):
    def __init__(self, frame, frame2, frame_main):
        super(Child, self).__init__(frame, frame2, frame_main)
                            
                    
class Parent(object):
    def __init__(self, a, b):
        self.a= a
        self.b= b
        print ('a', a)
        print ('b', b)

    def change(self):
        self.a = 20
        self.b = 20
        print(self.b + self.a)



text = Parent(1,2)
text2 = Parent(1,2).change()