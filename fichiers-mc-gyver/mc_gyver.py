#!/usr/bin/python3
# -*- coding: Utf-8 -*

from structure import *
from gardien import *


class Mc_gyver:
	
	def __init__(self, right, left, up, down):
		self.case_x = 1
		self.case_y = 1


	def moves(self, direction):
		"""movements of the main character in the maze"""
		if direction == 'right':
			if self.structure[self.case_y][self.case_x+1] != '#':
				self.case_x += 1

		if direction == 'left':
			if self.structure[self.case_y][self.case_x-1] != '#':
				self.case_x -= 1

		if direction == 'up':
			if self.structure_modifiable[self.case_y-1][self.case_x] != '#':
				self.case_y -= 1

		if direction == 'down':
			if self.structure_modifiable[self.case_y+1][self.case_x] != '#':
				self.case_y += 1

#loop of the game : Mc Gyver is moving until the exit
while Mc_gyver.self.case_x, Mc-gyver.self.case_y != 14, 14:

	for event in py:
		#to be replaced by "for event in pygame.event.get()" when importing pygame
		if event.key == K_RIGHT:
			Mc_gyver.moves('right')

		if event.key == K_LEFT:
			Mc_gyver.moves('left')

		if event.key == K_UP:
			Mc_gyver.moves('up')

		if event.key == K_DOWN:
			Mc_gyver.moves('down')

	if Mc_gyver.self.case_x, Mc-gyver.self.case_y = 14, 14:
		print("You win !")
		#add an automatic function "exit window"

def count_objects():
	pass
	#to be replaced by une function when objects implemented