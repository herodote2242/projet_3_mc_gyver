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
		super().__init__(maze, display)
		self.syringe = list(self.display)
	
	def list_free_sprites():
		# function listing all the free sprites on the maze
		self.free_sprites = []
		for line_number, line in enumerate(self.structure):
			for case_number, sprite in enumerate(line):
				if sprite == ' ':
					self.free_sprites.append([line_number, case_number])

	
	def choose_free_sprites():
		#function randomly choosing a sprite for the syringe objects
		positions = random.sample(self.free_sprites, len(self.syringe))

		for position, item in zip(positions, self.syringe):
			line_number, case_numer = position
			# Position the item in self.structure
			self.structure[line_number][case_number] = item

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
