class area:
    def area1(self,base,height):
        area = .5 * base *height
        print("triangle ",area)
    def area1(self,side):
        area = side*side
        print("square",area)
    def area1(self,leght,breath):
        area = leght*breath
        print("retangle",area)
obj = area()
obj.area1(4)