a,b = 0,1
def fibonacci(n):
    global a,b
    for i in range(0,n):
        print(a)
        a,b = b,a+b
