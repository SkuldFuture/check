from random import *


class Card(object):
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def card_value(self):
		"""Returns the number of points that the card gives"""
		if self.rank in "TJQK":
			# Ten, Jalet, Quine, King equal ten points
			return 10
		else:
			# Returns the required number of points for any other card
			# An Ace initially gives 1 point
			return "A23456789".index(self.rank) + 1

	def get_rank(self):
		return self.rank

	def __str__(self):
		return "%s%s" % (self.rank, self.suit)


class Hand(object):
	def __init__(self, name):
		# Player name
		self.name = name
		# Initially the hand is empty
		self.cards = []

	def add_card(self, card):
		"""Adds a card to the hand"""
		self.cards.append(card)

	def get_value(self):
		"""Method of obtaining the number of points on the hand"""
		result = 0
		# Number of aces on hand
		aces = 0
		for card in self.cards:
			result += card.card_value()
			# If there is an ace on your hand - increase the number of aces
			if card.get_rank() == "A":
				aces += 1
		# Decide to count aces for 1 point or 11 points
		if result + aces * 10 <= 21:
			result += aces * 10
		return result

	def __str__(self):
		text = "%s's contains:\n" % self.name
		for card in self.cards:
			text += str(card) + " "
		text += "\nHand value: " + str(self.get_value())
		return text


class Deck(object):
	def __init__(self):
		# Ranks
		ranks = "23456789TJQKA"
		# Suits
		suits = "DCHS"
		# List generator creating a deck of 52 cards
		self.cards = [Card(r, s) for r in ranks for s in suits]
		# Shuffle the deck. Remember to import the "shuffle function" from the "random module"
		shuffle(self.cards)

	def deal_card(self):
		"""Card delivery function"""
		return self.cards.pop()


def new_game():
	# Create a deck
	d = Deck()
	# Set hands for the player and dealer
	player_hand = Hand("Player")
	dealer_hand = Hand("Dealer")
	# we give 2 cards to the player
	player_hand.add_card(d.deal_card())
	player_hand.add_card(d.deal_card())
	# we give 1 card to the dealer
	dealer_hand.add_card(d.deal_card())
	print(dealer_hand)
	print("="*20)
	print(player_hand)
	# Check flag to continue the game
	in_game = True
	# It makes sense for a player to draw cards only if he has less than 21 points on his hand
	while player_hand.get_value() < 21:
		ans = input("Hit or stand? (h\s) ")
		if ans == "h":
			player_hand.add_card(d.deal_card())
			print(player_hand)
			# If the player has too much, it makes no sense for the dealer to draw cards
			if player_hand.get_value() > 21:
				print("You lose")
				in_game = False
		else:
			print("You stand!")
			break
	print("=" * 20)
	if in_game:
		# According to the rules, the dealer is obliged to draw cards while his account is less than 17
		while dealer_hand.get_value() < 17:
			dealer_hand.add_card(d.deal_card())
			print(dealer_hand)
			# If the dealer has too much play it makes no sense - player won
			if dealer_hand.get_value() > 21:
				print("Dealer bust")
				in_game = False
	if in_game:
		# if no one had a bust - a comparison of the player's and dealer's points
		# In this version, if the dealer and the player have the same amount of points, the casino wins
		if player_hand.get_value() > dealer_hand.get_value():
			print("YOU WIN")
		else:
			print("DEALER WIN")


new_game()