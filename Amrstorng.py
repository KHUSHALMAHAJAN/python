num = int(input("enter a number: "))
sum = 0
temp = num
while(num>0):
    digit = int(num/10)
    # print(digit)
    temp2 = int(num%10)
    # print(temp2)
    sum = sum + (temp2 ** 3)
    # print(sum)
    num = digit
if(temp == sum):
    print("it is amrstorng number")
else:
    print("it is not amrstong number")
