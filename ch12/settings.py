#! /usr/bin/env python
# coding=utf-8

class Settings():
	def __init__(self):
		# 屏幕信息
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# 飞船信息
		self.ship_speed_factor = 1.5

		# 子弹相关信息
		self.bullet_speed_factor = 10
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 3
