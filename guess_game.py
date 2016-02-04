# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

global x, winner, guess, game_over, last_game_played

# helper function to start and restart the game
last_game_played = None
def new_game():

    # initialize global variables used in your code here
    global x, winner, guess, game_over, last_game_played
    
    if last_game_played == None:
        last_game_played = 'range100'
        
    winner = False
    game_over = False
    
    if last_game_played == 'range100': 
        range100()
        
    if last_game_played == 'range1000': 
        range1000()
             


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global x, guesses, last_game_played
    last_game_played = 'range100'
    game_over = False
    guesses = 7
    print("")
    print("New game. Range is from 0 to 100")
    print("Number of remaining guesses is 7")
    x = random.randrange(0, 100)
    #print(x)
    #print(last_game_played)



def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global x, guesses, last_game_played
    last_game_played = 'range1000'
    game_over = False
    guesses = 10
    print("")
    print("New game. Range is from 0 to 1000")
    print("Number of remaining guesses is 10")
    x = random.randrange(0, 1000)
    #print(x)
    #print(last_game_played)
    
    
    
def input_guess(guess):
    # main game logic goes here
    global guesses, winner, game_over
    print("")
    
    if (game_over != True):
        if int(guess) == x:
            winner = True
            print("Correct!")
        else:
            winner = False
            
        guesses = guesses - 1
        print("Guess was " + str(guess))

        if winner != True:
            print("Number of remaining guesses is " + str(guesses))
            if int(guess) > x:
                print("Lower!")
            else:
                print("Higher!")
        else:
            new_game()
        if guesses == 0:
            print("The game is over. You lost.")
            game_over = True
            new_game()
     

# create frame
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Range is [0, 100)", range100)
frame.add_button("Range is [0, 1000)", range1000)
frame.add_input("Enter number", input_guess, 100)
# register event handlers for control elements and start frame


# call new_game 
new_game()
