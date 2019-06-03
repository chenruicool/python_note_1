#! /usr/bin/env python
# coding=utf-8

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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
	elif event.key == pygame.K_q:
		sys.exit()

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

def update_bullets(ai_setting, screen, aliens, bullets):
	bullets.update()

	# 绘制子弹
	for bullet in bullets:
		bullet.draw_bullet()

	# 删除消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	# print(len(bullets))


def update_bullets_aliens_collision(ai_setting, screen, aliens, bullets):
	# 两个实参True告诉Pygame删除发生碰撞的子弹和外星人。
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if len(aliens) == 0:
		bullets.empty()
		create_fleet(ai_setting, screen, aliens)

# 刷新外星人
def update_aliens(ai_setting, stats, ship, aliens, screen, bullets):
	check_fleet_edges(ai_setting, aliens)
	aliens.update()
	# 检测外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		print("Ship hit!!!")
		ship_hit(ai_setting, stats, screen, ship, aliens, bullets)

	# 检测外星人是否达到底部
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen.get_rect().bottom:
			print("alien reach bottom!!!")
			ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
			break

def create_fleet(ai_setting, screen, aliens):
	# 计算出大小
	alien = Alien(ai_setting, screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	available_space_x = ai_setting.screen_width - 2*alien_width
	available_space_y = (ai_setting.screen_height - 4*alien_height)/2
	# x方向的个数
	number_aliens_x = int(available_space_x/(2*alien_width))
	# y方向的个数
	number_aliens_y = int(available_space_y/(2*alien_height))

	# print('available_space_x=', available_space_x)
	# print('available_space_y=', available_space_y)
	# print('alien_width=', alien_width)
	# print('alien_height=', alien_height)
	for y_index in range(number_aliens_y):
		for x_index in range(number_aliens_x):
			alien = Alien(ai_setting, screen)
			alien.x = alien_width + 2*alien_width*x_index
			alien.rect.x = alien.x
			alien.rect.y = alien_height + 2*alien_height*y_index
			aliens.add(alien)
			# print(len(aliens))

def upadte_screen(ai_setting, stats, screen, ship, bullets, aliens):
	screen.fill(ai_setting.bg_color)
	ship.blitme()
	if stats.game_active:
		update_bullets(ai_setting, screen, aliens, bullets)
		update_bullets_aliens_collision(ai_setting, screen, aliens, bullets)
		update_aliens(ai_setting, stats, ship, aliens, screen, bullets)
		aliens.draw(screen)

	# 将最近绘制的屏幕可见
	pygame.display.flip()

def change_alien_direction(ai_setting, aliens):
	# 向下
	for alien in aliens.sprites():
		alien.rect.y += ai_setting.fleet_drop_speed
	# 取反方向
	ai_setting.fleet_direction *= -1


def check_fleet_edges(ai_setting, aliens):
	for alien in aliens:
		if alien.check_edge():
			change_alien_direction(ai_setting, aliens)
			break

# 外星人撞到飞船
def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):
	aliens.empty()
	bullets.empty()

	stats.ships_left -= 1
	if stats.ships_left > 0:
		# 创建新的
		create_fleet(ai_setting, screen, aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False
		print('you lose')



