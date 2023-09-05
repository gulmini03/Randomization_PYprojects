import random

#0='rock'
#1='paper'
#2='scissors'

print("Let's play the Rock, Paper and Scissor GAME")
User1 = input("Enter name of 1st player")
User2 = input("Enter name of 2nd player")

print(f"WELCOME {User1} and {User2} . Let's begin!!")

min = 0
max = 2

user1 = random.randint(min,max)
user2 = random.randint(min,max)

#print(user1)
#print(user2)

if(user1 > user2):
    print(f"{User1} wins 1 point")
elif(user1 < user2):
    print(f"{User2} wins 1 point")
else:
    print("IT'S A DRAW!")
print()