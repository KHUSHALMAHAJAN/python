num = int(input("enter a num: "))
for i in range(2,num):
    if(num % i == 0):
        print("prime number")
        break;
else:
    print("it is not prime number")
