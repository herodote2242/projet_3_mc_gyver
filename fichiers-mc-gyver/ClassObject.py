#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from random import randrange
# -tc- import juste ce qui est nécessaire
# import labyrinthe
# import decor
# import structure_modifiable

# -tc- importer ClassMcGyver et ClassObject sont nécessaires pour ton code
# -tc- de test en fin de module
import ClassMcGyver as mac
import ClassObject as obj
import ClassMaze as maze


WALL = '#'


class Object:
	"""
	creation of the class Objects, allowing random creation on the maze
	"""

	# -tc- D'où viennent les case_x et case_y pour initcleaialiser self.case_x et self.case_y ?
	# -tc- Je rajoute des arguments avec des valeurs par défaut pour éviter les
	#-tc- les erreurs.
	def __init__(self, structure, display, case_x=0, case_y=0):
		"""
		initializing the objects representation
		"""
		self.display = display
		self.structure = structure
		self.case_x = case_x
		self.case_y = case_y

# -tc- Placer tout le code executable en dessous de cette condition, comme vu dans les cours
# -tc- permettra de t'éviter bien des problèmes. C'est notamment ça qui génére pas mal
# -tc- d'erreurs dans ton code actuel
if __name__ == "__main__":
	# -tc- Ne pas oublier de prefixer chaque classe avec le nom de module qui la pré-définit
	maze = maze.Maze()
	needle = obj.Object('N', maze)
	tube = obj.Object('T', maze)
	ether = obj.Object('E', maze)
	Mc_gyver = mac.McGyver('m', maze)
	Guardian = obj.Object('g', maze)
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
