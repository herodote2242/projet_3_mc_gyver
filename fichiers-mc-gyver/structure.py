#!/usr/bin/python3
# -*- coding: Utf-8 -*

import json
import pygame

pygame.init()


"""
defining the different element's of the window
"""

sprite_number = 15
sprite_dimension = 40
window_dimension = sprite_number * sprite_dimension
window_title = "Mac Gyver's Maze"
small_icon = "images/img_macgyver.png"
image_wall = "images/img_wall.png"
image_path = "images/img_path.png"
image_macgyver = "images/img_macgyver.png"
image_guardian = "images/img_guardian.png"



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


	def display(self, window):
		"""
		method allowing the construction of the graphic maze with images
		"""
		wall = pygame.image.load(image_wall).convert()
		path = pygame.image.load(image_path).convert()
		guardian = pygame.image.load(image_guardian).convert_alpha()
		macgyver = pygame.image.load(image_macgyver).convert_alpha()
		line_number = 0

		for line in self.structure:
			case_number = 0

			for sprite in line:
				x = case_number * sprite_dimension
				y = line_number * sprite_dimension

				if sprite == '#':
					window.blit(wall, (x,y))

				elif sprite == ' ':
					window.blit(path, (x,y))

				elif sprite == 'g':
					window.blit(guardian, (x,y))
				case_number += 1
			line_number += 1





def main():
	maze = Maze()
	maze.display()


if __name__ == "__main__":
	main()



class Application:


	def __init__(self):

		self.window = pygame.display.set_mode((600, 600))
		self.icone = pygame.image.load(img_macgyver.png)
		pygame.display.set_icon(icone)
		pygame.display.set_caption("Mc Gyver's Maze")
		self.m = Mc_gyver("img_macgyver.png")


	def startgame(self):
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
			self.window.blit(fond (0,0))
			self.window.blit(Mc_gyver.move, (case_x, case_y))
			pygame.display.flip()
