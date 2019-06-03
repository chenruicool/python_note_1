#! /usr/bin/env python
# coding=utf-8

# 子弹模块

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ai_setting, screen, ship):
		# super().__init__(Bullet, self) # python 2.7
		super().__init__()
		self.screen = screen

		# 创建一个子弹
		self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)
		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor

	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

