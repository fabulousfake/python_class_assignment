# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        string = "Hand contains "
        for i in range(len(self.cards)):
            string += str(self.cards[i]) + ' '
        return string
         
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        ace_count = 0
        for i in range(len(self.cards)):
            rank = self.cards[i].get_rank()
            value += VALUES[rank]
            if (rank == 'A'):
                ace_count += 1
        
        if ace_count:
            if value + 10 <= 21:
                return (value + 10)
        
        return value

        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + i * CARD_SIZE[0], pos[1]])
            if (((pos[0] + i * CARD_SIZE[0]) + CARD_SIZE[0]) == 600):
                print "Error card is printed out of frame!"
            

player_hand = Hand()
dealer_hand = Hand()

# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        card = self.deck[-1]
        self.deck.remove(card)
        return card
    
    def __str__(self):
        # return a string representing the deck
        string = "Deck contains "
        for i in range(len(self.deck)):
            string += str(self.deck[i]) + ' '
        return string

deck = Deck()

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, score

    if in_play:
        score -= 1
        outcome = "You lose!"
        in_play = False
        return
    
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    print "Player", player_hand
    print "Dealer", dealer_hand
    
    in_play = True
    outcome = ""

def hit():
    # if the hand is in play, hit the player
    global in_play, outcome, player_hand, deck, score
    
    print "Hit! Player", player_hand
    
    if in_play:
        print "In play"
        value = player_hand.get_value()
        print "Hand value before hit = ", value
        
        if value <= 21:
            player_hand.add_card(deck.deal_card())
            print "Added: ", player_hand
            value = player_hand.get_value()
            if value > 21:
                outcome = "You are busted!"
                in_play = False
                print "You are busted!"
                print "Hand value after hit = ", value
                score -= 1
        else:
            print "We may never get here"
            outcome = "You are busted!"
            in_play = False
            print "You are busted!"
            score -= 1
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, player_hand, dealer_hand, deck, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()
        if player_value > 21:
            print "Player you are busted!"
            outcome = "You are busted!"
            in_play = False
            score -= 1
            return
        else:
            while ((dealer_value <= 17) and (dealer_value < player_value)):
                dealer_hand.add_card(deck.deal_card())
                dealer_value = dealer_hand.get_value()
                print "Dealer Hand", dealer_hand, "Dealer value", dealer_value
            
            print "Player Hand = ", player_hand, "Dealer Hand = ", dealer_hand
            print "Player value = ", player_value, "Dealer value = ", dealer_value
            
            if ((player_value > dealer_value) or (dealer_value > 21)):
                outcome = "You win!"
                in_play = False
                score += 1
                print "Player you win!"
            else:
                outcome = "Dealer wins!"
                in_play = False
                score -= 1
                print "Dealer wins!"
            

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_hand, dealer_hand, in_play, outcome, score
    
    player_hand.draw(canvas, [100, 400])
    dealer_hand.draw(canvas, [100, 200])
    
    canvas.draw_text("Blackjack", [100, 75], 35, 'Aqua')
    canvas.draw_text("Dealer", [100, 175], 25, 'Black')
    canvas.draw_text("Player", [100, 375], 25, 'Black')
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_SIZE[0]/2, 200 + CARD_BACK_SIZE[1]/2], CARD_BACK_SIZE)
        canvas.draw_text("Hit or Stand?", [200, 375], 25, 'Black')
    else:
        canvas.draw_text("New Deal?", [200, 375], 25, 'Black')
        
    canvas.draw_text(outcome, [200, 175], 25, 'Black')
    canvas.draw_text("Score: " + str(score), [400, 75], 25, 'Black')
    
    
    # card = Card("S", "A")
    # card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
print "Player", player_hand
frame.start()


# remember to review the gradic rubric