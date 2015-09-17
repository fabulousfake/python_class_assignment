# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# uncomment line 31 if you want to check the code

import simplegui
import random

# initialize global variables used in your code
number = -1
max_range = 0
max_guess_count = 0
cur_guess_count = 0

# helper function to start and restart the game
def new_game():
    # start with default of 100 so that the user can get started
    global number, max_range, max_guess_count, cur_guess_count
    
    if (max_range == 0):
        max_range = 100
        max_guess_count = 7
    
    number = random.randrange(0, max_range)
    cur_guess_count = 0
    
    print "New Game! Start guessing between [0,", max_range, ")"
    print max_guess_count, "guess(es) remaining"
    print
    
#    print number
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global max_range, max_guess_count
    
    max_range = 100
    max_guess_count = 7

    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global max_range, max_guess_count
    
    max_range = 1000
    max_guess_count = 10
    
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global number, cur_guess_count, max_guess_count, max_range
    
    my_guess = int(guess)
    cur_guess_count += 1
 
    if (my_guess < 0 or my_guess >= max_range):
        print "Error number not in range. Enter another number"
        return None
    
    guess_diff = max_guess_count - cur_guess_count
    
    if (my_guess < number):
        print "Guess higher than", my_guess
    elif (my_guess > number):
        print "Guess lower than", my_guess
    elif (my_guess == number):
        print "You got it genius!"
        print "Let's play again!"
        print
        new_game()
        return None
    
    print guess_diff, "guess(es) remaining"
    print
    if (guess_diff == 0):
        print "Sorry! You are out of guesses. The number is ", number
        print "Try again!"
        print
        new_game()
        return None
    
# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements
button1 = frame.add_button("Range [0 - 100)", range100)
button2 = frame.add_button("Range [0 - 1000)", range1000)
inp = frame.add_input("Take a guess", input_guess, 100)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
