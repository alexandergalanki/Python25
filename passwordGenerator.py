import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '[', ']', '{', '}', '|', ';',
           ':', "'", ',', '.', '<', '>', '?', '/', '~', '`']
password=""
NoOfLetters=int(input("how many letters do you want?\n"))
NoOfsymbols=int(input("how many symbols do you want?\n"))
NoOfNumbers=int(input("how many numbers do you want?\n"))

for l in range(1,NoOfLetters+1):
    password=password+random.choice(letters)
for l in range(1,NoOfsymbols+1):
    password=password+random.choice(symbols)
for l in range(1,NoOfNumbers+1):
    password=password+random.choice(digits)
PassArray=list(password)
print(''.join(random.sample(PassArray,len(PassArray))))