command = input('Command: ')
from numpy import *
def game():
    print("Welcome to Rock-paper-scissor")
    x = input("Enter Your Move: ")
    y = random.randint(3)

    if x == 'rock':
        z = 'rock'
    elif x == 'scissor':
        z = 'scissor'
    elif x == 'paper':
        z = 'paper'

    if y == 1:
        print("Computer's Move: Rock")
        if z == 'rock':
            print('Draw')
        elif z == 'paper':
            print("Nah you'd win")
        elif z == 'Scissor':
            print('You lose!')



    elif y == 2:
        print("Computer's Move: Scissor")

        if z == 'scissor':
            print('Draw')
        elif z == 'rock':
            print("Nah you'd win")
        elif z == 'paper':
            print('You lose!')






    elif y == 0:
        print("Computer's Move: Paper")
        if z == 'paper':
            print('Draw')
        elif z == 'scissor':
            print("Nah you'd win")
        elif z == 'rock':
            print('You lose!')
            
            
if command == 'game':
    game()
     
    


