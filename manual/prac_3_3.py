import math
num = float(input("Enter a number: "))
if num < 0:
    print("Square root of a negative number is imaginary.")
else:
    print(f"Square root of {num} is {math.sqrt(num):.2f}")