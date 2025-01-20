n = int(input("enter a number "))
temp = 0
while(n>0):
    r = int(n%10)
    n = int(n/10)
    temp += r
print(temp)