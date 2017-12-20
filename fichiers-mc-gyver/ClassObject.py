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
	
	def list_free_sprites(self):
		# function listing all the free sprites on the maze
		self.free_sprites = []
		for line_number, line in enumerate(self.structure):
			for case_number, sprite in enumerate(line):
				if sprite == ' ':
					self.free_sprites.append([line_number, case_number])

	
	def choose_free_sprites(self):
		#function randomly choosing a sprite for the syringe objects
		positions = random.sample(self.free_sprites, len(self.syringe))
		for position, item in zip(positions, self.syringe):
			line_number, case_number = position
			#position the item in self.structure
			self.structure[line_number][case_number] = item



#testing if class working correctly
def main():

	syringe = Syringe(Object)


if __name__ == "__main__":
	main()