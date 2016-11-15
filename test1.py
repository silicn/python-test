#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

import time

import test


# for i in xrange(10000):
# 	#转化为整型值
# 	x = int(math.sqrt(i + 100))
# 	y = int(math.sqrt(i + 268))

# 	if (x * x == i + 100) and (y * y == i+268):
# 		pass
# 		print i 




# year  = int(raw_input('year:\n'))
# month = int(raw_input('month:\n'))
# day = int(raw_input('day:\n'))

# months = (0,31,59,90,120,151,181,212,243,273,304,334)

# if 0 <month <= 12:
# 	sum = months[month - 1]
# else:
# 	print 'data error'

# sum += day

# leap = 0

# if (year %400 == 0) or ((year%4) == 0 and (year%100 != 0)):
# 	leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print 'it is the %dth day.' % sum   



# l = []

# for i in xrange(3):
# 	x = int(raw_input('interger:\n'))
# 	l.append(x)
# l.sort()
# print l



# def fib(n):
# 	a,b = 1,1
# 	for i in range(n-1):
# 		a,b = b,a+b
# 	return a

# # 输出了第10个斐波那契数列
# print fib(10)


# a = [1,2,3]
# b = a[:]
# print b 



# for i in range(1,10):
#     for j in range(1,10):
#         result = i * j
#         print '%d * %d = % -3d' % (i,j,result)
#     pass


# import time

# myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
# 	print key, value
# 	time.sleep(1) # 暂停 1 秒



# f1 = 1
# f2 = 1
# for i in range(1,21):
#     print '%12ld %12ld' % (f1,f2),
#     if (i % 3) == 0:
#         print ''
#     f1 = f1 + f2
#     f2 = f1 + f2



if __name__ == '__main__':
	a = 077
	b = a & 3
	print 'a & b  = %d' % b

	b &= 7

	print 'a & b = %d' % b

pass

list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5,6,7]

print "list1[0] :",list1[0]

print "list2[1:5]",list2[1:5]


pass

tup1 = (12,34.56)

tup2 = ('abc','xyz')

tup3 = tup1 + tup2

print tup3

pass

dict = {'alice':'1234','beth':'5678','cecil':'2738'}
print dict

ticks = time.time()
print "当前时间为：",ticks

localtime = time.asctime(time.localtime(time.time()))   

print "本地时间：",localtime

def test(str):
	print str 
	return

test("设么东西")


def sum( a, b):
	print a+b
	return a+b 


sum(3,4)

test.sum(5,6)






