#! /usr/bin/env python
# coding=utf-8

# 第四章 操作列表

# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	# print magician
	print magician.title() + ", that was a great trick!" 

print "Thank you, everyone. That was a great magic show!"

#######################################################
# 创建数值列表
for value in range(1,5): # 只打印 1 2 3 4 
	print value

numbers = list(range(1,6)) # 只打印 1 2 3 4 5
print numbers

even_numbers = list(range(2,11,2)) # 只打印 2 4 6 8 10
print(even_numbers)

# 两个星号(**)表示乘方运算
print 5**3

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print min(digits), max(digits), sum(digits)

# 列表解析
squares = [value**2 for value in range(1,11)]
print 'squares=', squares

#######################################################
# 切片 ==>如果没有指定第一个索引，Python将自动从列表开头开始; 如果没有指定第二个索引,Python将自动到最后一个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #只打印 第0、1、2个

# 复制列表 ==> 两个不同的列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print 'friend_foods=', friend_foods

# 这两个 变量都指向同一个列表
friend_foods_1 = my_foods

#######################################################
# 元组 ==> 不可变的列表被称为元组

dimensions = (200, 50)
print dimensions[0], dimensions[1]

# dimensions[0] = 250 不能修改

for dimension in dimensions:
	print dimension

# 修改元组变量 ==> 给存储元组的变量赋值
dimensions = (400, 100)
print dimensions


