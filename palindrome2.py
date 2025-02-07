n = int(input("Enter a number :- "))
check = n
rem = ""
strem = ""
while(n > 0):
    rem = str(int(n % 10))
    n = int(n/10)
    strem += rem
inrem = int(strem)
if(inrem == check):
    print("this is palindrome")
else:
    print("this not palindrome")