dis = {}
n = int(input("Enter a total number of student are participate :- "))
for i in range(n):
    print("student :- ",i+1)
    name = str(input("Enter a name of student :- "))
    event = str(input("Enter a event name coding/sport/dance :- "))
    dis.update({name : event})
print("name total student")
for i in dis:
    print(i,":",dis[i])

