n = int(input("Enter a year :- "))
if(n%4 == 0):
    if(n%100 == 0):
        print("century year")
    print("leap year")
else:
    print("is not leap year")
        