string = input("Enter a string :- ")
uppercase = 0
lowercase = 0
for i in string:
    if(i.isupper()):
        uppercase += 1
    else:
        lowercase += 1
print("uppercase =",uppercase)
print("lowercase =",lowercase)