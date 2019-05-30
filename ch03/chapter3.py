#! /usr/bin/env python
# coding=utf-8

# 第三章 列表简介

# 定义一个列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print 'bicycles=', bicycles

# 索引从0而不是1开始
print '第0个 ', bicycles[0]
print '第1个 ',bicycles[1]

# 取数据
message = "My first bicycle was a " + bicycles[0].title() + "."
print '取数据', message

# 修改列表元素
bicycles[0] = 'aaabbb'
print '修改列表元素', bicycles

# 添加列表元素 ==>添加到末尾
bicycles.append('ducati')
print '添加列表元素', bicycles

# 插入元素 ==> 插入到指定位置
bicycles.insert(1, 'two')
print '插入元素', bicycles

# 删除元素 ==> 删除指定位置
del bicycles[1]
print '删除元素', bicycles

# 使用 pop 方法 ==> 默认删除最后一个
pop_data = bicycles.pop(0)
print '使用 pop 方法', pop_data, bicycles

# 根据值来删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print '根据值来删除元素 11', motorcycles
motorcycles.remove('ducati')
print '根据值来删除元素 22', motorcycles

#######################################################
# 使用方法 sort() 对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print 'cars sort ', cars
cars.sort(reverse=True)
print 'cars sort reverse ', cars

# 使用函数 sorted() 对列表进行临时排序
print 'cars sorted ', sorted(cars)

# 倒着打印列表
print ' before cars.reverse()', cars
cars.reverse()
print ' aftere cars.reverse()', cars

# 确定列表的长度
print '确定列表的长度', len(cars)









