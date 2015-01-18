"""Fichier se chargeant de l'aspect graphique du jeu kidnap the princess"""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2014, Antoine Grimod'
__license__ = 'Copyright'
__version__ = '0.1'
__maintainer__ = 'Antoine Grimod'
__email__ = 'vivalgrim@gmail.com'
__status__ = 'Production'


import pygame

import globals

pygame.init()


def load_image(path):

	image = ""
	try:
		image = pygame.image.load(path).convert_alpha()
	except NameError as erreur_ouverture:
		print("Impossible de charger l'image : ", erreur_ouverture)

	return image


def load_sound(path):

	son = ""
	try:
		son = pygame.mixer.Sound(path)

	except NameError as erreur_ouverture:
		print("Impossible de charger le son : ", erreur_ouverture)
	return son


def load_music(path):

	music = ""
	try:
		music = pygame.mixer.music.load(path)
	except NameError as erreur_ouverture:
		print("Impossible de charger l'image : ", erreur_ouverture)

	return music


class Fenetre:

	def __init__(self, titre, logo, taille=(400, 400)):

		self.fenetre = pygame.display.set_mode([taille[0], taille[1]])

		pygame.display.set_caption(titre)
		pygame.display.set_icon(logo)

	def update(self, elements, position):

		for picture in elements:

			for pos in position:

				self.fenetre.blit(picture, pos)

		pygame.display.flip()


def create_subsurface(surface, horizontale, vertice):

	width = surface.get_width() / horizontale
	height = surface.get_height / vertice

	list_images = []

	for x in range(horizontale):
		for y in range(vertice):
			list_images.append(surface.subsurface((width * x, height * y)))

	return list_images


def scroll(current_tab, next_tab):

	liste = current_tab + next_tab  # on creer une liste qui contient toutes les images a afficher

	decalage = 2

	tours_de_boucle = current_tab[0][0].get_width() / decalage * globals.taille_tab

	for image in range(tours_de_boucle):


