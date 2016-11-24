#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# result = os.system('ls -l .')
#
# print result

result2 = os.popen('ls -l')
# file type
print('type: ', type(result2))

for info in result2.readlines():
    if "JiaHao" in info:
        print info.
    else:
        print "error"
