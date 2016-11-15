#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Employee():
    # """docstring for Employee."""

    employeeCount = 0

    def __init__(self, name):
        super(Employee, self).__init__()
        self.name  = name

    def displayName(self):
        print self.name

    def displayCount(self):
        print self.employeeCount
