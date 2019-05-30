# 第一章 起步

#! /usr/bin/env python
# coding=utf-8

class Test():
	def __init__(self, name):
		self.name = name

	def print_name(self):
		print self.name

aList = []
for i in range(10):
	test = Test('i=' + str(i))
	aList.append(test)

# aList.print_name()

print 'c'.find('s')
