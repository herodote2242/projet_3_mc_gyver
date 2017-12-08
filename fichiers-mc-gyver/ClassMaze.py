#!/usr/bin/env python3
# -*- coding: Utf-8 -*
# -tc- D'abord les imports de la bibliothèque standard
import json
# -tc- Ensuite les bibliothèques tièrces
import pygame
# -tc- Finalement nos propres imports
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
			# -tc- renommer data et structure, puisque par la suite tu fais référence
			# -tc- à structure
			self.structure = json.load(f)


	def display(self, window):
		"""
		method allowing the construction of the graphic maze with images
		"""
        # -tc- correction de typo: deco -> decor
		# -tc- par ailleurs, les decor préfixent les images
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
					window.blit(guardian, (x,y))

				# -tc- Ajout d'une condition pour McGyver
				elif sprite == 'm':
					window.blit(macgyver, (x, y))



# -tc- Ici, on va tester si notre si le labyrinthe se charge
def main():
	pygame.init()
	window = pygame.display.set_mode((600, 600))
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
