import random
min = 1
max = 6

print ("do you want to roll the dice?")
dice_roll = input("yes/no")

if dice_roll == 'yes' :
    print (random.randint(min,max))
    
if dice_roll == 'no' :
    print ("GAME OVER")


