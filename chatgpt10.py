name = input("Enter a number :- ")
revers = name[::-1]
print(revers)
if(name == revers):
    print("this string is palindrome")
else:
    print("this string not palindrome")