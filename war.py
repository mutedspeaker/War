import random
# Added the four suits, and 14 ranks, plus a dictionary containing value of each rank.
suits = ('Hearts','Spades','Clubs','Diamonds')
ranks = ('Two', 'Three', 'Four','Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

# Card class, representing one single card, with a suit and a rank.
class Card:
    
    def __init__(self, suit, rank):
    
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

# Deck class representing a whole deck of 52 cards, and has functions to shuffle the deck, and deal a single card.
class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop(0)
 
# Player class, instantiates a player who basically has a name, and has access to a list of cards, which can be increased or decreased.
class Player:
    
    def __init__ (self, name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # Add a single card
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
      
# Game Setup

# Two players
player_one = Player("One")
player_two = Player("Two")

# A new and shuffled deck.
new_deck = Deck()
new_deck.shuffle()

# Distributing 26 cards to each player
for card in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
# While game_on
round_num = 0
game_on = True

while game_on:
    
    round_num += 1
    print(f"Round Number: {round_num}")
    
    if len(player_one.all_cards) == 0:
        print('Player One is all out of cards! Player two wins')
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print('Player Two is all out of cards! Player one wins')
        game_on = False
        break
    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # While at_war
    at_war = True    

    while at_war:
                            
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
    
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
    
            at_war = False
        
        else:
            print("WAR!")
            
            if len(player_one.all_cards) < 5:
                print("P1 out of cards, P2 wins!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print("P2 out of cards, P1 wins!")
                game_on = False
                break  
            
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
