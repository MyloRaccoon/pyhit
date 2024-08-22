from tkinter import *
from PIL import Image, ImageTk

class Title_screen():

	def __init__(self, canvas, play_menu = None):
		self.play_menu = play_menu
		self.canvas = canvas
		self.bg = ImageTk.PhotoImage(Image.open("assets/black.png"))
		self.btn_quit = Button(canvas, text = 'quit', command = lambda : exit())
		self.btn_play = Button(canvas, text = 'play', command = lambda : self.go_to_play_menu(self.play_menu.create_menu))

	def create_menu(self):
		self.canvas.create_image(0,0, anchor = NW, image=self.bg)
		self.btn_play.place(x=576,y=200)
		self.btn_quit.place(x=576,y=250)

	def go_to_play_menu(self, func_create_menu):
		self.btn_quit.place_forget()
		self.btn_play.place_forget()
		func_create_menu()
