#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import decor
import pygame
import ClassMaze
# -tc- Ne pas oublier d'importer ClassMcGyver
import ClassMcGyver


class Application:
	"""
	a class launching the game when opening labyrinth.py
	"""

	# -tc- Je ne vois aucune raison de passer des arguments au init de cette classe
	def __init__(self, window=None, icone=None, m=None):
		#initializing application class

		pygame.init()
		# creating instances from the different classes
		self.maze = ClassMaze.Maze()
		# -tc- passer self.maze à mc_gyver
		self.mc_gyver = ClassMcGyver.McGyver("m", self.maze)

		#playing theme song looping for ever
		# -tc- Attention, le fichier s'appelle MacGyver_theme_song.mp3
		# -tc- et non Mac_Gyver_theme_song.mp3
		pygame.mixer.music.load('MacGyver_theme_song.mp3')
		pygame.mixer.music.play(-1, 0.0)
		self.window = pygame.display.set_mode((600, 600))
		icon = pygame.image.load(decor.small_icon)
		pygame.display.set_icon(icon)
		pygame.display.set_caption("Mc Gyver's Maze")
		# à voir si besoin de garder ou pas:
		# self.m = McGyver("images/img_macgyver.png", structure)
		self.background = pygame.Surface((600, 600))
		self.background.fill((255, 255, 255))
		self.window.blit(self.background, (0, 0))
		pygame.display.flip()


	def startgame(self):
		#game loop
		game_continue = 1
		while game_continue:

			pygame.time.clock().tick(30)

			for event in pygame.event.get():

				if event.type == QUIT:
					game_continue = 0

				#possibility of closing the window
				elif event == KEYDOWN:

					if event.key == K_ESCAPE:
						game = 0

					#events of mc-gyver's moves
					elif event.key == K_RIGHT:
						self.m('right')

					elif event.key == K_LEFT:
						self.m('left')

					elif event.key == K_UP:
						self.m('up')

					elif event.key == K_DOWN:
						self.m('down')

			#refreshing the window
			self.window.blit(fond, (0,0))
			self.window.blit(self.m(), (case_x, case_y))
			pygame.display.flip()

# -tc- Code de test
def main():
	app = Application()

if __name__ == "__main__":
	main()
