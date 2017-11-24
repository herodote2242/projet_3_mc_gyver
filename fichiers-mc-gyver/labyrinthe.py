#!/usr/bin/python3
# -*- coding: Utf-8 -*

import json
import pygame
from decor import *
from classes import *

pygame.init()

# creating instances from the differents classes
maze = Maze()

mc_gyver = Mc_gyver()

needle = Object('N')
tube = Object('T')
ether = Object('E')
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

