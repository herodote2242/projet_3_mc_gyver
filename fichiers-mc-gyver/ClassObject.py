#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import random
import pygame
import json
import ClassMaze as maze
import decor


class Object:
	"""
	creation of the class Objects, allowing objects'creation on the maze
	"""

	def __init__(self, maze, display):
		#initializing the objects representation

		self.display = display
		self.structure = maze.structure
		self.case_x = 0
		self.case_y = 0


class Syringe(Object):
	"""
	creation of the class Syringe, composed of 3 elements randomly distributed on the maze
	"""
	
	def __init__(self, maze, display):
		#initializing the syringe objects representation
		super().__init__(maze, syringe)
		self.display = display
		self.structure = maze.structure
		syringe = [tube, needle, ether]	

	
	def list_free_sprites():
		# function listing all the free sprites on the maze
		free_sprites = []

		with open('structure_modifiable.json', 'r') as f:
			self.structure = json.load(f)

			for line_number, line in enumerate(self.structure):
				for case_number, sprite in enumerate(line):
					x = case_number * decor.sprite_dimension
					y = line_number * decor.sprite_dimension
					if sprite == ' ':
						free_sprites.append([x,y])

	
	def choose_free_sprite():
		#function randomly choosing a sprite for the syringe objects

		for item in syringe:
			random.choice(free_sprites)
		item.display()

	#for item in syringe:
		#technique d'implémentation aléatoire à revoir
		#faire une liste des emplacements disponibles
		#en choisir un pour afficher l'objet
		#item.case_y = randrange(1, 14)
		#item.case_x = randrange(1, 14)

		#if needle.structure[needle.case_x][needle.case_y] in ["#", "m", "g"]:
			#needle.case_y = randrange(1, 14)
			#needle.case_x = randrange(1, 14)
		
		#if tube.structure[tube.case_x][tube.case_y] in ["#", "N", "m", "g"]:
			#tube.case_y = randrange(1, 14)
			#tube.case_x = randrange(1, 14)

		#if ether.structure[ether.case_x][ether.case_y] in ["#", "N", "T", "m", "g"]:
			#ether.case_y = randrange(1, 14)
			#ether.case_x = randrange(1, 14)

		#item.display()

#testing if class working correctly
def main():

	syringe = Syringe(Object)


if __name__ == "__main__":
	main()