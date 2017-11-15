#!/usr/bin/python3
# -*- coding: Utf-8 -*

from structure import *
from gardien import *


class Mc_gyver:
	
	def __init__(self, structure):
		self.case_x = 1
		self.case_y = 1
		self.structure = structure


	def moves(self, direction):
		"""movements of the main character in the maze"""
		if direction == 'right':
			if self.structure[self.case_y][self.case_x+1] != '#':
				self.case_x += 1

		if direction == 'left':
			if self.structure[self.case_y][self.case_x-1] != '#':
				self.case_x -= 1

		if direction == 'up':
			if self.structure[self.case_y-1][self.case_x] != '#':
				self.case_y -= 1

		if direction == 'down':
			if self.structure[self.case_y+1][self.case_x] != '#':
				self.case_y += 1

		if Mc_gyver.self.case_x, Mc_gyver.self.case_y = 14, 14:
			end = True


def main():
	#loop of the game : Mc Gyver is moving until the exit

	end = False

	while not end:
		#to be replaced by "for event in pygame.event.get()" when importing pygame
		response = input("where do you want to go?")

		if response in ["left", "right", "up", "down"]:
			Mc_gyver.moves(response)

		#up to date maze after each movement

	if Mc_gyver.self.case_x, Mc-gyver.self.case_y = 14, 14:
		print("You win !")
		#add an automatic function "exit window"

def count_objects():
	pass
	#to be replaced by une function when objects implemented