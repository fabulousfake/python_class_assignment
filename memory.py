# implementation of card game - Memory

import simplegui
import random

CARD_SIZE = [50, 100]
FRAME_SIZE = [800, 100]


num_list = range(8)
num_list.extend(range(8))
exposed = []
state = 0
card1 = -1
card2 = -1
turn_count = 0


# helper function to initialize globals
def new_game():
    global num_list, exposed, state, card1, card2, turn_count, label
    
    random.shuffle(num_list)
    exposed = [False for n in num_list]
    state = 0
    card1 = -1
    card2 = -1
    turn_count = 0
    label.set_text("Turns = " + str(turn_count))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, card1, card2, turn_count, label
    
    index = pos[0] / CARD_SIZE[0]
    
    if (exposed[index] == True):
        return
    
    exposed[index] = True
    if (state == 0):
        state = 1
        card1 = index
    elif (state == 1):
        turn_count += 1
        label.set_text("Turns = " + str(turn_count))
        state = 2
        card2 = index
    else:
        if (num_list[card1] != num_list[card2]):
            exposed[card1] = False
            exposed[card2] = False
        card1 = index
        state = 1
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    positionx = CARD_SIZE[0] / 2
    i = 0
    for num in num_list:
        if (exposed[i] == True):
            canvas.draw_text(str(num), (positionx - 10, CARD_SIZE[1] / 2 + 10), 40, 'White')
        else:
            canvas.draw_line((positionx, 0), (positionx, CARD_SIZE[1]), CARD_SIZE[0] - 1, 'Green')
        positionx += CARD_SIZE[0]
        i += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric