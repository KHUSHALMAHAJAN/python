n=int(input("enter a number of item :- "))
i = 1
prc = 0
while(i<=n):
    inprc= int(input(f"enter a item {i} price :- "))
    prc = prc + inprc
    i += 1
if(prc>= 1000 and prc<=5000):
    dis = (prc/100)*10
    total_price = prc - dis
    print(f"you got 10% discount your total a amount is {total_price}")
elif(prc> 5000):
    dis = (prc/100)*20
    total_price = prc - dis
    print(f"you got 20% discount your total a amount is {total_price}")
else:
    print(f"your total amount is {prc}")
