#Used for card shuffle
import random
#boolean used to know if hand is in play
playing=False

chip_pool=int(input("please enter the number of chip pools you want: "))
bet=1
restart_phrase="press 'd' to deal the cards again, or pres  'q' to quit"

#heart, diamond, clubs and spades
suits=('H','D','C','S')

#possible card ranks
ranking=('A','2','3','4','5','6','7','8','9','10','J','Q','K')

#Point values dict (Note:Aces can also be 11, check self.ace for details
card_val={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

class card:
    def __init__(self,suit, rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.suit+self.rank
    def grab_suit(self):
        return self.suit
    def grab_rank(self):
        return self.rank
    def draw(self):
        print (self.suit + self.rank)

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        #Aces can be 1 or 11. so need to define it here
        self.ace=False
    def __str__(self):
        '''Return a string of current hand composition'''
        hand_comp=""
        for card in self.cards:
            card_name=card.__str__()
            hand_comp=hand_comp+" "+card_name
        return 'The hand has %s'%hand_comp
    def card_add(self,card):
        '''Add another card to the hand'''
        self.cards.append(card)

        #check for Aces
        if card.rank=='A':
            self.ace=True
        self.value=self.value+card_val[card.rank]
    def calc_val(self):
        '''calculate the value of the hand, make aces an 11 if they don't bust the hand'''
        if (self.ace==True and self.value<12):
            return self.value+10
        else:
            return self.value
    def draw(self,hidden):
        if hidden==True and playing==True:
            #don't show first hidden card
            starting_card=1
        else:
            starting_card=0
        for x in range(starting_card,len(self.cards)):
            self.cards[x].draw()

class Deck:
    def __init__(self):
        '''create a deck in order'''
        self.deck=[]
        for suit in suits:
            for rank in ranking:
                self.deck.append(card(suit,rank))
    def shuffle(self):
        '''shuffle the deck, python actually already has a shuffle method in its random lib'''
        random.shuffle(self.deck)
    def deal(self):
        '''Grab the first item in the deck'''
        single_card=self.deck.pop()
        return single_card
    def __str__(self):
        deck_comp=""
        for card in self.cards:
            deck_comp=deck_comp+" "+ deck_comp.__str__()
        return "the deck has" + deck_comp
    # First Bet
def make_bet():
    '''Ask the player for the bet amount and '''
    global bet
    bet=0
    print ('what amount of chips would you like to bet? (Enter whole integer please)')

    #while loop to keep asking for the bet
    while bet==0:
        bet_comp=input() #use bet_comp as a checker
        bet_comp=int(bet_comp)
        #check to make sure bet is within the remaining amount of chips le