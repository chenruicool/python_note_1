#! /usr/bin/env python
# coding=utf-8

# 第九章 类

# 创建Dog类
class Dog():  # 首字母大写==>类
	# __init__()是一个特殊的方法，每当你根据Dog类创建新实 例时，Python都会自动运行它
	# 每个与类相关联的方法 调用都自动传递实参self，它是一个指向实例本身的引用
	# 方法 __init__()并未显式地包含return语句，但Python自动返回一个实例
	def __init__(self, name, age): 
		# 该变量被关联到当前创建的实例
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + ' is now sitting!')

	def roll_over(self):
		print(self.name.title() + ' is now rolled over!')

# 首字母小写==>实例 
my_dog = Dog('willile', 6)
print 'my_dog.name:',my_dog.name, ",my_dog.age:",my_dog.age
my_dog.sit()
my_dog.roll_over()

#######################################################
# Car 类
class Car(object):
	def __init__(self, make, module, year):
		self.make = make
		self.module = module
		self.year = year
		self.odometer = 0
	
	def get_describtive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.module
		return long_name

	def read_odometer(self):
		return self.odometer

	def update_odometer(self, odometer):
		self.odometer = odometer

	def increment_odometer(self, miles):
		self.odometer += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_describtive_name())

my_used_car = Car('subaru', 'outback', 1023)
my_used_car.update_odometer(23000)
my_used_car.increment_odometer(100)
print(my_used_car.read_odometer())

#######################################################
# 将实例用作属性
class Battery(object):
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		long_info = 'This car has ' + str(self.battery_size) + ' -khw battery'
		print(long_info)

	def get_range(self):
		if self.battery_size == 70:
			car_range = 240
		elif self.battery_size == 85:
			car_range = 270

		message = "This car can go " + str(car_range) + ' miles.'
		print(message)

# 继承
class ElectricCar(Car):
	def __init__(self, make, model, year):
		# python 3
		# super().__init__(make, model, year)
		#python 2.7
		super(ElectricCar, self).__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		print('fill_gas_tank')

my_tesla = ElectricCar('tesla', 'module', 2016)
print(my_tesla.get_describtive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#######################################################
# 导入单个类 ==> from file_name import class_name
# 从一个模块中导入多个类 ==> from file_name import class_name1, class_name2
# 导入模块中的所有类 ==> from file_name import *

#######################################################
# Python 标准库

# 创建字典并记录其中的键—值对的添加顺序
from collections import OrderedDict
favorite_languages = OrderedDict() # 创建一个空的有序字典

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

#######################################################
# 类名应采用驼峰命名法
# 实例名和模块名都采用小写格式，并在单词之间加上下划线。


