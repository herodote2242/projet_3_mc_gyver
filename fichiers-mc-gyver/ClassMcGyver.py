#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import ClassObject as obj
import ClassMaze as maze
import decor

# -tc- McGyver est la seule classe à hériter de Object, on peut se demander si il
# -tc- n'est pas préférable d'éliminer cette classe et d'introduire le attributs
# -tc- self.structure, self.display, self.case_x et self.case_y directement dans
# -tc- McGyver. 
# -tc- Si on décide de la garder, il serait mieux de renommer en Item et de la placer
# -tc- dans le module item.py (pour respecter les recommandations du PEP8)
class McGyver(obj.Object):
    """
    creation of the class McGyver, allowing to define his position and its movement method
    """

    def __init__(self, maze):
        # Mac Gyver's position
        super().__init__(maze, 'm')
        self.case_x = 1
        self.case_y = 1
        self.object_number = 0


    def increment_object_number():
        # function to count the number of picked up objects
        if [self.case_x][self.case_y] in ClassObject.positions:
            self.object_number += 1


    # -tc- Je pense qu'on peut facoriser le code de cette méthode, très répétitif
    def move(self, direction):

        WALL = '#'

        # defining the different moves
        if direction == 'right':
            if self.case_y < 14:
                if self.structure[self.case_x][self.case_y+1] != WALL:
                    #previous position turns back to a path
                    self.structure[self.case_x][self.case_y] = ' '
                    self.case_y += 1
                    #new position turns into mc-gyver's icon
                    self.structure[self.case_x][self.case_y] = self.display

        elif direction == 'left':
            if self.case_y > 0: 
                if self.structure[self.case_x][self.case_y-1] != WALL:
                    #previous position turns back to a path
                    self.structure[self.case_x][self.case_y] = ' '
                    self.case_y -= 1
                    #new position turns into mc-gyver's icon
                    self.structure[self.case_x][self.case_y] = self.display


        elif direction == 'up':
            if self.case_x > 0:
                if self.structure[self.case_x-1][self.case_y] != WALL:
                    #previous position turns back to a path
                    self.structure[self.case_x][self.case_y] = ' '
                    self.case_x -= 1
                    #new position turns into mc-gyver's icon
                    self.structure[self.case_x][self.case_y] = self.display


        elif direction == 'down':
            if self.case_x < 14:
                if self.structure[self.case_x+1][self.case_y] != WALL:
                    #previous position turns back to a path
                    self.structure[self.case_x][self.case_y] = ' '
                    self.case_x += 1
                    #new position turns into mc-gyver's icon
                    self.structure[self.case_x][self.case_y] = self.display


    def endgame(self):
        #condition of victory or defeat
        if self.structure[self.case_x][self.case_y] == [13][14]:
            #victory
            if self.object_number == 3:
                #guardian turns into a blood splatter
                maze.guardian = pygame.image.load(decor.image_youloose).convert_alpha()
                #Mc Gyver reaches the exit
                if self.structure[self.case_x][self.case_y] == [15][14]:
                    game_continue = False

            #defeat
            elif self.object_number != 3:
                #Mc Gyver turns into a blood splatter
                maze.mcgyver = pygame.image.load(decor.image_youloose).convert_alpha()
                game_continue = False

#test
def main():
    structure = maze.Maze()
    mac = McGyver(structure)

if __name__ == "__main__":
    main()
