#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from random import randrange

import labyrinthe
import decor
import structure_modifiable

WALL = '#'

class Object:
	"""
	creation of the class Objects, allowing random creation on the maze
	"""

	def __init__(self, display, structure):
		"""
		initializing the objects representation
		"""
		self.display = display
		self.structure = structure
		self.case_x = 0
		self.case_y = 0


class McGyver(Object):
	"""
	creation of the class McGyver, allowing to define his position and its movement method
	"""

	def __init__(self, display, structure):
		# Mac Gyver's position
		super().__init__(display, structure)
		self.case_x = 1
		self.case_y = 1
		self.object_number = 0


	def increment_object_number():
		"""
		function to count the number of picked up objects
		"""
		self.object_number += 1
		# to be improved with the condition of walking on the sprite and fading it

	# -tc- La fonction move a été retravaillée un peu pendant la session. Assure-toi
	# -tc- que tu comprends bien ce qu'on a fait et pose des questions dans le cas
	# -tc- contraire
	def move(self, direction):
		"""
		Mac Gyver's movements in the maze
		"""

		# defining the different movements
		if direction == 'right':
			if self.structure[self.case_y][self.case_x+1] != WALL:
				self.case_x += 1

		elif direction == 'left':
			if self.structure[self.case_y][self.case_x-1] != '#':
				self.case_x -= 1

		elif direction == 'up':
			if self.structure[self.case_y-1][self.case_x] != '#':
				self.case_y -= 1

		elif direction == 'down':
			if self.structure[self.case_y+1][self.case_x] != wall:
				self.case_y += 1

		# verification of the presence of the guardian
		if self.structure[self.case_x][self.case_y] == "g":
			return True
		else:
			return False

# -tc- Nous avons modifié certaines créations d'objets. Attention aux paramètres
# -tc- pris par le constructeur.
maze = Maze()
needle = Object('N', maze)
tube = Object('T', maze)
ether = Object('E', maze)
# -tc La classe Mc_gyver a été renommée en McGyver
mcgyver = McGyver('m', maze)
guardian = Object('g',maze)
objects = [needle, ether, tube]

# -tc- Revoir l'algorithme de positionnement aléatoire pour les objets, comme
# -tc- discuté à la session
for item in syringe:

	item.case_y = randrange(1, 14)
	item.case_x = randrange(1, 14)

	if needle.structure[needle.case_x][needle.case_y] in ["#", "m", "g"]:
		needle.case_y = randrange(1, 14)
		needle.case_x = randrange(1, 14)
	
	if tube.structure[tube.case_x][tube.case_y] in ["#", "N", "m", "g"]:
		tube.case_y = randrange(1, 14)
		tube.case_x = randrange(1, 14)

	if ether.structure[ether.case_x][ether.case_y] in ["#", "N", "T", "m", "g"]:
		ether.case_y = randrange(1, 14)
		ether.case_x = randrange(1, 14)

	item.display()




class Maze:
	"""
	a square maze made of 15 sprites width and 15 sprites height
	"""

	def __init__(self):
		"""
		sprites are displayed according to blanks or # in structure_modifiable.py
		"""
		with open('structure_modifiable.json', 'r') as f:
			self.data = json.load(f)


	def display(self, window):
		"""
		method allowing the construction of the graphic maze with images
		"""

		wall = deco.pygame.image.load(image_wall).convert()
		path = decor.pygame.image.load(image_path).convert()
		guardian = decor.pygame.image.load(image_guardian).convert_alpha()
		macgyver = decor.pygame.image.load(image_macgyver).convert_alpha()
		line_number = 0

		for line_number, line in enumerate(self.structure):
			case_number = 0

			for case_number, sprite in enumerate(line):
				x = case_number * decor.sprite_dimension
				y = line_number * decor.sprite_dimension

				if sprite == '#':
					window.blit(wall, (x,y))

				elif sprite == ' ':
					window.blit(path, (x,y))

				elif sprite == 'g':
					window.blit(guardian, (x,y))




class Application:
	"""
	a class launching the game when opening labyrinth.py
	"""

	def __init__(self):
		"""
		initializing application class
		"""
		self.window = pygame.display.set_mode((600, 600))
		self.icone = pygame.image.load("img_macgyver.png")
		pygame.display.set_icon(icone)
		pygame.display.set_caption("Mc Gyver's Maze")
		self.m = McGyver("img_macgyver.png", structure)


	def startgame(self):
		#game loop
		game_continue = 1
		while game_continue:

			pygame.time.clock().tick(30)

			for event in pygame.event.get():

				if event.type == QUIT:
					game = 0

				#possibility of closing the window
				elif event == KEYDOWN:

					if event.key == K_ESCAPE:
						game = 0

					#events of mc-gyver's moves
					elif event.key == K_RIGHT:
						Mc_gyver.move('right')

					elif event.key == K_LEFT:
						Mc_gyver.move('left')

					elif event.key == K_UP:
						Mc_gyver.move('up')

					elif event.key == K_DOWN:
						Mc_gyver.move('down')

			#refreshing the window
			self.window.blit(fond, (0,0))
			self.window.blit(McGyver.move(), (case_x, case_y))
			pygame.display.flip()
