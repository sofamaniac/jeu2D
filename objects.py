"""Fcichier contenant le code des entity du jeu kidnap the princess"""

# -*-coding:utf-8-*


import pickle


__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2014, Antoine Grimod'
__license__ = 'Copyright'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'


class Niveau:
	def __init__(self, path=""):
		# contient le numero du level et son world (si j'en fais :D)
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


class Plateforme:

	def __init__(self):
		#todo : creer les plateformes bougeante ou non (il suffit de declarer un mouvement null)
		return