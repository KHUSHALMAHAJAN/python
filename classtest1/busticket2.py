n=int(input("enter a number of passengers :- "))
i = 1
prc = 0
while(i<=n):
    age = int(input("enter your age :- "))
    dis = int(input("enter your distance :- "))
    if(age <= 12):
        inprc = dis * 2
        prc = inprc + prc
    elif(age > 12 and age <= 60):
        inprc = dis * 5
        prc = inprc + prc
    else:
        inprc = dis * 3
        prc = inprc + prc
    i += 1
print("total ticket price is",prc,"string")
    