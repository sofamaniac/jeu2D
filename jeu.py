"""Fichier contenant les mecaniques de jeu du jeu 2D kidnap the princess"""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2014, Antoine Grimod'
__license__ = 'Copyright'
__version__ = '0.1'
__maintainer__ = 'Antoine Grimod'
__email__ = 'vivalgrim@gmail.com'
__status__ = 'Production'

import pygame

import entity, graphics, globals

from pygame.locals import *
from sys import exit


def jeu():

	player = entity.Entity()  # todo : mettre args pour creation joueur

	jouer = True

	pygame.key.set_key_repeat(50, 30)  # todo : mettre la duree d'1 animation

	#premette d'eviter les conflits si l'on appuie sur plusieurs touche
	#necessite quand meme la creation d'un thread pour l' animation
	droite = False
	gauche = False

	while jouer and player.current_life != 0:

		pygame.time.Clock.tick(60)

		for event in pygame.event.get():

			if event.type == QUIT:

				exit(0)

			if event.type == KEYDOWN:

				if (event.key == K_RIGHT or droite) and not gauche:
					droite = True
					player.deplacement("droite")

				if (event.key == K_LEFT or gauche) and not droite:
					gauche = True
					player.deplacement("gauche")

				if event.key == K_UP:
					player.deplacement("haut")

				if event.key == K_DOWN:
					player.deplacement("bas")

		if player.position[0] > globals.taille_fenetre[0] - 50:

			player.animation.pause()
			player.saut.pause()
			#faire pareil avec le reste des ennemies

			graphics.scroll(globals.niveau.current_tab, globals.niveau.tab[1][0])#todo faire la gestion du tableau suivant