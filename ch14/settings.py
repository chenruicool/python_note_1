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
		self.ship_limit = 1

		# 子弹相关信息
		self.bullet_speed_factor = 10
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 3

		# 外星人相关
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 100
		self.fleet_direction = 1
		self.speedup_scale = 1.1

		#记分数
		self.high_score = 0
		self.alien_points = 50
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 10
		self.fleet_direction = 1
		self.alien_speed_factor = 1

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale




