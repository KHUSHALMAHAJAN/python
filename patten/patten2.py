# n = int(input("enter a number"))
row = 8
for i in range(1,5):
    for k in range(1,i):
        print(" ",end=" ")

    for j in range(1,row):
        print(j%2,end=" ")
    row -=2
    
    print()