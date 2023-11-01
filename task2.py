import os
from random import randint
def guess_number():
    answer = randint(1, 100)
    guess = int(input("Please enter your guess: "))
    while guess != answer:
        if guess < answer:
            os.system('cls')
            print("Too low!")
            guess = int(input("Please enter your guess: "))
        elif guess > answer:
            os.system('cls')
            print("Too high!")
            guess = int(input("Please enter your guess: "))
    print("Congratulation!")
guess_number()