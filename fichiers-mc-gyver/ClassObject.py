#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from random import randrange


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

	import ClassMaze as maze
	import ClassObject as obj

	structure = maze.Maze()
	needle = obj.Object(structure, 'N')
	tube = obj.Object(structure, 'T')
	ether = obj.Object(structure, 'E')

	print('Needle:', needle.display)
	print('Tube:', tube.display)
	print('Ether', ether.display)
	


if __name__ == "__main__":
	main()