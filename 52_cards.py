import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		
	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:

	def __init__(self):
		self.deck = [] #start with an empty list
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp =''
		for card in self.deck:
			deck_comp += '\n'+ card.__str__()
		return "The deck has: "+deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card


test_deck = Deck()
test_deck.shuffle()
print(test_deck)

class Hand:

	def __init__(self):
		self.cards = [] # start with an empty list as we did in the Deck class
		self.value = 0 #start with zero value
		self.aces = 0 #add on attribute to keep track of aces

	def add_card(self,card):
		# card passed in
		# from Deck.deal() --> single Card(suit,rank)
		self.cards.append(card)
		self.value += values[card.rank]

		# track aces
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):

		# 
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

test_deck = Deck()
test_deck.shuffle()

# PLAYER
test_player = Hand()
# Deal 1 card from the deck CARD(suit,rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

class Chips:

	def __init__(self,total=100):
		self.total = 100 # This can be set to a default value or supplied by a user input
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

	def take_bet(chips):

		while True:

			try:
				chips.bet = int(input("How many chips would you like to bet? "))
			except:
				print("Sorry please provide an interger")
			else:
				if chips.bet > chips.total:
					print("Sorry, your bet can't exceed", chips.total)
				else:

	def hit(deck,hand):
		Single_card = deck.deal()
		Hand.add_card()
		Hand.adjust_for_ace()

	def hit_or_stand(deck,hand):
	global playing # to control and upcoming while loop
		while True:
			x = input(‘Hit or Stand? Enter h or s ‘)
		if x [0].lower() == h:
			hit(deck, hand)
		elif x[0].lower() == ‘s’:
			print(“Player Stands Dealer’s Turn”)
			playing = False
		else:
			print(“Sorry, I did not understand that, Please enter h or s only!”)
			continue
		break
	
	def player_busts(player, dealer, chips):
		print("BUST PLAYER!")
		chips.lose_bet()

	def player_wins(player, dealer, chips):
		print('PLAYER WINS!')
		chips.win_bet()

	def dealer_busts(player, dealer, chips):
		print('PLAYER WINS! DEALER BUSTS!')
		chips.win_bet()

	def dealer_wins(player, dealer, chips):
		print("DEALER WINS!")
		chips.lose_bet()

	def push (player, dealer):
		print ('Dealer and player tie! PUSH')

		while True:
	# Print an opening statement
	
	print("WELCOME TO BLACKJACK")
	# Create & shuffle the deck, deal two cards to each player
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Set up the Player's chips
	
	player_chips = Chips()

	# Prompt the Player for their bet

	take_bet(player_chips)

	# Show cards (but kieep one dealer card hidden)
	show_some(player_hand, dealer_hand)

	while playing: # recall this varaiable from our hit_or_stand function

		# Prompt for Player to Hit or Stand

		# Show cards (but keep on dealer card hidden)

		# If player's hand exceeds 21, run player_bursts() and break out of loop
			
		break
	#If 



