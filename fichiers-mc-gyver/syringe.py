#!/usr/bin/env python3
# -*- coding: Utf-8 -*

"""This module deals with the construction of the 3 objects of the syringe,
and the way they are randomly distributed at the maze's construction."""

import random
import pygame
import json
import maze
import config


class Syringe:
    """Creation of the class Syringe, composed of 3 elements randomly
    distributed on the maze."""

    def __init__(self, maze):
        """Initializing the syringe objects representation."""
        self.structure = maze.structure
        self.syringe = config.items

    def list_free_sprites(self):
        """A function listing all the free sprites on the maze."""
        self.free_sprites = []
        for line_number, line in enumerate(self.structure):
            for case_number, sprite in enumerate(line):
                if sprite == ' ':
                    self.free_sprites.append([line_number, case_number])

    def choose_free_sprites(self):
        """A function randomly choosing a sprite for the syringe objects."""
        positions = random.sample(self.free_sprites, len(self.syringe))
        for position, item in zip(positions, self.syringe):
            line_number, case_number = position
            # Position the item in self.structure.
            self.structure[line_number][case_number] = item


# Test.
def main():

    syringe = Syringe(Object)


if __name__ == "__main__":
    main()
