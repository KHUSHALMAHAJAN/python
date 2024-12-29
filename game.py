import random
import time

print("play with computer \nstone paper scissor")
name = input("Enter your name: ")
print("Hello, " + name + " Let's play game")
computeroption = 0
userscore = 0
computerscore = 0
repeat = "yes"
while(repeat == "yes"):
 time.sleep(2)
 print("\n\nkhushaEnter a stone paper scissor")
 option = input("plz enter in small world: ")
 time.sleep(3)
 random_integer = random.randint(1,3)
 if(random_integer == 1):
    computeroption = "stone"
 elif(random_integer == 2):
    computeroption = "paper"
 elif(random_integer == 3):
    computeroption = "scissor"
 print("computer is select " + computeroption)
 if(computeroption == "stone"):
    if(option == "stone"):
        print("match drow")
    elif(option == "paper"):
        print(name + " win")
        userscore += 1
    elif(option == "scissor"):
        print("computer win")
        computerscore += 1
 elif(computeroption == "paper"):
    if(option == "stone"):
        print("computer win")
        computerscore += 1
    elif(option == "paper"):
        print("match drow")
    elif(option == "scissor"):
        print(name + " win")
        userscore =+ 1
 elif(computeroption == "scissor"):
    if(option == "stone"):
        print(name + " win")
        userscore += 1
    elif(option == "paper"):
        print("computer win")
        computerscore +=1
    elif(option == "scissor"):
        print("match drow")
 else:
    print("Enter a valid option")
 time.sleep(2.5)
 strus = str(userscore)
 print("\n\n" + name + " score is " + strus)
# print(userscore)
 strcs = str(computerscore)
 print("\ncomputer score is " + strcs)
 repeat = input("you repeat is game \n yes/no: ")
