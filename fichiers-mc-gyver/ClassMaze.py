#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import pygame
import json


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
		wall = deco.pygame.image.load(image_wall).convert()
		path = decor.pygame.image.load(image_path).convert()
		guardian = decor.pygame.image.load(image_guardian).convert_alpha()
		macgyver = decor.pygame.image.load(image_macgyver).convert_alpha()

		for line_number, line in enumerate(self.structure):

			for case_number, sprite in enumerate(line):
				x = case_number * decor.sprite_dimension
				y = line_number * decor.sprite_dimension

				if sprite == '#':
					window.blit(wall, (x,y))

				elif sprite == ' ':
					window.blit(path, (x,y))

				elif sprite == 'g':
					window.blit(guardian, (x,y))

#test
def main():
	maze = Maze()

if __name__ == "__main__":
	main()
