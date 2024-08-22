class Player():

	def __init__(self, name, game):
		self.name = name
		self.game = game
		self.bank = 0
		self.hand = []
		self.index_card_storage = []

	def __str__(self):
		string = ''
		for card in self.hand:
			string += f' {str(card)}'
		return string

	def reset(self):
		self.bank = 0
		self.hand = []
		self.index_card_storage = []

	def banking(self):
		for card in self.hand:
			self.bank += card
		self.hand.clear()

	def recurence(self, e, l):
		i = 0
		for element in l:
			if e == element:
				i += 1
		return i

	def draw(self):
		if len(self.game.card_pile.pile) != 0:
			card = self.game.card_pile.draw()
			self.hand.append(card)
		else:
			card = -1
		return card

	def is_dead(self, card):
		if self.recurence(card, self.hand) >= 2 and len(self.hand) > self.game.card_limit:
			self.hand = []
			return True
		return False