from tkinter import *
from PIL import Image, ImageTk
from progs.player import Player

class Name_changer():

	def  __init__(self, player, x, y, canvas, menu):
		self.menu = menu
		self.player = player
		self.btn = Button(canvas, text = 'change name', command = lambda : self.change_name())
		self.entry = Entry(canvas, font=('Helvetica', 16, 'bold'))
		self.x = x 
		self.y = y 
		self.state = 'change'
		self.btn.place(x = self.x, y = self.y)

	def change_name(self):
		self.state = 'confirm'
		self.entry.place(x=self.x,y= self.y + 20)
		self.btn.config(text = 'confirm', command = lambda : self.confirm_name())

	def confirm_name(self):
		self.state = 'change'
		self.player.name = self.entry.get()
		self.entry.place_forget()
		self.btn.config(text = 'change name', command = lambda : self.change_name())
		self.menu.update_play_menu()

class Play_menu():

	def __init__(self, game, canvas, title_screen, game_screen):
		self.bg = ImageTk.PhotoImage(Image.open("assets/black.png"))
		self.canvas = canvas
		self.game = game
		self.all_name_changer = []
		self.btn_add_player = Button(self.canvas, text = 'add player', command = lambda : self.add_player())
		self.btn_remove_player = Button(self.canvas, text = 'remove player', command = lambda : self.remove_player())
		
		self.btn_add_s_card = Button(self.canvas, text = '+', command = lambda : self.add_s_card())
		self.btn_remove_s_card = Button(self.canvas, text = '-', command = lambda : self.remove_s_card())
		self.btn_add_l_card = Button(self.canvas, text = '+', command = lambda : self.add_l_card())
		self.btn_remove_l_card = Button(self.canvas, text = '-', command = lambda : self.remove_l_card())

		self.btn_start = Button(canvas, text = 'start', command = lambda : self.exit_play_menu(game_screen.start_game))
		self.btn_back = Button(canvas, text = 'back', command = lambda : self.exit_play_menu(title_screen.create_menu))

	def create_menu(self):
		self.create_name_changer()

		self.update_play_menu()

		self.btn_add_player.place(x=300,y=150)
		self.btn_remove_player.place(x=400,y=150)

		self.btn_add_s_card.place(x=700, y=260)
		self.btn_remove_s_card.place(x=750, y=260)
		self.btn_add_l_card.place(x=700, y=310)
		self.btn_remove_l_card.place(x=750, y=310)

		self.btn_start.place(x=500,y=500)
		self.btn_back.place(x=1000,y=650)

	def update_play_menu(self):
		self.canvas.create_image(0,0, anchor = NW, image=self.bg)
		for index in range(len(self.game.all_player)):
			self.canvas.create_text(index*150+50,50, text=self.game.all_player[index].name, fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)
		self.canvas.create_text(150,250, text=f'nombre de petites cartes (1 à 5) : {self.game.n_s_card}', fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)
		self.canvas.create_text(150,300, text=f'nombre de grosses cartes (6 à 10) : {self.game.n_l_card}', fill='white', font=("Comic Sans MS", "20", "bold"), anchor=NW)

	def create_name_changer(self):
		for index in range(len(self.game.all_player)):
			self.all_name_changer.append(Name_changer(self.game.all_player[index], index*150+75, 100, self.canvas, self))

	def is_changing_name(self):
		for name_changer in self.all_name_changer:
			if name_changer.state == 'confirm':
				return True
		return False

	def add_player(self):
		if len(self.game.all_player) < 8 and not self.is_changing_name():
			player = Player(f'player{len(self.game.all_player)+1}', self.game)
			self.game.all_player.append(player)
			self.all_name_changer.append(Name_changer(player, (len(self.game.all_player)-1)*150+75, 100, self.canvas, self))
			self.update_play_menu()

	def remove_player(self):
		if len(self.game.all_player) > 2 and not self.is_changing_name():
			self.game.all_player.pop(-1)
			self.all_name_changer[-1].btn.place_forget()
			self.all_name_changer.pop(-1)
			self.update_play_menu()

	def add_s_card(self):
		if self.game.n_s_card < 20:
			self.game.n_s_card += 1
		self.update_play_menu()

	def remove_s_card(self):
		if self.game.n_s_card > 2:
			self.game.n_s_card -= 1
		self.update_play_menu()

	def add_l_card(self):
		if self.game.n_l_card < 20:
			self.game.n_l_card += 1
		self.update_play_menu()

	def remove_l_card(self):
		if self.game.n_l_card > 2:
			self.game.n_l_card -= 1 
		self.update_play_menu()

	def remove(self):
		for name_changer in self.all_name_changer:
			name_changer.btn.place_forget()
		self.btn_add_player.place_forget()
		self.btn_remove_player.place_forget()
		self.btn_add_s_card.place_forget()
		self.btn_remove_s_card.place_forget()
		self.btn_add_l_card.place_forget()
		self.btn_remove_l_card.place_forget()
		self.btn_start.place_forget()
		self.btn_back.place_forget()

	def exit_play_menu(self, function):
		if not self.is_changing_name():
			self.remove()
			function()