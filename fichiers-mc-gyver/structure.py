#!/usr/bin/python3
# -*- coding: Utf-8 -*

import json
import pygame
from pygame.locals import *



class Maze:
	"""
	a square maze made of 15 sprites width and 15 sprites height
	"""

	def __init__(self):
	    """
	    sprites are displayed according to blanks or # in structure_modifiable.py
	    """
	    with open('structure_modifiable.json', 'r') as f:
	    	self.data = json.load(f)


	def display(self):
		"""
		method allowing the .json (wich can be easily and-modified) to
		be displayed as a maze structure 15/15
		"""
		for line in self.data:
			print("".join(line))



def main():
	maze = Maze()
	maze.display()


if __name__ == "__main__":
	main()




pygame.init()

# image of mc gyver
img_macgyver = "images/img_macgyver.png"

window = pygame.display.set_mode((600, 600))
icone = pygame.image.load(img_macgyver.png)
pygame.display.set_icon(icone)
pygame.display.set_caption("Mc Gyver's Maze")
m = Mc_gyver("img_macgyver.png")


#game loop
game = 1
while game :

	pygame.time.clock().tick(30)

	for event in pygame.event.get():

		if event.type == QUIT:
			game = 0

		#possibility of closing the window
		elif event == KEYDOWN:

			if event.key == K_ESCAPE:
				game = 0

			#events of mc-gyver's moves
			elif event.key == K_RIGHT:
				Mc_gyver.move('right')

			elif event.key == K_LEFT:
				Mc_gyver.move('left')

			elif event.key == K_UP:
				Mc_gyver.move('up')

			elif event.key == K_DOWN:
				Mc_gyver.move('down')

	#refreshing the window
	window.blit(fond (0,0))
	window.blit(Mc_gyver.move, (case_x, case_y))
	pygame.display.flip()
