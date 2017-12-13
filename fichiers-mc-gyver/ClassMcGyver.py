#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import ClassObject as obj
import ClassMaze as maze
import decor

class McGyver(obj.Object):
	"""
	creation of the class McGyver, allowing to define his position and its movement method
	"""

	def __init__(self, maze):
		# Mac Gyver's position
		super().__init__(maze, 'm')
		self.case_x = 1
		self.case_y = 1
		self.object_number = 0


	def increment_object_number():
		# function to count the number of picked up objects
		self.object_number += 1
		# to be improved with the condition of walking on the sprite and fading it


	def move(self, direction):

		WALL = '#'

		# defining the different moves
		if direction == 'right':
			if self.structure[self.case_x][self.case_y+1] != WALL:
				#previous position turns back to a path
				self.structure[self.case_x][self.case_y] = ' '
				self.case_y += 1
				#new position turns into mc-gyver's icon
				self.structure[self.case_x][self.case_y] = self.display

		elif direction == 'left':
			if self.structure[self.case_x][self.case_y-1] != WALL:
				#previous position turns back to a path
				self.structure[self.case_x][self.case_y] = ' '
				self.case_y -= 1
				#new position turns into mc-gyver's icon
				self.structure[self.case_x][self.case_y] = self.display


		elif direction == 'up':
			if self.structure[self.case_x-1][self.case_y] != WALL:
				#previous position turns back to a path
				self.structure[self.case_x][self.case_y] = ' '
				self.case_x -= 1
				#new position turns into mc-gyver's icon
				self.structure[self.case_x][self.case_y] = self.display


		elif direction == 'down':
			if self.structure[self.case_x+1][self.case_y] != WALL:
				#previous position turns back to a path
				self.structure[self.case_x][self.case_y] = ' '
				self.case_x += 1
				#new position turns into mc-gyver's icon
				self.structure[self.case_x][self.case_y] = self.display


		# verification of the presence of the guardian
		if self.structure[self.case_x][self.case_y] == "g":
			return True
		else:
			return False

#test
def main():
	structure = maze.Maze()
	mac = McGyver(structure)

if __name__ == "__main__":
	main()