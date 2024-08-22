from random import shuffle
from progs.player import Player
class Game():

	def  __init__(self):
		self.card_limit = 3
		self.n_s_card = 11
		self.n_l_card = 7

		self.all_player = [Player('player1', self), Player('player2', self)]

		self.current_player_i = 0
		self.current_player = self.all_player[0]

		self.card_pile = Pile(self.n_s_card, self.n_l_card)

	def initiate_game(self):
		self.card_pile.__init__(self.n_s_card, self.n_l_card)
		for player in self.all_player:
			player.reset()

	def turn(self):
		self.current_player_i += 1
		self.current_player_i %= len(self.all_player)
		self.current_player = self.all_player[self.current_player_i]

	def can_steal(self, value):
		n_stealed_card = 0
		for player in self.all_player:
			player.index_card_storage.clear()
			if player != self.current_player:
				for i in range(len(player.hand)):
					if player.hand[i] == value:
						player.index_card_storage.append(i)
						n_stealed_card += 1
		return n_stealed_card

	def steal(self, value):
		for player in self.all_player:
			if player != self.current_player:
				for i in player.index_card_storage:
					self.current_player.hand.append(player.hand.pop(i)) 
					for j in range(len(player.index_card_storage)):
						player.index_card_storage[j] -= 1

	def get_classement(self):
		classment = []
		for player in self.all_player:
			classment.append((player.bank, player.name))
		classment.sort()
		return classment

class Pile():

	def __init__(self, n_s_card, n_l_card):
		self.pile = []
		self.n_s_card = n_s_card
		self.n_l_card = n_l_card

		for i in range(self.n_s_card):
			for j in range(1,6):
				self.pile.append(j)

		for i in range(self.n_l_card):
			for j in range(6, 11):
				self.pile.append(j)

		shuffle(self.pile)

	def __len__(self):
		return len(self.pile)

	def draw(self):
		return self.pile.pop(0)