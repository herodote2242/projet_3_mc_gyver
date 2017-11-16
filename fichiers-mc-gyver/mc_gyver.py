#!/usr/bin/python3
# -*- coding: Utf-8 -*

# -tc- Eviter les from module import *
from structure import *
from gardien import *


class Mc_gyver:
    """ -tc- documenter ta classe dans une docstring. """
	
	def __init__(self, structure):
		self.case_x = 1
		self.case_y = 1
		self.structure = structure


    # -tc- note de style: plutot utiliser l'infinitif move() que moves()
	def moves(self, direction):
		"""movements of the main character in the maze"""

        # -tc- Il peux être avantageux de créer une méthode is_wall() dans 
        # -tc- ta structure plutôt que de manipuler la structure interne

        # -tc- initialiser end à False

		if direction == 'right':
			if self.structure[self.case_y][self.case_x+1] != '#':
				self.case_x += 1
        # -tc- elif
		if direction == 'left':
			if self.structure[self.case_y][self.case_x-1] != '#':
				self.case_x -= 1

        # -tc- elif
		if direction == 'up':
			if self.structure[self.case_y-1][self.case_x] != '#':
				self.case_y -= 1

        # -tc- elif
		if direction == 'down':
			if self.structure[self.case_y+1][self.case_x] != '#':
				self.case_y += 1
        # -tc- Mc_gyver.self.case_x ne veut rien dire. C'est simplement self.case_x et self.case_y
        # -tc- Tu ne peux pas tester comme ça
		if Mc_gyver.self.case_x, Mc_gyver.self.case_y = 14, 14:
			end = True

        # -tc- retourner end pour que le code appelant sache si c'est fini ou pas

def main():
	#loop of the game : Mc Gyver is moving until the exit

    # -tc- créer un objet mygyver

	end = False

	while not end:
		#to be replaced by "for event in pygame.event.get()" when importing pygame

        # -tc- peut-être afficher à l'utilisateur les réponses acceptées
		response = input("where do you want to go?")

        # -tc- tu peux ajouter la possibilité pour l'utilisateur d'entrer quit
		if response in ["left", "right", "up", "down"]:
            # -tc- Attention, tu n'as pas créé l'objet Mc_gyver. Tu ne peux donc pas
            #      appeler la méthode move()
            # -tc- On veut tester si c'est fini avec end = mcgyver.move(response)
			Mc_gyver.moves(response)

		# up to date of the maze when pygame imported:
		# pygame.display.flip()
		# otherwise :
		maze.display()

    # -tc- Comme plus haut, attention à ce test qui est faut
	if Mc_gyver.self.case_x, Mc-gyver.self.case_y = 14, 14:
		print("You win !")
		#add an automatic function "exit window"

# -tc- Cette fonction doit probablement être une méthode de ta classe
def count_objects():
	pass
	#to be replaced by une function when objects implemented

# -tc- Il faut encore exécuter main
