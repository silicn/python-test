#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Employee():
    # """docstring for Employee."""
    def __init__(self, name):
    #s    super(Employee, self).__init__()
        self.name  = name

    def displayName(self):
        print self.name
