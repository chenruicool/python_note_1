#! /usr/bin/env python
# coding=utf-8

# 第十一章 测试代码

import unittest # 单元测试和测试用例 ==> 核实函数的某个方面没有问题
from chapter11_1 import get_formatted_name
from chapter11_1 import AnonymousSurvey

# 这个类必须继承 unittest.TestCase类，这样Python才知道如何运行你编写的测试。
class TestNameCase(unittest.TestCase):

	# 所有以test_打头的方法都将自动运行
	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis', 'joplin')
		# 断言方法 assertEqual
		self.assertEqual(formatted_name, 'Janis Joplin') 

if False:
	question = "Which language is your favourte language?"
	my_survey = AnonymousSurvey(question)
	my_survey.show_question()

	print('enter \'q\' to quit at any time')
	while True:
		response = input('Language: ')
		if response == 'q':
			break
		my_survey.store_respons(response)

	my_survey.show_result()

# 各种断言方法 ==> 
# assertEqual(a, b)  核实a == b
# assertNotEqual(a, b)  核实a != b 
# assertTrue(x)  核实x为True 
# assertFalse(x)  核实x为False 
# assertIn(item, list)  核实item在list中 
# assertNotIn(item, list) 核实item不在list中

# 测试类
class TestAnonymousSurvey(unittest.TestCase):
	# 如果你在TestCase类中包含了方法setUp()，Python将先运行 它，再运行各个以test_打头的方法。
	def setUp(self):
		question = "Which language is your favourte language?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['python', 'javascript']

	def test_store_single_respons(self):
		self.my_survey.store_respons(self.responses[0])
		self.assertIn('python', self.my_survey.responses)

	def test_strore_three_responses(self):
		for response in self.responses:
			self.my_survey.store_respons(response)

		for response in self.responses:
			self.assertIn(response, self.responses)



if True:
	unittest.main()

