#!/usr/bin/env python3
# -*- coding: Utf-8 -*

"""
This module is responsible of the creation of the game, its loops,
and how it is supposed to react to the keyboard's events.
"""

import sys
import pygame
from pygame.locals import *
import maze
import mcgyver
import syringe
import config


class Application:
    """A class launching the game when opening labyrinth.py."""

    def __init__(self, window=None, icon=None, m=None):
        """Initializing application class."""

        pygame.init()

        # Playing theme song looping for ever.
        pygame.mixer.music.load('MacGyver_theme_song.mp3')
        pygame.mixer.music.play(-1, 0.0)

        # Creating the window.
        self.window = pygame.display.set_mode((600, 600), RESIZABLE)
        self.icon = pygame.image.load(config.small_icon)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Mc Gyver's Maze")

        # Creating instances from the different classes.
        self.maze = maze.Maze()
        self.mc_gyver = mcgyver.McGyver(self.maze)

        # Creating syringe.
        self.syringe = syringe.Syringe(self.maze)
        self.syringe.list_free_sprites()
        self.syringe.choose_free_sprites()

    def startgame(self):
        """Creating the game loop."""
        while not self.mc_gyver.endgame(self.window):

            pygame.time.Clock().tick(30)
            # A key has been pressed.
            pygame.event.pump()

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:

                    # Possibility of closing the window.
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    # Events of Mc Gyver's moves.
                    elif event.key == K_RIGHT:
                        self.mc_gyver.move('right')

                    elif event.key == K_LEFT:
                        self.mc_gyver.move('left')

                    elif event.key == K_UP:
                        self.mc_gyver.move('up')

                    elif event.key == K_DOWN:
                        self.mc_gyver.move('down')

                # Refreshing the window.
                self.maze.display(self.window)
                pygame.display.flip()


# Test.
def main():
    app = Application()


if __name__ == "__main__":
    main()
