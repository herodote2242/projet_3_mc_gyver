#!/usr/bin/python3
# -*- coding: Utf-8 -*

# -tc- 1) Il est préférable de mettre les import de la bibliothèque standard avant
# -tc- 2) Eviter les from module import *! Actuellement aucun de ces imports n'est nécessaire
from objets import *
from mc_gyver import *
from gardien import *
import json


class Maze:
	"""
	a rectangular maze made of 15 sprites width and 15 sprites height
	"""

    # -tc- parfait!
	def __init__(self):
        """ -tc- Tu peux documenter ta méthode dans une docstring"""
	    # sprites are displayed according to blanks or # in structure_modifiable.py
	    with open('structure_modifiable.json', 'r') as f:
	    	self.data = json.load(f)


	def display(self):
        """-tc- Tu peux documenter ta méthode dans un docstring"""
		for line in self.data:
			print("".join(line))



def main():
	maze = Maze()
	maze.display()


if __name__ == "__main__":
	main()
