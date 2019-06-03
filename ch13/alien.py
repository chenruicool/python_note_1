#! /usr/bin/env python
# coding=utf-8

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, ai_setting, screen):
		super(Alien, self).__init__()
		self.ai_setting = ai_setting
		self.screen = screen

		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def update(self):
		fleet_direction = self.ai_setting.fleet_direction
		self.x += self.ai_setting.alien_speed_factor * fleet_direction
		self.rect.x = self.x

	def check_edge(self):
		screen_rect = self.screen.get_rect()
		if self.rect.left <= 0:
			return True
		elif self.rect.right >= screen_rect.right:
			return True

