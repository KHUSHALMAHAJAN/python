n = int(input("Enter a number :- "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()