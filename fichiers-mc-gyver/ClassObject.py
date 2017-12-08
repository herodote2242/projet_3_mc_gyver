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


if __name__ == "__main__":
    # -tc- Comme pas d'importation de ClassObject, pas besoin de préfixer par obj.les
    # -tc- appels à la classe Object
	maze = maze.Maze()
	needle = Object('N', maze)
	tube = Object('T', maze)
	ether = Object('E', maze)
	Mc_gyver = mac.McGyver('m', maze)
	Guardian = Object('g', maze)
	syringe = [needle, ether, tube]

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

#test
def main():
	obj = Object()

if __name__ == "__main__":
	main()
