"""Fichier contenant les fonctions necessaires a l'initialisation du jeu. Point d'entree du jeu"""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2014, Antoine Grimod'
__license__ = 'Copyright'
__version__ = '0.1'
__maintainer__ = 'Antoine Grimod'
__email__ = 'vivalgrim@gmail.com'
__status__ = 'Production'


import graphics

import os

import globals

#on creer la fenetre
fenetre = graphics.Fenetre("jeu2D", graphics.load_image("img/logo.png"), (400, 400))

#on charge toutes les images dont le jeu aura besoin
list_image = os.listdir("img")

#on creer un dictionnaire qui contiendra le nom de l'image plus l'image chargee
globals.dico_images = {}

for path in list_image:
	globals.dico_images[path[:-4]] = graphics.load_image("img/" + path)  # on retire l'extansion de la clef dans le dictionnaire

list_music = os.listdir("music")
dico_music = {}

for path in list_music:
	globals.dico_images[path[:-4]] = graphics.load_music("music/" + path)

list_sound = os.listdir("sound")
globals.dico_sound = {}

for path in list_music:
	globals.dico_sound[path[:-4]] = graphics.load_sound("sound/" + path)

#Todo : lancer le menu principal