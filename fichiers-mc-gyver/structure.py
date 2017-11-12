#!/usr/bin/python3
# -*- coding: Utf-8 -*

from objets import *
from mc_gyver import *
from gardien import *
from structure_modifiable import Structure
import json
import pygame


class Maze:
"""
a rectangular maze made of 15 sprites width and 15 sprites height
"""

	def __init__(self, data):
		#initialisation of the window maze
		self.data = data
		self.structure = 0
		pass


	def generate_maze():
	    # sprites are displayed according to blanks or # in structure_modifiable.py
	    with open('structure_modifiable.json', 'r') as f:
	      data = json.load(f)

	    for line in data:
	      print("".join(line))


generate_maze()



if __name__ == "__main__":
	main()
