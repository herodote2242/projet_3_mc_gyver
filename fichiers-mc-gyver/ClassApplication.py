#!/usr/bin/env python3
# -*- coding: Utf-8 -*


import sys
import pygame
from pygame.locals import *
# -tc- PEP8 recommande des noms de modules tout en minuscules.
# -tc- Je propose: application, maze, mcgyver, item (avec renommage de la classe Object en Item, car object
# -tc- est un mot réservé en python)
# -tc- Je propose également de mettre la classe Syringe dans un module syringe.py dédié.
import ClassMaze
import ClassMcGyver
import ClassObject
# -tc- je me demande si renommer le module decor en config ne serait pas opportun
import decor



class Application:
    """
    a class launching the game when opening labyrinth.py
    """

    def __init__(self, window=None, icon=None, m=None):
        #initializing application class

        pygame.init()
        #creating instances from the different classes
        # -tc- Avec la proposition de renommage de ClassMaze en maze, les 
        # -tc- lignes ci-dessous deviendraient:
        # -tc-     self.maze = maze.Maze()
        # -tc-     self.my_gyver = mcgyver.McGyver(self.maze)
        # -tc-     self.syringe = syringe.Syringe(self.maze, ['T', 'N', 'E'])
        self.maze = ClassMaze.Maze()
        self.mc_gyver = ClassMcGyver.McGyver(self.maze)
        
        #creating syringe
        self.syringe = ClassObject.Syringe(self.maze, 'TNE')
        self.syringe.list_free_sprites()
        self.syringe.choose_free_sprites()


        #playing theme song looping for ever
        pygame.mixer.music.load('MacGyver_theme_song.mp3')
        pygame.mixer.music.play(-1, 0.0)

        #creating the window
        self.window = pygame.display.set_mode((600, 600), RESIZABLE)
        self.icon = pygame.image.load(decor.small_icon)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Mc Gyver's Maze")


    def startgame(self):
        #game loop
        game_continue = True
        while game_continue:

            pygame.time.Clock().tick(30)
            # a key has been pressed
            pygame.event.pump()


            for event in pygame.event.get():

                if event.type == QUIT:
                    game_continue = False

                elif event.type == KEYDOWN:

                    #possibility of closing the window
                    if event.key == K_ESCAPE:
                        game_continue = False

                    #events of mc-gyver's moves
                    elif event.key == K_RIGHT:
                        self.mc_gyver.move('right')

                    elif event.key == K_LEFT:
                        self.mc_gyver.move('left')

                    elif event.key == K_UP:
                        self.mc_gyver.move('up')

                    elif event.key == K_DOWN:
                        self.mc_gyver.move('down')

            #refreshing the window
            if game_continue:
                self.maze.display(self.window)
                pygame.display.flip()

        ClassMcGyver.endgame()
        pygame.quit()


# test
def main():
    app = Application()

if __name__ == "__main__":
    main()
