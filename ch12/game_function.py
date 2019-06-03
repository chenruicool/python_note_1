#! /usr/bin/env python
# coding=utf-8

import sys
import pygame
from bullet import Bullet

def fire_bullet(ai_setting, screen, ship, bullets):
	if len(bullets) < ai_setting.bullet_allowed:
		new_bullet = Bullet(ai_setting, screen, ship)
		bullets.add(new_bullet)

# 按下
def check_keydown_events(event, ai_setting, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_setting, screen, ship, bullets)
# 放开
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False	

def check_events(ai_setting, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_setting, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_bullets(bullets):
	bullets.update()

	# 绘制子弹
	for bullet in bullets:
		bullet.draw_bullet()

	# 删除消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	# print(len(bullets))

def upadte_screen(ai_setting, screen, ship, bullets):
	screen.fill(ai_setting.bg_color)
	ship.blitme()
	update_bullets(bullets)

	# 将最近绘制的屏幕可见
	pygame.display.flip()
