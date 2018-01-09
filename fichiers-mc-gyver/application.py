#!/usr/bin/env python3
# -*- coding: Utf-8 -*

# -tc- Documenter le module à l'aide d'une docstring de module

import sys
import pygame
from pygame.locals import *
import maze
import mcgyver
import item
import config



class Application:
    """
    a class launching the game when opening labyrinth.py
    """

    def __init__(self, window=None, icon=None, m=None):
        # -tc- Tu peux utiliser une docstring pour documenter cette méthode
        #initializing application class

        pygame.init()

        #playing theme song looping for ever
        # -tc- pour mes tests: pygame.mixer.music.load('MacGyver_theme_song.mp3')
        # -tc- pour mes tests: pygame.mixer.music.play(-1, 0.0)

        #creating the window
        self.window = pygame.display.set_mode((600, 600), RESIZABLE)
        self.icon = pygame.image.load(config.small_icon)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Mc Gyver's Maze")

        #creating instances from the different classes
        self.maze = maze.Maze()
        self.mc_gyver = mcgyver.McGyver(self.maze)
        
        #creating syringe
        self.syringe = item.Syringe(self.maze, 'TNE')
        self.syringe.list_free_sprites()
        self.syringe.choose_free_sprites()

    def startgame(self):
        # -tc- Documenter cette méthode à l'aide d'une docstring
        #game loop
        while not self.mc_gyver.endgame(self.window):

            pygame.time.Clock().tick(30)
            # a key has been pressed
            pygame.event.pump()


            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    # -tc- sys.quit() n'existe pas
                    sys.exit()

                elif event.type == KEYDOWN:

                    #possibility of closing the window
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        # -tc- sys.quit() n'existe pas
                        sys.exit()

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
                self.maze.display(self.window)
                pygame.display.flip()
                self.maze.show()
    


# test
def main():
    app = Application()

if __name__ == "__main__":
    main()
