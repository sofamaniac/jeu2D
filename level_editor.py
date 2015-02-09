"""Fichier contenant l'editeur de level du jeu kidnap the princess"""
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

pygame.init()

import graphics
from pygame.locals import *


class Niveau:

	def __init__(self, path):

		#contient le numero du level et son world (si j'en fais :D)
		self.num_level = 0

		#caracteristique du level
		self.background = 0
		self.music = 0

		#contient les ids et les images correspondantes
		self.dico_images = 0

		#contient les differents tableau et leur position dans le niveau
		self.dico_tab = 0

		#cotnient les ennemies par tableau et leur position dans ce dernier
		#ils seront inclut plus tard dans dico tab
		self.dico_ennemies = 0

		self.current_tab = [0, 0]  # contient la key du tableau courant

		self.charger(path)

	def charger(self, file_path):

		level_recup = ""

		with open(file_path, 'rb') as level:

			depickler = pickle.Unpickler(level)
			level_recup = depickler.load()

		self.num_level = level_recup.num_level

		self.background = level_recup.background
		self.music = level_recup.music

		self.dico_images = level_recup.dico_images

		self.dico_tab = level_recup.dico_tab


continuer = True
dico_image = {}  # todo : creer le dico contenant les alias de toute les images
taille_tab = [150, 75]

#chaque niveau contient une liste pour chaque ligne de tableau
#qui contient une liste pour chaque tableau qui contient 2 listes afin de pouvoir definir les briques
level = []
current_pos = [0, 0, 0, 0]  # ligne, tab, x, y
while continuer:

	for event in pygame.event.get():

		if event.type == QUIT:

			continuer = False

		if event.type == KEYDOWN:

			if event.key in dico_image.keys():

				level[current_pos] = dico_image[event.key]

			if event.key == K_UP:
				if current_pos[3] - 1 < 0:
					level.insert(0, [[[], []]])  # on ajoute une nouvelle ligne de tableau au debut du level
				else:
					current_pos[3] -= 1

			elif event.key == K_DOWN:
				if current_pos[3] + 1 > taille_tab[1]:
					level.append([[[], []]])  # on ajoute une nouvelle ligne de tableau a la fin de la liste

				else:
					current_pos[3] += 1

			elif event.key == K_RIGHT:
				if current_pos[2] + 1 > taille_tab[0]:
					level[current_pos[0]][current_pos[1]].append([])
				else:
					current_pos[2] += 1

			elif event.key == K_LEFT:
				if not current_pos[3] - 1 < 0 and not current_pos[2] == 0:
					current_pos[2] -= 1

#todo : avant d'enregistrer supprimer les tableaux vides ou les ligne de tableaux vides,...