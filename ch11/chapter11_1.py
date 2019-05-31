#! /usr/bin/env python
# coding=utf-8

# 第十一章 测试代码

def get_formatted_name(first, last):
	return first.title() + ' ' + last.title()

# full_name = get_formatted_name('janis', 'joplin')
# print(full_name)


class AnonymousSurvey():
	def __init__(self, question):
		self.question = question
		self.responses = []

	def show_question(self):
		print(self.question)

	def store_respons(self, new_respons):
		self.responses.append(new_respons)

	def show_result(self):
		for response in self.responses:
			print('- ' + response)



