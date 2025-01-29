n = int(input("enter a number of vehicle is parking :- "))
for i in range(n):
    hour = int(input(f"Enter a hour you vehical is parking {i+1} :- "))
    if(hour >= 2 and hour <= 5):
        extra_hour = hour - 1
        price = extra_hour * 10
        print("your total fee is",price + 20)
    elif(hour >= 6):
        extra_hour = hour - 5
        price = extra_hour * 5
        print("your total fee is",price + 60)
    else:
        print("your total fee is 20")