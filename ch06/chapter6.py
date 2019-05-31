#! /usr/bin/env python
# coding=utf-8

# 第五章 字典 ==> 一系列键-值对

# 一个简单的字典
alien_0 = {'color':'green', 'points':5}
print alien_0['color'], alien_0['points']

# 使用字典
new_points = alien_0['points']
print 'you just eared ' + str(new_points) + ' points'

# 添加键—值对
print alien_0
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print 'alien_0=', alien_0

#######################################################
# 创建一个空字典
alien_0 = {}

#修改字典中的值
alien_0 = {'color':'green'}
print 'The alien is ' + alien_0['color'] + "."
alien_0['color'] = "yellow"
print 'The alien is ' + alien_0['color'] + "."
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print ('Original x_position is: ' + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('new x_position is:' + str(alien_0['x_position']))

# 删除键—值对
alien_0 = {'color':'green', 'points':5}
del alien_0['color']
print 'after del alien_0=', alien_0

#######################################################
# 类似对象组成的字典
favorite_language = {
	'jen':'python',
	'sarah':'c',
	'edward':'rub',
	'phil':'python',
}
print('jen favorite_language is ' + favorite_language['jen'].title() + '.')

#遍历字典
user_0 = {
	'username':'username',
	'first':'first',
	'last':'last',
}
# 遍历所有的键—值对
for key, value in user_0.items():
	print '遍历字典:', key, value

# 遍历字典中的所有键
for key in user_0.keys():
	print '遍历字典中的所有键:', key

# 按顺序遍历字典中的所有键
for sortedKey in sorted(user_0.keys()):
	print 'sorted: ' ,sortedKey

# 遍历字典中的所有值
for value in user_0.values():
	print '遍历字典中的所有值:' + value.title()

for language in set(favorite_language.values()):
	print 'unique language:' + language.title()

#######################################################
# 嵌套
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print alien

# 字典列表 ==>列表中存储字典
aliens = []
for i in range(30):
	new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == "green":
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
print aliens[:5]

# 字典中存储列表
pizza = {
	'crust':'thick',
	'toppings':['mushrooms', 'extra cheese'],
}
print('You ordered a ' + pizza['crust'] + ' with the following toppings:')
for topping in pizza['toppings']:
	print(topping)

# 字典中存储字典
users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
	},	
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
	},
}

for name, user_info in users.items():
	print name.title() + " first is:" + user_info['first'].title()
	print name.title() + " last is:" + user_info['last'].title()
	print name.title() + " location is:" + user_info['location'].title()

