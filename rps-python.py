from cgi import test
from doctest import OutputChecker
from optparse import check_choice
import random


def game():
    print("Would you like to play a game? (y/n)")
    choice = input()

    if choice.lower() == "y":
        print("Great, you're now playing rock (r), paper(p), scissors(s). Click enter to proceed.")
        answer = input()
        start=True

    else:
        print("Alright, maybe another time...")    
       
    if start==True:
        print("What will your choice be? rock (r) paper(p) scissors(s)")
        answer = input()  


    
    n = ['Rock', 'Paper', 'Scissors']

    if answer.lower() == "r":
        choice = random.choice(n)
        print('Rock vs ' + choice)

        if choice=="Rock":
            print("It's a draw!") 

        if choice=="Scissors":
            print("You won!") 

        if choice=="Paper": 
            print("You lost!")
        

    if answer.lower() == "p":
        choice = random.choice(n)
        print('Paper vs ' + choice)

        if choice=="Rock":
            print("You won!") 

        if choice=="Scissors":
            print("You lost!") 

        if choice=="Paper": 
            print("It's a draw!")

    if answer.lower() == "s":
        choice = random.choice(n)
        print('Scissors vs ' + choice)

        if choice=="Rock":
            print("You lost!") 

        if choice=="Scissors":
            print("It's a draw!") 

        if choice=="Paper": 
            print("You won!")
        

game()
