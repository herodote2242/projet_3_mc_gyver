#!/usr/bin/python3
# -*- coding: Utf-8 -*

# -tc- pour la première ligne du fichier, utilise plutôt
# -tc- #!/usr/bin/env python3 qui a l'avantage d'être plus portable

import structure
import gardien
# -tc- Attention, tu dois également faire un import decor

# -tc- Evite de mettre toutes les classes dans un même fichier

# -tc- Si on regarde ce qui se fait en nommage de classes, on 
# -tc- utilisera plus volontier MyGyver que Mc_Gyver.  
class Mc_gyver:
	# -tc- Ne met pas d'espace entre le nom de la classe et la docstring
	"""
	creation of the class Mc_Gyver, allowing to define his position and its movement method
	"""

	def __init__(self, structure):
		# -tc- Quelle est la différence entre (case_x, case_y) et (x, y)?
		# Mac Gyver's position
		self.case_x = 1
		self.case_y = 1
		self.x = 1
		self.y = 1
		self.structure = structure
		# -tc- On peut éventuellement ajouter une propriété self.object_number
		# -tc- et l'initialiser à zéro


	# -tc- On peut éventuellement utiliser un méthode increment_object_number()
	# -tc- qui va incrémenter self.object_number() à chaque appel
	def count_objects():
		pass
		#to be replaced by une function when objects implemented


	def move(self, direction):
		"""Mac Gyver's movements in the maze"""
		
		# -tc- Ta fonction interne is_wall() ne fait pas ce que tu veux
		# -tc- Crée plutôt des méthodes pour is_wall et is_guardian() plutôt
		# -tc- que des fonctions internes
		def is_wall():
			"""
			verification of the existence of a wall allowing or not the movement
			"""
			if self.structure[self.case_x][self.case_y] == "#":
				# -tc- c'est plutôt return True. Tu ne peux pas affecter une
				# -tc- valeur à une fonction de cette manière
				is_wall(self.structure) = True

			else:
				is_wall(self.structure) = False


		# -tc- Remarques similaire à is_wall()
		def is_guardian():
			"""
			verification of the presence of the guardian
			"""
			if self.structure[self.case_x][self.case_y] == "g":
				is_guardian(self.structure) = True

			else:
				is_guardian(self.structure) = False



		# -tc- ici, tu écrases tes fonctions ci-dessus en affectant à is_wall
		# -tc- et is_guardian de nouvelle valeurs
		end = False
		is_wall = False
		is_guardian = True


		# -tc- Systématiquement, les instructions ci-dessous te permettent de te
		# -tc- déplacer sur un mur.
		if direction == 'right':
			# -tc- Attention, is_wall a écrasée. Ce n'est plus une fonction. Par ailleurs,
			# -tc- comme défini plus haut, is_wall() ne prend pas de'argument
			if is_wall(self.structure[self.case_y][self.case_x+1]):
				# -tc- si je traduis tes intentions: SI mur à droite, aller à droite
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

	# -tc- Attention, return end est mal indenté
	return end
	




class Object:
	# -tc- N'oublie pas d'ajouter une documentation à chaque classe que tu crées

	def __init__(self, representation):
		# -tc- N'oublie pas d'ajouter une documentation éà chaque méthode
		self.representation = representation



# -tc- Ta n'as pas encore créé needle, ether et tube. Il te faut
# -tc- les créer explicitement: needle = Object('N'), par exemple.
objects = [needle, ether, tube]

for item in objects:

	# -tc- tes items n'on pas de propriété case_x ou case_y
	item.case_y = randrange(1, 14)
	item.case_x = randrange(1, 14)

	# -tc- Pour tester l'appartenance, tu peux utiliser l'opérateur in.
	# -tc- Par ailleurs, tes objets ne continent pas de propriété structure
	if needle.structure[needle.case_x][needle.case_y] == "#", "m", "g":
		needle.case_y = randrange(1, 14)
		needle.case_x = randrange(1, 14)
	
	if tube.structure[tube.case_x][tube.case_y] == "#", "N", "m", "g":
		tube.case_y = randrange(1, 14)
		tube.case_x = randrange(1, 14)

	if ether.structure[ether.case_x][ether.case_y] == "#", "N", "T", "m", "g":
		ether.case_y = randrange(1, 14)
		ether.case_x = randrange(1, 14)

	# -tc- les Object n'ont pour l'instance pas de méthode display()
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
		# -tc- Attention à importer decor au début du fichier et à ensuite
		# -tc- charger decor.image_wall ainsi que les autres images
		wall = pygame.image.load(image_wall).convert()
		path = pygame.image.load(image_path).convert()
		guardian = pygame.image.load(image_guardian).convert_alpha()
		macgyver = pygame.image.load(image_macgyver).convert_alpha()
		line_number = 0

		# -tc- Plus pythonique: for line_number, line in enumerate(self.structure):
		for line in self.structure:
			case_number = 0

			# -tc- Plus pytonique: for case_number, sprite in enumerate(line):
			for sprite in line:
				# -tc- importer decor et faire x = case_number * decor.sprite_dimension
				x = case_number * sprite_dimension
				y = line_number * sprite_dimension

				if sprite == '#':
					window.blit(wall, (x,y))

				elif sprite == ' ':
					window.blit(path, (x,y))

				elif sprite == 'g':
					window.blit(guardian, (x,y))
				# -tc- devient inutile si tu utilises enumerate()
				case_number += 1
			# -tc- devient inutile si tu utilises enumerate()
			line_number += 1




# -tc- attention: pas d'espace en le nom de la classe et le nom de la docstring
class Application:


	"""
	a class launching the game when opening labyrinth.py
	"""
	def __init__(self):

		self.window = pygame.display.set_mode((600, 600))
		# -tc- Attention: le nom de l'image doit être une chaine de caractères
		self.icone = pygame.image.load(img_macgyver.png)
		pygame.display.set_icon(icone)
		pygame.display.set_caption("Mc Gyver's Maze")
		# -tc- la classe Mc_gyver prend la structure en paramètre de son constructeur
		self.m = Mc_gyver("img_macgyver.png")


	def startgame(self):
		#game loop
		# -tc- Utiliser un nom de variable plus explicite, comme game_continue
		game = 1
		while game :

			pygame.time.clock().tick(30)

			for event in pygame.event.get():

				if event.type == QUIT:
					game = 0

				#possibility of closing the window
				elif event == KEYDOWN:

					# -tc- Donc espace te fait quitter le programme ?
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
