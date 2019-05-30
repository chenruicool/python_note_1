#! /usr/bin/env python
# coding=utf-8

# 第二章 变量和简单数据类型

# 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头
message = "Hello Python world!"
print(message)

# 修改字符串的大小写
name = "ada lovelace"
print(name.title())

# 合并(拼接)字符串 ==> 使用加号(+)来合并字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# 使用制表符或换行符来添加空白
print("\tPython")

# 删除空白
s = ' python '
a = s.rstrip()
b = s.lstrip()
c = s.strip()
print(len(s), len(a), len(b), len(c))

#######################################################
# 连接数字
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# 取整
print(3/2, 3.0/2, 3/2.0, 3.0/2.0)

#######################################################
# Python 之禅
# 终端输入 python3 ==> import this

