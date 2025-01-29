n = int(input("enter a number"))
i = 2
k = 0
while(i<n):
    if(n % i == 0):
        k =+ 1   
    i =+ 1   

if(k == 0):
    print("prime number")
else:
    print("not")
