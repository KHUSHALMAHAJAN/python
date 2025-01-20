# temp = ""
# temp += "2"
# temp += "3"
# tempi = int(temp)
# tempi += 4
# print(tempi)

n = int(input("enter a number "))
check = n
r = ""
temp = ""
while(n>0):
    r = str(n%10)
    print("r",r)
    n = int(n/10)
    print("n",n)
    temp += r
tempint = int(temp)
if(tempint == check):
    print("it is palindrome")
else:
    print("it is not palindrome")