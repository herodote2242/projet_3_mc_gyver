#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import random
import pygame
import json
# -tc- Le fait de renommer ClassMaze en maze permet de respecter PEP8 et d'éviter de renommer comme
# -tc- ci-dessous
import ClassMaze as maze
# -tc- renommer éventuellement en config
import decor

# -tc- Il est proposé de renommer le présent fichier en item et de placer la classe Syringe dans un module Syringe

# -tc- Renommer Object en Item permettrait de créer un module item.py (object.py étant une mauvaise idée)
# -tc- On peut même aller plus loin dans le nettoyage. Retrospectivement, cette classe n'est vraiment utile
# -tc- qu'à la classe McGyver (Syringe était une collection d'éléments, et pas un objet unique). Du coup,
# -tc- on pourrait même l'éliminer et placer les attributs structure, case_x et case_y directement dans
# -tc- la classe McGyver
class Object:
    """
    creation of the class Objects, allowing objects'creation on the maze
    """

    def __init__(self, maze, display):
        #initializing the objects representation

        self.display = display
        self.structure = maze.structure
        self.case_x = 0
        self.case_y = 0

# -tc- Syringe représentant en fait trois objets, il ne fait pas vraiment de sens
# -tc- que Syringe hérite de Object.
class Syringe(Object):
    """
    creation of the class Syringe, composed of 3 elements randomly distributed on the maze
    """
    
    def __init__(self, maze, display):
        #initializing the syringe objects representation
        # -tc- si on n'hérite pas de Object, il faut juste faire:
        # -tc     self.maze = maze
        super().__init__(maze, display)
        # -tc- on pourrait passer direment une liste en paramètre de init (renommer display elements)
        # -tc- Cela nous donnerait: self.syringe = elements
        self.syringe = list(self.display)
    
    def list_free_sprites(self):
        # function listing all the free sprites on the maze
        self.free_sprites = []
        for line_number, line in enumerate(self.structure):
            for case_number, sprite in enumerate(line):
                if sprite == ' ':
                    self.free_sprites.append([line_number, case_number])

    
    def choose_free_sprites(self):
        #function randomly choosing a sprite for the syringe objects
        positions = random.sample(self.free_sprites, len(self.syringe))
        for position, item in zip(positions, self.syringe):
            line_number, case_number = position
            #position the item in self.structure
            self.structure[line_number][case_number] = item



#testing if class working correctly
def main():

    syringe = Syringe(Object)


if __name__ == "__main__":
    main()
