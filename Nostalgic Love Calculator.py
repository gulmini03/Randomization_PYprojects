name1 = input("enter name1")
name2 = input("enter name2")

lower_1 = name1.lower()
lower_2 = name2.lower()

#print (lower_1)
#print (lower_2)
cn = lower_1 + lower_2 #cn=checkname

print (cn)

t = cn.count('t')
r = cn.count('r')
u = cn.count('u')
e = cn.count('e')

true= t+r+u+e

l = cn.count('l')
o = cn.count('o')
v = cn.count('v')
e = cn.count('e')

love=l+o+v+e

scores = str(true) + str(love)

print (scores)
score = int(scores)

if score<10:
    print (f"Your score is  {scores} You go together like coke and mentos.")
elif score>90:
    print (f"Your score is  {scores} You go together like coke and mentos.")
elif (30<score<50):
    print (f"Your score is  {scores} You are alright together.")
else:
    print (f"Your score is {scores}.")
