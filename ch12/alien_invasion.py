#! /usr/bin/env python
# coding=utf-8

import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group

def run_game():
	pygame.init()
	ai_setting = Settings()
	game_mode = (ai_setting.screen_width, ai_setting.screen_height)
	screen = pygame.display.set_mode(game_mode)
	pygame.display.set_caption('Alien Invasion')

	# 飞船来了
	ship = Ship(ai_setting, screen)

	# 我是子弹
	bullets = Group()

	while True:
		gf.check_events(ai_setting, screen, ship, bullets)
		ship.update()
		# gf.update_bullets(bullets)
		gf.upadte_screen(ai_setting, screen, ship, bullets)
	

run_game()