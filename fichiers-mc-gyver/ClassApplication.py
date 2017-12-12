#!/usr/bin/env python3
# -*- coding: Utf-8 -*

# grâce à différentes sources (coding with pygame, un autre labyringht sur internet)
# j'ai remarqué que sans les lignes d'import de sys et de pygame.locals, il y avait des erreurs 
# à partir de la ligne 53 sur les éléments QUIT, KEY_DOWN, KEY_ESCAPE, etc...
# quid également de l'utilité des lignes 54 à 57
import sys
import pygame
from pygame.locals import *
import ClassMaze
import ClassMcGyver
import ClassObject
import decor



class Application:
	"""
	a class launching the game when opening labyrinth.py
	"""

	def __init__(self, window=None, icon=None, m=None):
		#initializing application class

		pygame.init()
		# creating instances from the different classes
		self.maze = ClassMaze.Maze()
		self.mc_gyver = ClassMcGyver.McGyver(self.maze)
		
		#playing theme song looping for ever
		# pygame.mixer.music.load('MacGyver_theme_song.mp3')
		# pygame.mixer.music.play(-1, 0.0)

		#creating the window
		self.window = pygame.display.set_mode((600, 600))
		self.icon = pygame.image.load(decor.small_icon)
		pygame.display.set_icon(self.icon)
		pygame.display.set_caption("Mc Gyver's Maze")
		# à voir si besoin de garder ou pas:
		#self.m = McGyver("images/img_macgyver.png", structure)
		pygame.display.flip()


	def startgame(self):
		#game loop
		game_continue = True
		while game_continue:

			pygame.time.Clock().tick(30)
			pygame.event.pump()
			# A key has been pressed

			for event in pygame.event.get():
				# a vérifier le bien fondé de ces 3 lignes
				if event.type == QUIT:
					game_continue = False

				elif event.type == KEYDOWN:
					#possibility of closing the window
					if event.key == K_ESCAPE:
						game_continue = False

					#events of mc-gyver's moves
					elif event.key == K_RIGHT:
						self.mc_gyver.move('right')

					elif event.key == K_LEFT:
						self.mc_gyver.move('left')

					elif event.key == K_UP:
						self.mc_gyver.move('up')

					elif event.key == K_DOWN:
						self.mc_gyver.move('down')
			#pygame.display.update()

			#refreshing the window
			#à voir si nécessaire car pas de fond initialisé en 0,0
			#self.window.blit(fond, (0,0))
			#self.window.blit(self.window, (self.mc_gyver.case_x, self.mc_gyver.case_y))
			if game_continue:
				self.maze.display(self.window)
				pygame.display.flip()

		pygame.quit()

# test
def main():
	app = Application()

if __name__ == "__main__":
	main()
