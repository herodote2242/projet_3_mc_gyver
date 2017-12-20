#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import ClassObject as obj
import ClassMaze as maze
import decor

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


    def endgame():
        #condition of victory or defeat
        if self.structure[self.case_x][self.case_y] == [13][14]:
            #victory
            if self.object_number == 3:
                #guardian turns into a blood splatter
                self.structure[14][14] == "l"
                #Mc Gyver reaches the exit
                if self.structure[self.case_x][self.case_y] == [15][14]:
                    game_continue = False

            #defeat
            elif self.object_number != 3:
                #Mc Gyver turns into a blood splatter
                self.structure[self.case_x][self.case_y] = "l"
                game_continue = False

#test
def main():
    structure = maze.Maze()
    mac = McGyver(structure)

if __name__ == "__main__":
    main()