import random
name=str(input("Enter your name: "))
choice=str((input("Enter your choice (snake, water, gun): ")))
newchoice=choice.lower()
if newchoice=="snake":
    i=1
elif newchoice=="water":
    i=2
elif newchoice=="gun":
    i=3    
print("Welcome", name, "to snake, water, gun game")
num = int(random.randint(1, 3))
if num==1:
    num_choice="snake"
elif num==2:
    num_choice="water"
elif num==3:
    num_choice="gun"
    print("your choice", newchoice)
print("computer choice", num_choice)
if(i==num):
    print("Tie")
elif(i==1 and num==2):
    print("You Win")
elif(i==1 and num==3):
    print("Computer Win")
elif(i==2 and num==1):
    print("Computer Win")
elif(i==2 and num ==3):
    print("You Win")
elif(i==3 and num==1):
    print("You Win")
elif(i==3 and num==2):
    print("Computer Win")