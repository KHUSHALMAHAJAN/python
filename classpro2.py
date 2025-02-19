class first:
    def __init__(self,a,b):
        self.__a = a
        self.b = b
    def display(self):
        print("print value a of",self.__a)
        print("print value a of",self.b)
class second(first):
    def __init__(self, a, b,c,d):
        super().__init__(a, b)
        self.c = c
        self.d = d
    def display2(self):
        # print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)

obj2 = second(1,2,3,4)
obj1 = first(11,22)
obj1.display() 
obj2.display2()
obj1.display()