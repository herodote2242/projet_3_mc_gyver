#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import decor
import pygame
from pygame.locals import*
import ClassMaze
import ClassMcGyver


class Application:
	"""
	a class launching the game when opening labyrinth.py
	"""

	def __init__(self):
		#initializing application class

		pygame.init()
		# creating instances from the different classes
		self.maze = ClassMaze.Maze()
		self.mc_gyver = ClassMcGyver.McGyver("m", self.maze)
		
		#playing theme song looping for ever
		pygame.mixer.music.load('MacGyver_theme_song.mp3')
		pygame.mixer.music.play(-1, 0.0)
		#creating the window
		self.window = pygame.display.set_mode((600, 600))
		icon = pygame.image.load(decor.small_icon)
		pygame.display.set_icon(icon)
		pygame.display.set_caption("Mc Gyver's Maze")
		# à voir si besoin de garder ou pas:
		#self.m = McGyver("images/img_macgyver.png", structure)


	def startgame(self):
		#game loop
		game_continue = 1
		while game_continue:

			pygame.time.Clock().tick(30)

			for event in pygame.event.get():

				#possibility of closing the window
				if event == KEYDOWN:

					if event.key == K_ESCAPE:
						game_continue = 0

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

# test
def main():
	app = Application()

if __name__ == "__main__":
	main()