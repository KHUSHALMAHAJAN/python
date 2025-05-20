n = int(input("Enter your total bill :- "))
discount = 0 
if(n > 5000):
    discount  = ((n/100)*20)
elif(n > 3000 and n < 5000):
    discount = ((n/100)*10)
else:
    discount = n
print("you pay a total = ",discount)
