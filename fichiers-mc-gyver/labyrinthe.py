#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import json
import pygame
import decor
import classes

pygame.init()

# creating instances from the different classes
maze = Maze(structure)

mc_gyver = McGyver(structure)

application = Application()


#playing theme song looping for ever
sound = pygame.mixer.music.load('Mac_Gyver_theme_song.mp3')
pygame.mixer.music.play(-1, 0.0)


maze.display()
application.startgame()
mc_gyver.move()

#launching the game loop
end = False

while not end:
	startgame()
	move()