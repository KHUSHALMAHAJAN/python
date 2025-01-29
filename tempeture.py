con = "yes"
mylist = []
n = 1
j = 1
while(con == "yes"):
    n = float(input("enter a tempeture "+ str(j) +" = "))
    mylist.append(n)
    j += 1
    con = input("you want to repat yes/no : ")
avg = float(sum(mylist)/len(mylist))
for k in mylist:
    if(k>avg):
        print(k)