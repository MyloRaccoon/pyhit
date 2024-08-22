from tkinter import *
from PIL import Image, ImageTk

class Game_screen():

	def __init__(self, canvas, game, title_screen):
		self.canvas = canvas
		self.game = game
		self.bg = ImageTk.PhotoImage(Image.open("assets/black.png"))
		self.btn_quit_game = Button(canvas, text = 'quit', command = lambda : self.exit_to_title(title_screen.create_menu))
		self.btn_continue = Button(canvas, text = 'oui', command = lambda : self.make_draw())
		self.btn_stop = Button(canvas, text = 'non', command = lambda : self.end_turn())
		self.btn_steal = Button(canvas, text = 'oui', command = lambda : None)
		self.btn_not_steal = Button(canvas, text = 'non', command = lambda : self.ask_continue())
		self.btn_card = Button(self.canvas, text = None, command = None)

	def start_game(self):
		self.game.initiate_game()
		self.reset_canvas()
		self.print_game()
		self.btn_quit_game.place(x=1000, y=10)
		self.make_draw()

	def print_players(self):
		for index in range(len(self.game.all_player)):
			player = self.game.all_player[index]
			self.canvas.create_text(index*150+50,50, text=player.name, fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)
			for jndex in range(len(player.hand)):
				self.canvas.create_text(jndex*20+index*150,100, text=player.hand[jndex], fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)
		self.canvas.create_text(5,200, text=f'Au tour de {self.game.current_player.name}', fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)

	def ask_continue(self):
		if len(self.game.card_pile.pile) != 0:
			self.reset_canvas()
			self.print_game()
			self.canvas.create_text(400,300, text='Continuer ?', fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)
			self.btn_continue.place(x=200, y=350)
			self.btn_stop.place(x=300, y=350)
		else:
			self.win_screen()

	def ask_steal(self, n_card, v_card):
		self.reset_canvas()
		self.print_game()
		msg = f'Voulez-vous voler {n_card} de valeur {v_card} ?'
		self.canvas.create_text(100,300, text=msg, fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)
		self.btn_steal.config(command = lambda : self.steal(v_card))
		self.btn_steal.place(x=200, y=350)
		self.btn_not_steal.place(x=300, y=350)

	def steal(self, card):
		self.game.steal(card)
		self.ask_continue()

	def reset_canvas(self):
		self.canvas.create_image(0,0, anchor=NW, image=self.bg)
		self.btn_continue.place_forget()
		self.btn_stop.place_forget()
		self.btn_steal.place_forget()
		self.btn_not_steal.place_forget()
		self.btn_card.place_forget()

	def print_game(self):
		self.print_players()
		self.canvas.create_text(1000, 650, text=f'Il reste {len(self.game.card_pile.pile)}cartes', fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)

	def make_draw(self):
		self.reset_canvas()
		self.print_game()
		player = self.game.current_player
		card = player.draw()
		if card != -1:
			self.btn_card.config(text = str(card), command = lambda: self.make_draw_next(player, card))
			self.btn_card.place(x=200, y=350)
		else:
			self.win_screen()

	def make_draw_next(self, player, card):
		self.reset_canvas()
		self.print_game()
		if not player.is_dead(card):
			can_steal = self.game.can_steal(card)
			if can_steal != 0:
				self.ask_steal(can_steal, card)
			else:
				self.ask_continue()
		else:
			self.end_turn()

	def end_turn(self):
		self.game.turn()
		self.game.current_player.banking()
		self.reset_canvas()
		self.print_game()
		self.make_draw()

	def exit_to_title(self, function):
		self.btn_card.place_forget()
		self.btn_continue.place_forget()
		self.btn_steal.place_forget()
		self.btn_stop.place_forget()
		self.btn_not_steal.place_forget()
		self.btn_quit_game.place_forget()
		function()

	def win_screen(self):
		for player in self.game.all_player:
			player.banking()
		self.reset_canvas()
		classement = self.game.get_classement()
		for i in range(len(classement)):
			step = classement[i]
			self.canvas.create_text(50, 50 + i*100, text=f'{len(classement) - i} | {step[1]} : {step[0]}', fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)