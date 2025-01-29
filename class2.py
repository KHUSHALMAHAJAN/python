n = int(input("Enter how many customer"))
ch = 0
ad = 0
se = 0
tick = 0
mylist = []
for i in range (1,n+1):
    temp = int(input("Enter a your no " + str(i) + " = "))
    mylist.append(temp)
for i in mylist:
    if(i<12 and i>0):
        ch += 1
        tick += 100
    elif(i>12 and i<60):
        ad += 1
        tick += 150
    else:
        se += 1
        tick += 250
if(len(mylist)>5):
    tick = tick * 0.9
    print(tick)
else:
    print(tick)

