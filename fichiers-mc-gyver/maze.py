#!/usr/bin/env python3
# -*- coding: Utf-8 -*

"""This module is about the graphic construction of the maze,
according to the file structure_modifiable.json."""

import json
import pygame
import config


class Maze:
    """A square maze made of 15 sprites width and 15 sprites height."""

    def __init__(self):
        """Sprites are displayed according to blanks, e, g, m, or # in
        structure_modifiable.json."""

        self.wall = pygame.image.load(config.image_wall).convert()
        self.path = pygame.image.load(config.image_path).convert()
        self.guardian = pygame.image.load(config.image_guardian)\
            .convert_alpha()
        self.macgyver = pygame.image.load(config.image_macgyver)\
            .convert_alpha()
        self.exit = pygame.image.load(config.image_exit).convert_alpha()
        self.tube = pygame.image.load(config.image_tube).convert_alpha()
        self.ether = pygame.image.load(config.image_ether).convert_alpha()
        self.needle = pygame.image.load(config.image_needle).convert_alpha()

        with open('structure_modifiable.json', 'r') as f:
            self.structure = json.load(f)

    def display(self, window):
        """Method allowing the construction of the graphic maze with images."""
        for line_number, line in enumerate(self.structure):

            for case_number, sprite in enumerate(line):
                x = case_number * config.sprite_dimension
                y = line_number * config.sprite_dimension

                if sprite == '#':
                    window.blit(self.wall, (x, y))

                elif sprite == ' ':
                    window.blit(self.path, (x, y))

                elif sprite == 'g':
                    window.blit(self.path, (x, y))
                    window.blit(self.guardian, (x, y))

                elif sprite == "m":
                    window.blit(self.path, (x, y))
                    window.blit(self.macgyver, (x, y))

                elif sprite == "T":
                    window.blit(self.path, (x, y))
                    window.blit(self.tube, (x, y))

                elif sprite == "N":
                    window.blit(self.path, (x, y))
                    window.blit(self.needle, (x, y))

                elif sprite == "E":
                    window.blit(self.path, (x, y))
                    window.blit(self.ether, (x, y))

                elif sprite == "e":
                    window.blit(self.path, (x, y))
                    window.blit(self.exit, (x, y))

                # Image of defeated character.
                elif sprite == "l":
                    window.blit(self.path, (x, y))
                    window.blit(self.image_youlose, (x, y))

def is_wall():
    if sprite == "#":
        return True
# Test.
def main():
    pygame.init()
    window = pygame.display.set_mode((600, 600))
    # Playing theme song looping for ever.
    pygame.mixer.music.load('MacGyver_theme_song.mp3')
    pygame.mixer.music.play(-1, 0.0)
    maze = Maze()
    maze.display(window)
    pygame.display.flip()
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
    pygame.quit()


if __name__ == "__main__":
    main()
