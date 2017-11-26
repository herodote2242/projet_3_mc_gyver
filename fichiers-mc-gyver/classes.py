#!/usr/bin/python3
# -*- coding: Utf-8 -*

# -tc- pour la première ligne du fichier, utilise plutôt
# #!/usr/bin/env python3 qui a l'avantage d'être plus portable

import structure
import gardien

# -tc- Evite de mettre toutes les classes dans un même fichier

class Mc_gyver:
	# -tc- Ne met pas d'espace entre le nom de la classe et la docstring
	"""
	creation of the class Mc_Gyver, allowing to define his position and its movement method
	"""

	def __init__(self, structure):
		# Mac Gyver's position
		self.case_x = 1
		self.case_y = 1
		self.x = 1
		self.y = 1
		self.structure = structure


	def count_objects():
		pass
		#to be replaced by une function when objects implemented


	def move(self, direction):
		"""Mac Gyver's movements in the maze"""
		
		def is_wall():
			"""
			verification of the existence of a wall allowing or not the movement
			"""
			if self.structure[self.case_x][self.case_y] == "#":
				is_wall(self.structure) = True

			else:
				is_wall(self.structure) = False


		def is_guardian():
			"""
			verification of the presence of the guardian
			"""
			if self.structure[self.case_x][self.case_y] == "g":
				is_guardian(self.structure) = True

			else:
				is_guardian(self.structure) = False



		end = False
		is_wall = False
		is_guardian = True


		if direction == 'right':
			if is_wall(self.structure[self.case_y][self.case_x+1]):
				self.case_x += 1

		elif direction == 'left':
			if is_wall(self.structure[self.case_y][self.case_x-1]):
				self.case_x -= 1

		elif direction == 'up':
			if is_wall(self.structure[self.case_y-1][self.case_x]):
				self.case_y -= 1

		elif direction == 'down':
			if is_wall(self.structure[self.case_y+1][self.case_x]):
				self.case_y += 1

		if is_guardian(self.structure[self.case_x][self.case_y]):
			end = True

	return end
	




class Object:

	def __init__(self, representation):
		self.representation = representation


objects = [needle, ether, tube]

for item in objects:

	item.case_y = randrange(1, 14)
	item.case_x = randrange(1, 14)

	if needle.structure[needle.case_x][needle.case_y] == "#", "m", "g":
		needle.case_y = randrange(1, 14)
		needle.case_x = randrange(1, 14)
	
	if tube.structure[tube.case_x][tube.case_y] == "#", "N", "m", "g":
		tube.case_y = randrange(1, 14)
		tube.case_x = randrange(1, 14)

	if ether.structure[ether.case_x][ether.case_y] == "#", "N", "T", "m", "g":
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
		wall = pygame.image.load(image_wall).convert()
		path = pygame.image.load(image_path).convert()
		guardian = pygame.image.load(image_guardian).convert_alpha()
		macgyver = pygame.image.load(image_macgyver).convert_alpha()
		line_number = 0

		for line in self.structure:
			case_number = 0

			for sprite in line:
				x = case_number * sprite_dimension
				y = line_number * sprite_dimension

				if sprite == '#':
					window.blit(wall, (x,y))

				elif sprite == ' ':
					window.blit(path, (x,y))

				elif sprite == 'g':
					window.blit(guardian, (x,y))
				case_number += 1
			line_number += 1




class Application:


	"""
	a class launching the game when opening labyrinth.py
	"""
	def __init__(self):

		self.window = pygame.display.set_mode((600, 600))
		self.icone = pygame.image.load(img_macgyver.png)
		pygame.display.set_icon(icone)
		pygame.display.set_caption("Mc Gyver's Maze")
		self.m = Mc_gyver("img_macgyver.png")


	def startgame(self):
		#game loop
		game = 1
		while game :

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
			self.window.blit(fond (0,0))
			self.window.blit(Mc_gyver.move, (case_x, case_y))
			pygame.display.flip()
