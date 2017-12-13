#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import json
import pygame
import decor


class Maze:
	"""
	a square maze made of 15 sprites width and 15 sprites height
	"""

	def __init__(self):
		"""
		sprites are displayed according to blanks or # in structure_modifiable.py
		"""
		with open('structure_modifiable.json', 'r') as f:
			self.structure = json.load(f)


	def display(self, window):
		"""
		method allowing the construction of the graphic maze with images
		"""
		wall = pygame.image.load(decor.image_wall).convert()
		path = pygame.image.load(decor.image_path).convert()
		guardian = pygame.image.load(decor.image_guardian).convert_alpha()
		macgyver = pygame.image.load(decor.image_macgyver).convert_alpha()

		for line_number, line in enumerate(self.structure):

			for case_number, sprite in enumerate(line):
				x = case_number * decor.sprite_dimension
				y = line_number * decor.sprite_dimension

				if sprite == '#':
					window.blit(wall, (x,y))

				elif sprite == ' ':
					window.blit(path, (x,y))

				elif sprite == 'g':
					window.blit(path, (x,y))
					window.blit(guardian, (x,y))

				elif sprite == "m":
					window.blit(path, (x,y))
					window.blit(macgyver, (x,y))

#testing if the maze is correctly loading
def main():
	pygame.init()
	window = pygame.display.set_mode((600, 600), RESIZABLE)
	#playing theme song looping for ever
	pygame.mixer.music.load('MacGyver_theme_song.mp3')
	pygame.mixer.music.play(-1, 0.0)
	maze = Maze()
	maze.display(window)
	pygame.display.flip()

	end = False
	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True
	pygame.quit()

if __name__ == "__main__":
	main()
