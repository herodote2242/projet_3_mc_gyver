#!/usr/bin/python3
# -*- coding: Utf-8 -*

from objets import *
from mc_gyver import *
from gardien import *
import json


class Maze:
	"""
	a rectangular maze made of 15 sprites width and 15 sprites height
	"""

	def __init__(self):
	    # sprites are displayed according to blanks or # in structure_modifiable.py
	    with open('structure_modifiable.json', 'r') as f:
	    	self.data = json.load(f)


	def display(self):
		for line in self.data:
			print("".join(line))



def main():
	maze = Maze()
	maze.display()


if __name__ == "__main__":
	main()
