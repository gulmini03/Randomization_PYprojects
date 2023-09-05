import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numletters= int(input("number of letters"))
numnumbers= int(input("number of numbers"))
numsymbols= int(input("number of symbols"))

password = ""

for i in range(numletters):
  password += random.choice(letters)

for i in range(numnumbers):
  password += random.choice(numbers)

for i in range(numsymbols):
  password += random.choice(symbols)
  
print(password)

passwordf = list(password)
random.shuffle(passwordf)

final= ''.join(passwordf)

print(final)


