cheackuppercase = 0
cheacklowercase = 0
cheackdigit = 0
password = input("Enter a password :- ")
for i in password:
    if(i.isupper()):
        cheackuppercase = 1
    if(i.islower()):
        cheacklowercase = 1
    if(i.isdigit()):
        cheackdigit = 1
if((len(password)>7) and cheackdigit == 1 and cheacklowercase == 1 and cheackuppercase == 1):
    print("storng Password")
else:
    print("weak password")
