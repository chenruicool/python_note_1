#! /usr/bin/env python
# coding=utf-8

# 第五章 if语句

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper()) 
	else:
		print(car.title())

# 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

# 比较数字
answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

# 使用 and 检查多个条件
# 使用 or 检查多个条件

# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
	print 'mushrooms is in requested_toppings '

# 检查特定值是否不包含在列表中
if not 'aaa' in requested_toppings:
	print 'aaa is in requested_toppings '

# 布尔表达式
game_active = True
can_edit = False

# if-elif-else 结构
age = 12
if age < 4:
	print 'Your admission cost is $0.'
elif age < 18:
	print 'Your admission cost is $5.'
else:
	print 'Your admission cost is $10.'

# 确定列表不是空的
requested_toppings = []
if requested_toppings:
	print 'requested_toppings True' 
else:
	print 'requested_toppings False' 



