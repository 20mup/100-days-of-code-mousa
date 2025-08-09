import random

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [
    '!','"','#','$','%','&',"'",'(',')','*','+',
    ',','-','.','/',':',';','<','=','>','?','@',
    '[','\\',']','^','_','`','{','|','}','~'
]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

# Make password as a list first
password = []

for char in range(nr_letters):
    password.append(random.choice(letters))

for char in range(nr_symbols):
    password.append(random.choice(symbols))

for char in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the list so order is random
random.shuffle(password)

# Join into a string
final_password = "".join(password)
print(f"Your password is: {final_password}")
