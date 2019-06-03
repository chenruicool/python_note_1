#! /usr/bin/env python
# coding=utf-8

import pygame.font
# from pygame.sprite import Group
# from ship import Ship


class Scoreboard():
	def __init__(self, ai_setting, screen, stats):
		self.ai_setting = ai_setting
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.stats = stats

		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		score_str = "score:" + str(self.stats.score)
		# round_score = (round(self.stats.score), -1)
		# score_str = "{:,}".format(round_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		# high_score_str = "{:,}".format(self.stats.high_score)
		high_score_str = "high score:" + str(self.stats.high_score)
		# high_score = (round(self.stats.high_score), -1)
		# high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_setting.bg_color)

		# 最高分
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top

	def prep_level(self):
		level_str = "lv:" + str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color, self.ai_setting.bg_color)

		# 玩家等级
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = 50

	def prep_ships(self):
		# self.ships = Group()
		ships_str = "left:" + str(self.stats.ships_left)
		self.ships_image = self.font.render(ships_str, True, self.text_color, self.ai_setting.bg_color)

		# 玩家飞船数
		self.ships_rect = self.ships_image.get_rect()
		self.ships_rect.right = self.screen_rect.right - 20
		self.ships_rect.top = 80

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.ships_image, self.ships_rect)



