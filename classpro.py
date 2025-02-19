class school:
    def __init__(self,name,mark):
        self.__name = name
        self.mark = mark
    def display(self):
        print("your name is",self.__name)
        print("your marks is",self.mark)
obj = school("khushal",58)
obj.display()
# print(obj.name)
        