#! /usr/bin/env python
# coding=utf-8

class GameStats():
	def __init__(self, ai_setting):
		self.ai_setting = ai_setting
		self.game_active = False
		self.high_score = 0
		self.reset_stats()

	def reset_stats(self):
		# 剩余飞船个数
		self.ships_left = self.ai_setting.ship_limit
		self.score = 0
		# 玩家等级
		self.level = 1
