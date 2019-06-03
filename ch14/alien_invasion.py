#! /usr/bin/env python
# coding=utf-8

import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_setting = Settings()
	game_mode = (ai_setting.screen_width, ai_setting.screen_height)
	screen = pygame.display.set_mode(game_mode)
	pygame.display.set_caption('Alien Invasion')

	# 统计
	stats = GameStats(ai_setting)

	# 得分
	sb = Scoreboard(ai_setting, screen, stats)

	# 按钮
	play_button = Button(ai_setting, screen, 'play')

	# 飞船来了
	ship = Ship(ai_setting, screen)

	# 我是子弹
	bullets = Group()

	# 外星人
	aliens = Group()
	gf.create_fleet(ai_setting, screen, aliens)

	while True:
		gf.check_events(ai_setting, screen, stats, sb, play_button, ship, bullets, aliens)
		gf.upadte_screen(ai_setting, screen, stats, sb, ship, bullets, aliens, play_button)
	

run_game()