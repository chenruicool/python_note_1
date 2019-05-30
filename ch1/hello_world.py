#! /usr/bin/env python
# coding=utf-8
# print("good")
name = "ada lovelace"
# print(name.title())

# print(6**3)
# print(3/2, 3.0/2)

# list = [value**2 for value in range(1,10)]
# for i in range(1,21):
#  	print i

aList = [i for i in range(1,21)]
bList = aList[:]
bList.append(1)
print min(aList), max(aList), sum(aList), aList[-2:], bList

print (5 in aList), (100 in aList), (200 not in aList)

cList = []
if cList:
	print 'cList is'
else:
	print 'not cList'