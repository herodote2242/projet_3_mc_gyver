#!/usr/bin/python3
# -*- coding: Utf-8 -*

import random


needle = Object('N')
tube = Object('T')
ether = Object('E')
# -tc- A quoi te sert la classe Mc_gyver si tu créés Mc_gyver à partir de la classe 
# -tc- Object ?
Mc_gyver = Object('m')
Guardian = Object('g')

Mc_gyver.case_x = 1
Mc_gyver.case_y = 1
Guardian.case_x = 14
Guardian.case_y = 14


"""
defining the different element's of the window
"""

sprite_number = 15
sprite_dimension = 40
window_dimension = sprite_number * sprite_dimension
window_title = "Mac Gyver's Maze"
# -tc- le répertoire images/ n'existe pas pour le moment.
small_icon = "images/img_macgyver.png"
image_wall = "images/img_wall.png"
image_path = "images/img_path.png"
image_macgyver = "images/img_macgyver.png"
image_guardian = "images/img_guardian.png"
