i  = 0
cpin = 1234
amount = 20000
while(i<3):
    pin = int(input("Enter your 4 digit pin number :- "))
    if(pin == cpin):
        withdrow = int(input("enter withdrowal :- "))
        if(withdrow <= amount and withdrow % 100 == 0):
            print("collect cash")
            print("your remain balnce ",amount - withdrow)
        break
    else:
        print("wrong pin")
    i += 1
    if(i >2):
        print("your account  has been block")
