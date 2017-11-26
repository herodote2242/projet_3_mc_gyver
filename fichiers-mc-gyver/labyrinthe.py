#!/usr/bin/python3
# -*- coding: Utf-8 -*

import json
import pygame
# -tc- Il est recommandé d'éviter le import *
from decor import *
from classes import *

pygame.init()

# creating instances from the differents classes
maze = Maze()

# -tc- le constructeur de la classe Mc_gyver() prend la structure
# -tc- du labyrinthe en argument
mc_gyver = Mc_gyver()

needle = Object('N')
tube = Object('T')
ether = Object('E')
# -tc- du coup, je ne comprends pas trop à quoi sert ce Mc_gyver de
# -tc- type Object
Mc_gyver = Object('m')
Guardian = Object('g')

application = Application()


"""
to be added : playing theme song
"""

maze.display()
application.startgame()
mc_gyver.move()

#launching the game loop
end = False

while not end:
	startgame()
	move()

