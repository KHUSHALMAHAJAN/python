currentbal = int(input("Enter a  your current balance :- "))
withdrawal = int(input("Enter a  your Withdrawal Amount :- "))
if(currentbal < withdrawal):
    print("Insufficient Balance")
else:
    if(withdrawal % 100 == 0):
        print("Collect your amount")
        print("Your remaing amount is ",currentbal - withdrawal)
    else:
        print("Invalid Amount. Please enter multiples of 100")