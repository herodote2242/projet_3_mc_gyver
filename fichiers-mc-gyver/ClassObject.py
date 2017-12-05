#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from random import randrange
import labyrinthe
import decor
import structure_modifiable


WALL = '#'


class Object:
	"""
	creation of the class Objects, allowing random creation on the maze
	"""

	def __init__(self, structure, display):
		"""
		initializing the objects representation
		"""
		self.display = display
		self.structure = structure
		self.case_x = case_x
		self.case_y = case_y


maze = Maze()
needle = Object('N', maze)
tube = Object('T', maze)
ether = Object('E', maze)
Mc_gyver = McGyver('m', maze)
Guardian = Object('g', maze)
syringe = [needle, ether, tube]


for item in syringe:

	item.case_y = randrange(1, 14)
	item.case_x = randrange(1, 14)

	if needle.structure[needle.case_x][needle.case_y] in ["#", "m", "g"]:
		needle.case_y = randrange(1, 14)
		needle.case_x = randrange(1, 14)
	
	if tube.structure[tube.case_x][tube.case_y] in ["#", "N", "m", "g"]:
		tube.case_y = randrange(1, 14)
		tube.case_x = randrange(1, 14)

	if ether.structure[ether.case_x][ether.case_y] in ["#", "N", "T", "m", "g"]:
		ether.case_y = randrange(1, 14)
		ether.case_x = randrange(1, 14)

	item.display()
