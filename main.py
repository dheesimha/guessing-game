# Perfect guess game 

import random

a = random.randint(1,100)
print("The computer has chosen it's number")

b = int(input("Start guessing the number "))

while b!=a:
    if b>a:
        print("Lower")
        b=int(input("Enter a number "))
    elif b<a :
        print("higher")
        b=int(input("Enter a number "))
print("You guessed it right , the number was ",a)

