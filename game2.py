import random
import time
import os

print("play with computer \nstone paper scissor")
name = input("Enter your name: ")
print("Hello, " + name + " Let's play game")

with open("gamehistroy.txt","a") as file:
    file.write("\nName :- " + name)

computeroption = "not use"
userscore = 0
computerscore = 0
useroption = 0
repeat = "yes"
playgame = "yes"
i = 0
winner = True

import os
import platform

def clear_console():
    # Check the operating system
    if platform.system() == "Windows":
        os.system('cls')  # Clear console for Windows
    else:
        os.system('clear')

while(repeat == "yes"):
            i += 1
            time.sleep(2)
            print("\n\nEnter a stone paper scissor")
            try:
                option = int(input("1: Stone\n2: Paper\n3: Scissor\nEnter a number: "))
                match option:
                    case 1:
                        useroption = "stone"
                    case 2:
                        useroption = "paper"
                    case 3:
                        useroption = "scissor"
                    case _:
                        print("plz enter valid value")
                        continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
            print("you are select "+ useroption)
    
            print("wait for computer turn....")
            random_integer = random.randint(1,3)
            match random_integer:
                case 1:
                    computeroption = "stone"
                case 2:
                    computeroption = "paper"
                case 3:
                    computeroption = "scissor"
                case _:
                    print("plz enter valid value")
            print("computer is select " + computeroption)

            if(computeroption == "stone"):
                match useroption:
                    case 'stone':
                        print("match drow")
                    case 'paper':
                        print(name + " win")
                        userscore += 1
                        winner = True
                    case 'scissor':
                        print("computer win")
                        computerscore += 1
                        winner = False

            elif(computeroption == "paper"):
                match useroption:
                    case 'stone':
                        print("computer win")
                        computerscore += 1
                        winner = False
                    case 'paper':
                        print("match drow")
                    case 'scissor':
                        print(name + " win")
                        userscore += 1
                        winner = True

            elif(computeroption == "scissor"):
                match useroption:
                    case 'stone':
                        print(name + " win")
                        userscore += 1
                        winner = True
                    case 'paper':
                        print("computer win")
                        computerscore += 1
                        winner = False
                    case 'scissor':
                        print("match drow")

            time.sleep(2.5)
            strus = str(userscore)
            print("\n\n" + name + " score is " + strus)
 
            strcs = str(computerscore)
            print("\ncomputer score is " + strcs)

            with open("gamehistroy.txt","a") as file:
                file.write("\n")
                stri = str(i)
                file.write("Round :- " + stri +"\n")
                file.write("your are select :- " + useroption + "\n")
                file.write("computer select :- " + computeroption + "\n")
                if(winner == True):
                    file.write(name + " win\n")
                else:
                    file.write("computer win\n")

                file.write("your score is :- " + strus + "\n") 
                file.write("computer score is :- " + strcs +'\n')

            repeat = input("you repeat is game \n yes/no: ")
            if(repeat == "yes"):
                clear_console()
                print("Best of lauck")
            else:
                clear_console()
                with open("gamehistroy.txt","r") as file:
                    content = file.read()
                    print("see your previous game  :- \n")
                    print(content)
                os.remove("gamehistroy.txt")