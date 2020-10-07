# region DECK OF CARDS
# import collections
# from random import choice
#
# Card = collections.namedtuple('Card', ['rank', 'suit'])
#
#
# class FrenchDeck:
# 	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
# 	suits = 'spades diamonds clubs hearts'.split()
#
# 	def __init__(self):
# 		self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
# 	def __len__(self):
# 		return len(self._cards)
#
# 	def __getitem__(self, position):
# 		return self._cards[position]
#
#
# beer_card = Card('7', 'diamonds')
# print(beer_card)  # Card(rank='7', suit='diamonds')
#
# deck = FrenchDeck()
# print(len(deck))  # 52

# region Method __getitem__

# print(deck[0])
# print(deck[-1])

# endregion

# region Choosing a random card

# print(choice(deck))
# print(choice(deck))
# print(choice(deck))

# endregion

# region Sequence
# print(deck[:3])
# print(deck[12::13])
# endregion

# region Iteration
# for card in deck:  # doctest: +ELLIPSIS
# 	print(card)
#
# for card in reversed(deck):  # doctest: +ELLIPSIS
# 	print(card)
# endregion

# region Sort cards first by value, then by suit

# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#
#
# def spades_high(card):
# 	rank_value = FrenchDeck.ranks.index(card.rank)
# 	return rank_value * len(suit_values) + suit_values[card.suit]
#
#
# for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
# 	print(card)  # from 2(*suit) to ace(*suit)

# endregion

# endregion

# region EMULATION OF NUMERIC TYPES

# from math import hypot
#
#
# class Vector:
#
# 	def __init__(self, x=0, y=0):
# 		self.x = x
# 		self.y = y
#
# 	def __repr__(self):
# 		return 'Vectot(%r, %r)' % (self.x, self.y)
#
# 	def __abs__(self):
# 		return hypot(self.x, self.y)
#
# 	def __bool__(self):
# 		return bool(abs(self))
#
# 	def __add__(self, other):
# 		x = self.x + other.x
# 		y = self.y + other.y
# 		return Vector(x, y)
#
# 	def __mul__(self, scalar):
# 		return Vector(self.x * scalar, self.y * scalar)
#
#
# v1 = Vector(2, 4)
# v2 = Vector(2, 1)
# print(v1 + v2)
#
# v = Vector(3, 4)
# print(abs(v))
#
# print(v * 3)
# print(abs(v * 3))

# endregion

# region ARRAY OF SEQUENCES

# region List inclusion and generator expressions

# # First example
# symbols = '$¢£¥€¤'
# codes = []
# for symbol in symbols:
# 	codes.append(ord(symbol))
#
# print(codes)
#
# # Reverse first example
# symbols = []
# codes = [36, 162, 163, 165, 8364, 164]
# for code in codes:
# 	symbols.append(chr(code))
#
# print(symbols)
#
# # Second example
# symbols = '$¢£¥€¤'
# codes = [ord(symbol) for symbol in symbols]
#
# print(codes)
#
# # Reverse second example
# codes = [36, 162, 163, 165, 8364, 164]
# symbols = [chr(code) for code in codes]
#
# print(symbols)

# endregion

# region Compare comparison list with map and filter

# symbols = '$¢£¥€¤'
# beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
# print(beyond_ascii)
#
# beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
# print(beyond_ascii)

# endregion

# region Cartesian products

# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
#
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)
#
# for color in colors:
# 	for size in sizes:
# 		print((color, size))
#
# tshirts = [(size, color) for size in sizes for color in colors]
# print(tshirts)
#
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)

# endregion

# region Generator expressions

# # Initializing tuple and array with generator expression
# import array
#
# symbols = '$¢£¥€¤'
# print(tuple(ord(symbol) for symbol in symbols))
#
# print(array.array('I', (ord(symbol) for symbol in symbols)))
#
# # Generating a Cartesian product by a generator expression
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
# 	print(tshirt)

# endregion

# region Tuple

# # Tuple as records with unnamed fields
# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for passport in sorted(traveler_ids):
# 	print('%s/%s' % passport)
# for country, _ in traveler_ids:
# 	print(country)
#
# # Unpacking tuples
# lax_coordinates = (33.9425, -118.408056)
# latitude, longitude = lax_coordinates
# print(latitude)
# print(longitude)


# print(divmod(20, 8))
# t = (20, 8)
# print(divmod(*t))
#
# quotient, remainder = divmod(*t)
# print(quotient, remainder)
#
# import os
#
# _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
# print(filename)


# # Using * to fetch excess items
# a, b, *rest = range(5)
# print(a, b, rest)
#
# a, b, *rest = range(3)
# print(a, b, rest)
#
# a, b, *rest = range(2)
# print(a, b, rest)
#
# a, *body, c, d = range(5)
# print(a, body, c, d)
#
# *head, b, c, d = range(5)
# print(head, b, c, d)


# Unpacking a nested tuple
metro_areas = [
	('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
	('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))


# endregion

# endregion
