#!/usr/bin/env python3
# -*- coding: Utf-8 -*

"""This module is about the definition of the Mc Gyver's class, how he moves,
how he picks up the objects and how he faces the guardian at the end."""

import pygame
from pygame.locals import *
import sys
import syringe
import maze
import application
import config


class McGyver:
    """Creation of the class McGyver, allowing to define his position
    and its movement method."""

    def __init__(self, maze, display='m'):
        """Defining the Mac Gyver's position and number of objects
        picked up at the beginning."""
        self.display = display
        self.structure = maze.structure
        self.maze = maze
        self.case_x = 1
        self.case_y = 1
        self.object_number = 0
        self.end_position = self.get_end_position()

    def get_end_position(self):
        """Searches the end position in the labyrinth."""
        for i, line in enumerate(self.structure):
            for j, col in enumerate(line):
                if self.structure[i][j] == 'e':
                    return i, j

    def move(self, direction):
        """Defining the different moves, counting if an object is picked up and
        updating the sprites after a move."""
        WALL = '#'

        # Defining the different moves.
        if direction == 'right':
            if self.case_y < 14:
                if self.structure[self.case_x][self.case_y+1] != WALL:
                    # Previous position turns back to a path.
                    self.structure[self.case_x][self.case_y] = ' '
                    self.case_y += 1
                    # Adding 1 to object_number if an object is picked up.
                    if self.structure[self.case_x][self.case_y]\
                            in ('T', 'N', 'E'):
                        self.object_number += 1
                    # New position turns into mc-gyver's icon.
                    self.structure[self.case_x][self.case_y] = self.display

        elif direction == 'left':
            if self.case_y > 0:
                if self.structure[self.case_x][self.case_y-1] != WALL:
                    # Previous position turns back to a path.
                    self.structure[self.case_x][self.case_y] = ' '
                    self.case_y -= 1
                    # Adding 1 to object_number if an object is picked up.
                    if self.structure[self.case_x][self.case_y]\
                            in ('T', 'N', 'E'):
                        self.object_number += 1
                    # New position turns into mc-gyver's icon.
                    self.structure[self.case_x][self.case_y] = self.display

        elif direction == 'up':
            if self.case_x > 0:
                if self.structure[self.case_x-1][self.case_y] != WALL:
                    # Previous position turns back to a path.
                    self.structure[self.case_x][self.case_y] = ' '
                    self.case_x -= 1
                    # Adding 1 to object_number if an object is picked up.
                    if self.structure[self.case_x][self.case_y]\
                            in ('T', 'N', 'E'):
                        self.object_number += 1
                    # New position turns into mc-gyver's icon.
                    self.structure[self.case_x][self.case_y] = self.display

        elif direction == 'down':
            if self.case_x < 14:
                if self.structure[self.case_x+1][self.case_y] != WALL:
                    # Previous position turns back to a path.
                    self.structure[self.case_x][self.case_y] = ' '
                    self.case_x += 1
                    # Adding 1 to object_number if an object is picked up.
                    if self.structure[self.case_x][self.case_y]\
                            in ('T', 'N', 'E'):
                        self.object_number += 1
                    # New position turns into mc-gyver's icon.
                    self.structure[self.case_x][self.case_y] = self.display

    def endgame(self, window):
        """Activating the end according victory or defeat."""
        if (self.case_x, self.case_y) == self.end_position:
            # Victory.
            if self.object_number == len(config.syringe_elements):
                # Guardian turns into a blood splatter.
                self.maze.guardian = pygame.image.load(config.image_youlose)\
                    .convert_alpha()
                self.maze.display(window)
                # Informing the player of the success.
                victory = pygame.image.load(config.image_gamewon).convert()
                window.blit(victory, (150, 200))
                pygame.display.flip()

            # Defeat.
            else:
                # Mc Gyver turns into a blood splatter.
                self.maze.macgyver = pygame.image.load(config.image_youlose)\
                    .convert_alpha()
                self.maze.display(window)
                # Too bad for the player, he lost.
                defeat = pygame.image.load(config.image_gameover).convert()
                window.blit(defeat, (150, 200))
                pygame.display.flip()

            for event in pygame.event.get():
                # Press any key to close.
                if event.type == KEYDOWN:
                    pygame.quit()
                    sys.exit()


# Test
def main():
    structure = maze.Maze()
    mac = McGyver(structure)


if __name__ == "__main__":
    main()
