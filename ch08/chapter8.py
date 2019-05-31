#! /usr/bin/env python
# coding=utf-8

# 第八章 函数

# 定义函数
def greet_user(username):
	print 'Hello ' + username.title() + '.'

# 实参是调用函数时传递给函数的信息。 ==> 值'jesse'是一个实参
greet_user('jessa')

# 定义一个函数 ==> 赋予 animal_type 默认值 'dog'
def describe_pet(pet_name, animal_type = 'dog'):
	print 'I have a ' + animal_type + '.'
	print 'My ' + animal_type + '\'s name is ' + pet_name.title() + '.'

# 位置实参
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# 关键字实参
describe_pet(pet_name='tom', animal_type='cat')
describe_pet(pet_name='ww')

#######################################################
# 返回简单值
def get_format_name(firstname, lastname, middlename=''):
	if middlename:
		full_name = firstname + ' ' + middlename + ' ' + lastname
	else:
		full_name = firstname + ' ' + lastname

	return full_name.title()

# 返回字典
musician = get_format_name('jimi', 'hendrix')
print 'musician:', musician

def build_person(firstname, lastname):
	person = {'first':firstname, 'last':lastname}
	return person

print(build_person('jimi', 'hendrix'))

# 传递列表
def greet_users(names):
	for name in names:
		print 'Hello ' + name.title() + '!'

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 函数中修改列表
def print_modules(unprint_modules, completed_modules):
	while unprint_modules:
		current_module = unprint_modules.pop()
		print "print current_module " + current_module
		completed_modules.append(current_module)

def show_completed(completed_modules):
	for current_module in completed_modules:
		print "complet current_module " + current_module

unprint_modules = ['apple', 'banana', 'pear']
completed_modules = []

if False:
	print_modules(unprint_modules, completed_modules)
	show_completed(completed_modules)
	print unprint_modules, completed_modules

#禁止函数修改列表
print_modules(unprint_modules[:], completed_modules)
show_completed(completed_modules)
print unprint_modules, completed_modules

#######################################################
# 传递任意数量的实参
def make_pizza(size, *toppings):
	print 'make a ' + str(size) + ' pizza with toppings:'
	print toppings, type(toppings)

make_pizza(6, 'pepperoni')
make_pizza(8, 'pepperoni', 'mushrooms')

# 关键字实参
# 形参**user_info中的两个星号让Python创建一个名为user_info的空字典,并将收到的所有名称—值对都封装到这个字典中
def build_profile(firstname, lastname, **user_info):
	profile = {}
	profile['firstname'] = firstname
	profile['lastname'] = lastname
	for k, v in user_info.items():
		profile[k] = v

	return profile

user_profile = build_profile('albert', 'einstein', location='New York', tel='123456')
print user_profile

#######################################################
# 导入整个模块 ==> 使用as给模块指定别名/使用as给函数指定别名
# import module_name
# import module_name as m
# from module_name import functon_name
# from module_name import functon_name as fn

# 导入模块中的所有函数
# from module_name import *




