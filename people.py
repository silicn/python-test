#!/usr/bin/python
# -*- coding: UTF-8 -*-


class People():

    sender = ""
    
    def __init__(self,name):
        self.name = name
        People.sender = "男"

    def disPlayName(self):
        print self.name

    def disPlaySend(self):
        print People.sender
