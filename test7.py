#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time

def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName, time.ctime(time.time()))


print_time("thread_1",1)

print_time("thread_2",1)
