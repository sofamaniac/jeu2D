"""Fichier contenant l'editeur de level du jeu kidnap the princess

- NE SERA PEUT-ETRE PAS INCLUS DANS LA VERSION FINALE

"""
# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2015, Antoine Grimod'
__license__ = 'GPL'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'

import pickle
import pygame
import graphics

from globals import *
from pygame.locals import *

pygame.init()

from objects import Niveau


def create_tab():
	new_tab = []

	for x in range(taille_tab[0]):

		new_tab.append([])

		for y in range(taille_tab[1]):
			new_tab[x].append(None)

	return new_tab


def update(current_tab, curseur_pos, curseur, background):
	fenetre.fenetre.blit(background, (0, 0))

	for x in range(taille_tab[0]):

		for y in range(taille_tab[1]):

			if current_tab[x][y]:
				fenetre.fenetre.blit(current_tab[x][y], (x * taille_case, y * taille_case))

	fenetre.fenetre.blit(curseur, (curseur_pos[2] * taille_case, curseur_pos[3] * taille_case))

	pygame.display.flip()


def enregistrer(niveau, path):
	with open(path, "rb") as fichier:

		pickler = pickle.Pickler(fichier)
		pickler.dump(niveau)


fenetre = graphics.Fenetre("editeur de niveau", None)

continuer = True
dico_image = {K_BACKSPACE: None,
			  K_1: graphics.load_image("img/blocs/grass.png"),
			  K_2: graphics.load_image("img/blocs/dirt.png"),
			  K_3: graphics.load_image("img/blocs/stone.png")}  # todo : creer le dico contenant les alias de toute les images

# chaque niveau contient une liste pour chaque ligne de tableau
#qui contient une liste pour chaque tableau qui contient 2 listes afin de pouvoir definir les briques
level = Niveau()
level.dico_tab = [[create_tab()]]


current_pos = [0, 0, 0, 0]  # 2 premiers : pos_y, pos_x du tableau dans le niveau
# 2 suivants : pos_y, pos_x dans le tableau en question


curseur = graphics.load_image("img/entity/curseur.png")
background = graphics.load_image("img/background/background_2.png")

pygame.key.set_repeat(75, 100)

while continuer:

	pygame.time.Clock().tick(60)

	for event in pygame.event.get():

		if event.type == QUIT:
			continuer = False

		if event.type == KEYDOWN:
			#Si la touche correspond a une image on la met dans level
			if event.key in dico_image.keys():
				level.dico_tab[current_pos[0]][current_pos[1]][current_pos[2]][current_pos[3]] = dico_image[event.key]

			if event.key == K_UP:

				if current_pos[3] - 1 < 0:
					level.dico_tab[current_pos[0]].insert(0, create_tab())  # on ajoute un nouveau tableau au debut de la ligne
					current_pos[3] = 0

				else:
					current_pos[3] -= 1

			elif event.key == K_DOWN:

				if current_pos[3] + 1 == taille_tab[1]:
					level.dico_tab[0].append(create_tab())  # on ajoute un nouveau tableau a la fin de la liste
					current_pos[3] = 0
					current_pos[1] += 1

				else:
					current_pos[3] += 1

			elif event.key == K_RIGHT:

				if current_pos[2] + 1 == taille_tab[0]:  # on change de tableau si au bord
					level.dico_tab.append([create_tab()])  # on ajoute une nouvelle ligne de tableau
					current_pos[2] = 0
					current_pos[0] += 1

				else:
					current_pos[2] += 1

			elif event.key == K_LEFT:
				# on change de tableau si au bord mais pas a la limite de la map
				if current_pos[2] == 0 and not current_pos[0] == 0:
					current_pos[0] -= 1

				elif current_pos[2] != 0:  # evite de sortir de l'ecran
					current_pos[2] -= 1

			elif event.key == K_ESCAPE:
				print("1. Enregistrer le fichier")
				print("2. Annuler")

				choix = int(input("Votre choix ?"))

				if choix == 1:
					name = "level/" + input("Nom du niveau ? ")

					level.background = background
					enregistrer(level, name)  # transforme level en obejt niveau


	update(level.dico_tab[current_pos[0]][current_pos[1]], current_pos, curseur, background)