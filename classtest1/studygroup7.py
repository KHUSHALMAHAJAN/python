list = []
j = 5
n = int(input("enter total number of student :- "))
for i in range(n):
    name = str(input(f"enter a name of student {i+1} :- "))
    list.append(name)
if(len(list) == 4):
    print("your group are perfect")
elif(len(list) > 4):
    print("your group extra student")
    for i in range(j,len(list)+1):
        print(j,":-",list[j-1])
        j += 1
else:
    print("your group is uncomplet")
