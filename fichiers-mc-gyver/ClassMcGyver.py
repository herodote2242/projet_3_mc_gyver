#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import ClassObject as obj

class McGyver(obj.Object):
	"""
	creation of the class McGyver, allowing to define his position and its movement method
	"""

	def __init__(self, display, structure):
		# Mac Gyver's position
		super().__init__(display, structure)
		self.case_x = 1
		self.case_y = 1
		self.object_number = 0


	def increment_object_number():
		# function to count the number of picked up objects
		self.object_number += 1
		# to be improved with the condition of walking on the sprite and fading it


	def move(self, direction):
		# defining the different movements
		if direction == 'right':
			if self.structure[self.case_y][self.case_x+1] != WALL:
				self.case_x += 1

		elif direction == 'left':
			if self.structure[self.case_y][self.case_x-1] != WALL:
				self.case_x -= 1

		elif direction == 'up':
			if self.structure[self.case_y-1][self.case_x] != WALL:
				self.case_y -= 1

		elif direction == 'down':
			if self.structure[self.case_y+1][self.case_x] != WALL:
				self.case_y += 1

		# verification of the presence of the guardian
		if self.structure[self.case_x][self.case_y] == "g":
			return True
		else:
			return False

#test
def main():
	mac = McGyver()

if __name__ == "__main__":
	main()