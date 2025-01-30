n = int(input("Enter day you take challenge :- "))
total_push_up = 0
total_squats = 0
total_jumping_jack = 0
for i in range(n):
    print("day",i+1)
    push_up = int(input("enter a number of push up :- "))
    squats = int(input("enter a number of squats :- "))
    jumping_jack = int(input("enter a number of jumping jack :- "))
    total_push_up += push_up
    total_squats += squats
    total_jumping_jack += jumping_jack
if(total_push_up == 50):
    print("congratulatory you completed push up")
elif(total_push_up < 50):
    remain = int((total_push_up/50)*100)
    print("your work is remain ",100 - remain,"% push up")
else:
    print("you got doubble congratulatory push up")

if(total_squats == 30):
    print("congratulatory you completed squats")
elif(total_squats < 30):
    remain = int((total_squats/30)*100)
    print("your work is remain ",100 - remain,"%","squats")
else:
    print("you got doubble congratulatory squats")

if(total_jumping_jack == 20):
    print("congratulatory you completed jumping jacks")
elif(total_jumping_jack < 20):
    remain = int((total_jumping_jack/20)*100)
    print("your work is remain ",100 - remain,"%","jumping jacks")
else:
    print("you got doubble congratulatory jumping jacks")
