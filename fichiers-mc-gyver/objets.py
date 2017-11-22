import random


needle = Object('N')
tube = Object('T')
ether = Object('E')
Mc_gyver = Object('m')
Guardian = Object('g')

Mc_gyver.case_x = 1
Mc_gyver.case_y = 1
Guardian.case_x = 14
Guardian.case_y = 14

class Object:

	def __init__(self, representation):
		self.representation = representation


maze = [needle, ether, tube]

for item in maze:

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
