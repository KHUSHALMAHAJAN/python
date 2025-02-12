def check_att(totalclass,attendclass):
    per = (attendclass/totalclass)*100
    if(per<75):
        print("your not allow exam")
    else:
        print("your allow exam")


tc = int(input("Enter a your total class :- "))
ac = int(input("Enter a ypur attend class :- "))
check_att(tc,ac)