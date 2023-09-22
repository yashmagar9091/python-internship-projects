import random
computer_no=random.randint(1,3)
round=int(input("enter the no of rounds you want to play with computer : "))
round_no=round
for i in range(0,round_no):
    user=int(input("choose the input:  'rock:1'  ,'paper:2'  ,'sessior:3' \n"))
    if(computer_no==1):
        print("computer input is: rock")
    elif(computer_no==2):
        print("computer input is: paper")
    elif(computer_no==3):
        print("computer input is: sessior")
    if(user==1 and computer_no==3):
        print("rock beat serrior so winner is the user")
    elif(user==3 and computer_no==1):
        print("rock beat sessior so winner is computer")
    elif(user==3 and computer_no==2):
        print("sessior beats paper so winner is user")
    elif(user==2 and computer_no==3):
        print("sessior beats paper so winner is computer")
    elif(user==2 and computer_no==1):
        print("paper beats rock so winner is user")
    elif(user==1 and computer_no==2):
        print("paper beats rock so winner is computer")
    if(user==computer_no):
        print("this is tie")
    else:
        print("user input is invalid")





