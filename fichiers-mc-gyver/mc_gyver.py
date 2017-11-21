#!/usr/bin/python3
# -*- coding: Utf-8 -*

import structure
import gardien



class Mc_gyver:
	
	"""
	creation of the class Mc_Gyver, allowing to define itself and its movement method
	"""

	def __init__(self, structure):
		self.case_x = 1
		self.case_y = 1
		self.structure = structure


	def count_objects():
		pass
		#to be replaced by une function when objects implemented


	def move(self, direction):
		"""movements of the main character in the maze"""
		
		def is_wall():
			"""
			verification of the existence of a wall allowing or not the movement
			"""
			if self.structure[self.case_x][self.case_y] == "#":
				is_wall(self.structure) = True

			else:
				is_wall(self.structure) = False


		def is_guardian():
			"""
			verification of the presence of the guardian
			"""
			if self.structure[self.case_x][self.case_y] == "g":
				is_guardian(self.structure) = True

			else:
				is_guardian(self.structure) = False



		end = False
		is_wall = False
		is_guardian = True


		if direction == 'right':
			if is_wall(self.structure[self.case_y][self.case_x+1]):
				self.case_x += 1

		elif direction == 'left':
			if is_wall(self.structure[self.case_y][self.case_x-1]):
				self.case_x -= 1

		elif direction == 'up':
			if is_wall(self.structure[self.case_y-1][self.case_x]):
				self.case_y -= 1

		elif direction == 'down':
			if is_wall(self.structure[self.case_y+1][self.case_x]):
				self.case_y += 1

		if is_guardian(self.structure[self.case_x][self.case_y]):
			end = True

	return end
	


def main():
	"""
	loop of the game : Mc Gyver is moving to the exit
	"""

	Mc_gyver = Mc_gyver(structure)

	end = False

	while not end:
		#to be replaced by "for event in pygame.event.get()" when importing pygame
		response = input("Where do you want to go? left, right, up, down ? Or quit ?")

		if response in ["left", "right", "up", "down", "quit"]:
			end = Mc_gyver.move(response)

		# up to date of the maze when pygame imported:
		# pygame.display.flip()
		# otherwise :
		maze.display()

	if is_guardian(self.structure[self.case_x][self.case_y]):
		print("You win !")
		#add an automatic function "exit window"



main()