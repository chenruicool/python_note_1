#! /usr/bin/env python
# coding=utf-8

import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
	pygame.init()
	ai_setting = Settings()
	game_mode = (ai_setting.screen_width, ai_setting.screen_height)
	screen = pygame.display.set_mode(game_mode)
	pygame.display.set_caption('Alien Invasion')

	# 统计
	stats = GameStats(ai_setting)

	# 飞船来了
	ship = Ship(ai_setting, screen)

	# 我是子弹
	bullets = Group()

	# 外星人
	aliens = Group()
	gf.create_fleet(ai_setting, screen, aliens)

	while True:
		if stats.game_active:
			gf.check_events(ai_setting, screen, ship, bullets)
			ship.update()
		
		gf.upadte_screen(ai_setting, stats, screen, ship, bullets, aliens)
	

run_game()