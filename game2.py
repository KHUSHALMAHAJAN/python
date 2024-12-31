import random
import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')  
    else:
        os.system('clear')  

def option_func(option):
    match option:
        case 1:
            return "stone"
        case 2:
            return "paper"
        case 3:
            return "scissor"
        case _:
            print("plz enter valid value")
            return None

print("Play with Computer\nStone Paper Scissor")
name = input("Enter your name: ")
print("Hello, " + name + " Let's play the game")

if os.path.exists("gamehistory.txt"):
    os.remove("gamehistory.txt")
with open("gamehistory.txt", "a") as file:
    file.write("\nName :- " + name)

computeroption = "not use"
userscore = 0
computerscore = 0
useroption = 0
repeat = "yes"
i = 0
winner = 0

while repeat == "yes":
    i += 1
    print("\nEnter a choice: Stone, Paper, or Scissor")
    try:
        option = int(input("1: Stone\n2: Paper\n3: Scissor\nEnter a number: "))
        useroption = option_func(option)
        if not useroption:
            continue
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    print("You selected: " + useroption)
    print("Wait for computer's turn...")
    random_integer = random.randint(1, 3)
    computeroption = option_func(random_integer)
    print("Computer selected: " + computeroption)

    if computeroption == useroption:
        print("Match Draw")
        winner = 2
    elif (useroption == "stone" and computeroption == "scissor") or \
         (useroption == "paper" and computeroption == "stone") or \
         (useroption == "scissor" and computeroption == "paper"):
        print(name + " wins this round!")
        userscore += 1
        winner = 1
    else:
        print("Computer wins this round!")
        computerscore += 1
        winner = 0

    strus = str(userscore)
    print("\n" + name + " Score: " + strus)
    strcs = str(computerscore)
    print("Computer Score:  " + strcs)

    with open("gamehistory.txt", "a") as file:
        stri = str(i)
        file.write("\nRound: " + stri + "\n")
        file.write("You selected: " + useroption + "\n")
        file.write("Computer selected: " + computeroption + "\n")
        if winner == 1:
            file.write(name + " wins\n")
        elif winner == 0:
            file.write("Computer wins\n")
        else:
            file.write("Match Draw\n")
        file.write(name + " Score: " + strus + "\n")
        file.write("Computer Score: " + strcs + "\n")

    repeat = input("Do you want to play again? (yes/no): ")

if repeat == "no":
    clear_console()
    with open("gamehistory.txt", "r") as file:
        content = file.read()
    print("See your previous game history:\n")
    print(content)
