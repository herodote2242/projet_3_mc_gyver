#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from random import randrange
# -tc- effectivement, aucune nécessité d'importer ici. C'était une erreur
# import ClassObject as obj

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
		self.case_x = 0
		self.case_y = 0

# -tc- Code de test de la classe Object
def main():
	import ClassMaze as maze
	structure = maze.Maze()
	needle = Object(structure, 'N')
	tube = Object(structure, 'T')
	ether = Object(structure, 'E')

	print('Needle:', needle.display)
	print('Tube:', tube.display)
	print('Ether:', ether.display)

if __name__ == "__main__":
	main()

