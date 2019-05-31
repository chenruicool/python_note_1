#! /usr/bin/env python
# coding=utf-8

# 第十章 文件和异常

# 函数open()接受一个参数: 要打开的文件的名称 ==> 返回一个表示文件的对象
# 关键字with在不再需要访问文件后将其关闭
with open('pi_digits.txt') as file_object:
	content = file_object.read()
	print 'content:', content
	print 'content.rstrip:', content.rstrip()

	for line in file_object:
		print line.rstrip() # 要消除这些多余的空白行，可在print语句中使用rstrip()

# 使用readlines
with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()
for line in lines:
	print ('line=' + line).rstrip()

# 圆周率值中包含你的生日吗
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.rstrip()

if False:
	birthday = input("Enter your birthday, in the form mmddyy: ")
	birthday = str(birthday)
	if birthday in pi_string:
		print("Your birthday appears in the first million digits of pi!")
	else:
		print("Your birthday does not appear in the first million digits of pi.")

#######################################################
# 写入空文件
# 读取模 式('r')、写入模式('w')、附加模式('a')
# Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数 str()将其转换为字符串格式。
filename = 'programming.txt'
with open(filename, 'w') as file_object: # 以写入模式打开这个文件
# with open(filename, 'a') as file_object:
	file_object.write("I LOVE programming")

# 异常 ==> 使用try-except代码块
a = 5
b = 1
try:
	answer = (a/b)
except ZeroDivisionError:
	print('You can not divide by 0')
else:
	print(answer)

try:
	with open('notExistFile.txt') as f_object:
		lines = f_object.readlines()
# except FileNotFoundError:
except:
	print('not found file')

# 分析文本
def count_words(filename):
	try:
		with open(filename) as f_object:
			lines = f_object.read()
	except:
		print('can not found file')
	else:
		words = lines.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

count_words('alice.txt')

#######################################################
# 存储数据
# JSON(JavaScript Object Notation)
import json

# 存储
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_object:
	json.dump(numbers, f_object)

# 读取
with open(filename) as f_object:
	ret_numbers = json.load(f_object)
	print 'ret_numbers=', ret_numbers

# 保存和读取用户生成的数据
filename = 'username.json'
try:
	with open(filename) as f_object:
		username = json.load(f_object)
except:
	with open(filename, 'w') as f_object:
		json.dump('inputname', f_object)
		print 'we will remember you when you back'
else:
	print('welcome:' + username)



