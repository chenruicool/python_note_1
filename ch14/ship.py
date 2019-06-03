#! /usr/bin/env python
# coding=utf-8

import pygame


class Ship():
	def __init__(self, ai_setting, screen):
		self.ai_setting = ai_setting
		self.screen = screen
		
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 放置到屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# rect的centerx等属性只能存储整数值
		self.center = float(self.rect.centerx)

		# 移动标志
		self.moving_right = False
		self.moving_left = False

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right:
			self.center += self.ai_setting.ship_speed_factor
			self.center = min(self.center, self.screen_rect.right)
		
		if self.moving_left:
			self.center -= self.ai_setting.ship_speed_factor
			self.center = max(self.center, 0)

		self.rect.centerx = self.center

	def center_ship(self):
		self.center = self.screen_rect.centerx
		