#! /usr/bin/env python
# coding=utf-8

# 第七章 用户输入和while循环

# 函数input
if False:
	message = input("tell me sth, ")
	print(message)

	name = input("please input your name: ")
	print 'Hello ', name

	age = input("please tell me your age: ")
	print age, int(age)>=18

# 求模
print 5%3

if False:
	num = input("input a num:")
	num = int(num)
	if num %2 == 0:
		print("the num " + str(num) + " is even.")
	else:
		print("the num " + str(num) + " is odd.")

#######################################################
# while循环
current_number = 1
while current_number<=5:
	print "while ",current_number
	current_number = current_number + 1

prompt = "Tell me sth, (Enter 'quit' to exit)"
message = ""
if False:
	while message != "quit":
		message = input(prompt)
		print(message)

if False:
	active = True
	while active:
		message = input(prompt)
		if message == "quit":
			active = False
			break
		else:
			print(message)

#######################################################
# 循环中使用continue
count = 0
while count<10:
	count += + 1
	if count % 2 == 0:
		continue
	print 'continue', count

# while 处理字典
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	confirmed_users.append(current_user)
	print 'verifying current_user:' + current_user

for user in confirmed_users:
	print user.title()

# while 删除
animals = ['cat', 'dog', 'cat', 'mouse']
print 'before animals', animals
while 'cat' in animals:
	animals.remove('cat')

print 'after animals', animals
