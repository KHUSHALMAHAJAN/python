# class parent:
#     a = 6
#     b = 4
# obj = parent
# print(obj.a)
# print(obj.b)

# class parent:
#     # def __init__(self):
#         # self.a = a
#         # self.b = b
#     def add(self,a,b):
#         print(self.a + self.b)
# obj = parent()
# obj.add(5,7)


# class student:
#     def __init__(self,name,rollno,address):
#         self.name = name 
#         self.rollno = rollno
#         self.address = address
#     def showstudentdetail(self):
#         print("name of student ",self.name)
#         print("rollno of student ",self.rollno)
#         print("adress os student ",self.address)

# name = ""
# rollno = 0
# address = ""

# def getinformationstudent():
#     name = input("Enter a name :- ")
#     rollno = int(input("enter a roll no :- "))
#     address = input("Enter a address :- ")
#     obj = student(name,rollno,address)
#     obj.showstudentdetail()

# getinformationstudent()

# obj = student(name,rollno,address)
# obj.showstudentdetail()

# class demo:
#     def __init__(self):
#         self.__a = int(input("Enter a number :- "))
#     def display(self):
#         print("number is ",self.__a)
# obj = demo() 
# obj.display()
# print(obj.a)

class diploma:
    def getdiploma():
        print("I got diploma")
class CO(diploma):
    def getdiploma():
        print("I am with CO diploma")
class IF(diploma):
    def getdiploma():
        print("I am with IF diploma")

objco = CO
objif = IF
objco.getdiploma()
objif.getdiploma()