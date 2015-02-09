"""Fcichier contenant le code des entity du jeu kidnap the princess"""

# -*-coding:utf-8-*
import pygame

import globals

from threading import Thread

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2014, Antoine Grimod'
__license__ = 'Copyright'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'


class Entity:

	def __init__(self, sons, pv, pm, damage, dico_image, damage_spec, taille_case):

		#attributs concernant l'apparence du perso
		self.current_image = ""
		self.images = dico_image  # continedra 4 key cotnenant chaqune un dico pour chaque cote : attaque, spec, damage, saut toutes les images seront orientees vers la droite si possible
		self.position = [0, 0]  # position en case
		self.sons = sons

		#attributs servant a definir les caracteristiques du personnages
		self.vie_max = pv
		self.current_life = pv
		self.mana_max = pm
		self.current_mana = pm

		#attributs definnissant les attaques du personnages
		self.damage = damage
		self.damage_spec = damage_spec

		#permet de definir un thread pour l'animation
		self.animation = Animation([], None, self, None, self.amplitude_deplacement / len(self.images["deplacement"]["droite"]))
		self.deplacement = [0, 0]

		#definit un thread pur le saut
		self.saut = Saut(self, -4, self.amplitude_deplacement / len(self.images["deplacement"]["droite"]))

		#permet de connaitre la taille des cases
		self.amplitude_deplacement = taille_case  # equivaut a definir la taille des case, represente la distance parcourue en px lors de l'animation d'un deplacment

	def deplacement(self, direction):

		self.animation.images = self.images["deplacement"][direction]
		self.animation.fenetre = globals.fenetre
		self.deplacement = []

		#todo faire la gestion de la collision avec les murs

		if direction == "droite":
			self.deplacement = [1, 0]

		elif direction == "gauche":
			self.deplacement = [-1, 0]

		elif direction == "bas":
			self.deplacement = [0, 1]

		elif direction == "haut":
			self.deplacement = [0, -1]

		#gestion de la collision
		niveau = globals.niveau.current_tab
		pos = [self.position[0] + self.deplacement[0], self.position[1] + self.deplacement[1]]

		#verifie la presence de sol sous les pieds du joueur
		sol = False

		for keys in niveau.get_keys():
			if pos[1] == keys[1]:
				sol = True

		#fait tomber le joueur s'il n'y a pas de sol
		if not sol and self.saut.v_y > 0:
			self.saut.v_y = 0
			self.saut.run()  # on fait sauter le joueur avec une vitesse verticale, ce qui le fait tomber

		if pos not in niveau.get_keys():

			if direction == "haut":
				self.saut.run()
				return
			self.animation.deplacement = self.deplacement

			self.animation.run()

		return


class Animation(Thread):

	def __init__(self, list_image, deplacement, entity, fenetre, amplitude):

		Thread.__init__(self)
		self.images = list_image
		self.deplacement = deplacement
		self.entity = entity
		self.fenetre = fenetre
		self.amplitude = amplitude

	def run(self):

		for image in self.images:

			pygame.time.Clock.tick(10)  # si l'animation se fait sur 4 images elle prendra 0.4s

			self.entity.current_image = image
			self.entity.position[0] += self.deplacement[0] * self.amplitude
			self.entity.position[1] += self.deplacement[1] * self.amplitude

			self.fenetre.blit(self.entity.current_image, self.entity.position)

		if self.deplacement[1] > 0:
			self.entity.deplacement("bas", self.fenetre)


class Saut(Thread):

	def __init__(self, entity, v_saut, amplitude):

		Thread.__init__(self)
		self.entity = entity
		self.list_image = entity.images["deplacement"]["saut"]
		self.amplitude = amplitude
		self.v_saut = v_saut  # vitesse verticale
		self.v_y = self.v_saut  # vitesse horizonatle
		self.g = 1  # vitesse d'acceleration en px

	def run(self):

		self.entity.current_image = self.list_image

		niveau = globals.niveau.current_tab

		pos_murs = []  # liste contenant les pos y des sols plafonds et murs

		for key in niveau.get_keys():
			#pour obtenir les coords reelles des plafonds on multiplie par la taille des cases
			pos_murs.append(key[1]*globals.taille_case)

		#on creer une boucle infinie que l'on arrete manuellement
		while True:

			self.entity.position[0] += self.entity.deplacement[0]
			self.entity.position[1] += self.v_y

			self.v_y += self.g

			#on detecte la collision avec un plafond le reste des collisions se fait dans la methode deplacer du joueur
			if (self.entity.position[1] + self.v_y) % globals.taille_case == 0:
				if self.entity.position in pos_murs:
					#si l'on chute c'est le sol, sinon c'est le plafond
					if self.v_y > 0:
						break

					else:
						self.v_y = 0

		self.v_y = self.v_saut


class Plateforme:

	def __init__(self):
		#todo : creer les plateformes
		return