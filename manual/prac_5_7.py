num = int(input("Enter a number: "))
sum_of_digits = 0

while num != 0:
    sum_of_digits += num % 10
    num //= 10

print(f"Sum of the digits: {sum_of_digits}")
