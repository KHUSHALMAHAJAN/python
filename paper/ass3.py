# num = 1
# i = 4
# j = 7
# k = 7
# l = 0
# while(i >= 1):
#     while(j >= 1):
#         print(num,end=" ")
#         j -= 1
#         if num == 1:
#             num = 0
#         else:
#             num = 1
#     print()
#     k -= 2
#     j = k
#     i -= 1
#     num = 1


# a = {1,2,3,4,5,6}
# print(a)

# a.add(7)
# print(a)

# a.remove(3)
# print(a)

# a.pop()
# print(a)

# dict1 = {'Goole' : 1, 'Facebook' : 2, 'Microsoft' : 3}
# dict2 = {'GFG' : 1, 'Microsoft' : 2, 'Youtube' : 3}
# dict1.update(dict2)
# for key, values in dict1.items( ):
#  print (key, values)

# num = int(input("Enter a number :- "))
# rem = 0
# temp = num
# ans = 0
# stri = ""
# intnum = 0
# while(num > 0):
#     rem = num % 10
#     strrem = str(rem)
#     num = int(num / 10)
#     stri += strrem
# intnum = int(stri)
# if(intnum == temp):
#     print("Its a palindrom")
# else:
#     print("Its not palindrom")

# import module

# module.program_method("c")
# upper = 0
# lower = 0

# def opeeration():
#     upper = 0
#     lower = 0
#     tempstr = input("enter a string :- ")
#     for i in tempstr:
#         if(i.isupper()):
#             upper += 1
#         else:
#             lower += 1
#     print(upper)
#     print(lower)
# opeeration()

# class student:
#     def __init__(self):
#         self.name = input("Enetr a name :- ")
#         self.roll = int(input("Enter a roll no :- "))
#     def display(self):
#         print("Name of student of ",self.name)
#         print("roll no of student",self.roll)
# obj = student()
# obj.display()

# course = "python"
# print(course[:3])
# print(course[3:])
# print(course[2:2])
# print(course[:])
# print(course[-1])
# print(course[1])

# class password(Exception):
#     pass

# try:
#     passw = input("enter a password :- ")
#     if(passw != "khushal"):
#         raise password
#     print("your are enter a correct password")
# except password:
#     print("your a worg passowrd")

# with open("demokhushal3.txt",'a') as f:
#     f.write('\n')
#     f.write(input("ENter a string :- "))
# with open("demokhushal3.txt",'r') as f:
#     print(f.read())

# a = [2,3,4,5,6,7]
# print(len(a))
# print(max(a))
# print(min(a))
# print(sum(a))

# dic = {1:'khushal',2:'manoj',3:'mahajan'}
# for i in dic:
#     print(i,":",dic[i])
# dic[1] = 'kunal'
# print(dic)
# del dic[1]
# print(dic)
# dic[4] = 'coding'
# print(dic)
# print(len(dic))

# fruit = 'banana'
# print(fruit[:3])
# print(fruit[3:])
# print(fruit[3:3])

# a = {1,2,3,4}
# # a.add(5)
# # print(a)
# # a.remove(3)
# # print(a)
# # for i in a:
# #     print(i)
# b= {2,5,7,9,1,3}
# #union
# c = a|b
# print(c)
# #intersection
# c = a&b
# print(c)
# #difference
# c = a-b
# print(c)
# #symmtric difference
# c = a^b
# print(c)

# with open("demokhushal3.txt",'r') as f:
#     print(f.readline())
#     print(f.readline())

# i = 1
# j = 1 
# k = 5
# n = 2

# while(i <= 3):
#     while(j <= i):
#         print(n,end=" ")
#         n += 2
#         j += 1
#     j = 1
#     i += 1
#     print()

# t = ("spam","Spam","SPAM!","SaPm")
# print(t[2])
# print(t[:-2])
# print(t[2:])
# print((t))

# def func(name = None):
#     if name is not None:
#         print("not None",name)
#     else:
#         print("none")
# func("khushal")

# class parent:
#     def __init__(self):
#         self.age = 45
#     def displaydemo(self):
#         print("parent",self.age)
# class child:
#     def __init__(self):
#         self.age = 20
#     def display(self):
#         print("child",self.age)
# parentobj = parent()
# childobj = child()
# print(childobj.age())
# parentobj.displaydemo()

# stri  = "khushal"
# re = stri[::-1]
# print(re)

class password(Exception):
    pass
try:
    text = input("Enter a password :- ")
    if('kuanl' != text):
        raise password
    print("password ",text)
except password:
    print("worng password")
finally:
    print("finalay")
