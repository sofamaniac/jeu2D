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

from threading import Thread
from math import fabs

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


def scroll(current_tab, next_tab, decalage=(2, 0)):

	liste = current_tab + next_tab  # on creer une liste qui contient toutes les images a afficher

	tours_de_boucle = 0

	if decalage[0] != 0:
		tours_de_boucle = current_tab[0][0].get_width() / fabs(decalage[0]) * globals.taille_tab

	elif decalage[1] != 0:
		tours_de_boucle = current_tab[0][0].get_hight() / fabs(decalage[1]) * globals.taille_tab

	for tour in range(tours_de_boucle):
		for image in len(liste[0]):
			liste[image]


class Button(Thread):
	def __init__(self, images, func_exe, pos):
		self.images = images
		self.current_image = images[0]
		self.func = func_exe
		self.pos = pos
		Thread.__init__(self)

	def run(self):

		while True:

			pygame.time.Clock.tick(60)
			pos_mouse = pygame.mouse.get_pos()

			if pos_mouse in self.current_image.get_rect():
				self.current_image = self.images[1]

				if pygame.mouse.get_pressed()[0]:
					self.current_image = self.images[2]
					self.func()
					self.current_image = self.images[0]