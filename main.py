from progs.game import Game
from progs.player import Player
from progs.play_menu import Play_menu
from progs.title_screen import Title_screen
from progs.game_screen import Game_screen
from tkinter import *
from PIL import Image, ImageTk

screen = Tk()
screen.title('Hit')
screen.configure(background='black')
screen.geometry("1280x720")
screen.resizable(True, True)

canvas = Canvas(screen, width='1280',height='720',bg='black', highlightthickness=0)
canvas.place(x=0,y=0)

game = Game()

title_screen = Title_screen(canvas)

game_screen = Game_screen(canvas, game, title_screen)

play_menu = Play_menu(game, canvas, title_screen, game_screen)

title_screen.play_menu = Play_menu(game, canvas, title_screen, game_screen)

title_screen.create_menu()

mainloop()