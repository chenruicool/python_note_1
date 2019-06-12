#! /usr/bin/env python
# coding=utf-8

# 第十五章 生成数据

# 安装 matplotlib
# pip3 install matplotlib


import matplotlib.pyplot as plt

from random import choice

# 绘制简单的折线图
if False:
	squares = [1, 4, 9, 16, 25]
	# plt.plot(squares, linewidth=5)

	input_values = [1, 2, 3, 4, 5]
	plt.plot(input_values, squares, linewidth=5)
	plt.show()

if False:
	plt.scatter(2, 4, s=200)
	x_values = [1, 2, 3, 4, 5]
	y_values = [1, 4, 9, 16, 25]
	plt.scatter(x_values, y_values, s=100)
	plt.show()

if False:
	x_values = list(range(1, 1001))
	y_values = [x**2 for x in x_values]
	# plt.scatter(x_values, y_values, c='red', edgecolor='none',s=40)
	plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none',s=40)
	plt.axis([0, 1100, 0, 1100000])

	plt.title("Square Numbers", fontsize=24)
	plt.xlabel("Value", fontsize=14)
	plt.ylabel("Square of Value", fontsize=14)
	plt.tick_params(axis='both', which='major',labelsize=14)
	plt.show()

	plt.savefig('squares_plot.png', bbox_inches='tight')

# 随机漫步
class RandomWalk():
	def __init__(self, num_points=5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]
		
	def fill_walk(self):
		while len(self.x_values) < self.num_points:
			x_direction = choice([1, -1])
			x_distance = choice([0, 1, 2, 3, 4])
			x_step = x_direction * x_distance

			y_direction = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4])
			y_step = y_direction * y_distance

			if x_step == 0 and y_step == 0:
				continue

			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)

if True:
	rw = RandomWalk()
	rw.fill_walk()
	plt.scatter(rw.x_values, rw.y_values, s=15)
	plt.show()

