#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
import item
import maze
import application
import config

class McGyver:
    """
    creation of the class McGyver, allowing to define his position and its movement method
    """

    def __init__(self, maze, display = 'm'):
        # Mac Gyver's position
        self.display = display
        self.structure = maze.structure
        self.maze = maze
        #super().__init__(maze, 'm')
        self.case_x = 1
        self.case_y = 1
        #self.object_number = 0


    def increment_object_number(self):
        # function to count the number of picked up objects
        if [self.case_x][self.case_y] in item.positions:
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


    def endgame(self):
        #condition of victory or defeat
        if (self.case_x, self.case_y) == "e":
            #victory
            if self.object_number == 3:
                #guardian turns into a blood splatter
                self.maze.guardian = pygame.image.load(config.image_youloose).convert_alpha()
                #informing the player of the success, and if he wants to play again
                victory = pygame.image.load(config.img_gamewon).convert()
                window.blit(victory, (150,200))
                for event in pygame.event.get():

                    if event.type == QUIT:
                        pygame.quit()

                    elif event.type == KEYDOWN:

                        #possibility of closing the window
                        if event.key == K_ESCAPE:
                            pygame.quit()

                        #or playing again
                        elif event.key == K_ENTER:
                            application.Application()

            #defeat
            else:
                #Mc Gyver turns into a blood splatter
                self.maze.mcgyver = pygame.image.load(config.image_youloose).convert_alpha()
                #too bad for the player, he lost but can try again
                defeat = pygame.image.load(config.img_gameover).convert()
                window.blit(defeat, (150, 200))
                for event in pygame.event.get():

                    if event.type == QUIT:
                        pygame.quit()

                    elif event.type == KEYDOWN:

                        #possibility of closing the window
                        if event.key == K_ESCAPE:
                            pygame.quit()

                        #or playing again
                        elif event.key == K_ENTER:
                            application.Application()
#test
def main():
    structure = maze.Maze()
    mac = McGyver(structure)

if __name__ == "__main__":
    main()