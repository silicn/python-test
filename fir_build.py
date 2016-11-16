#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess

fir_token = "454213ff6ed0b48cdd56fdc751977cdc"

out_put_path = "Users/JiaHao/Desktop/build/"


def buildProject():
    log =  raw_input('输入build log:')
    buildCmd = 'fir build_ipa /Users/JiaHao/Desktop/YunKeAssistant/YunKeAssistant1.0.1 -o %s -p -c "%s" -Q -T %s' %(out_put_path,log,fir_token)
    process = subprocess.Popen(buildCmd, shell = True)
	# process.wait()
    print "build xcode ..."

def main():
    buildProject()

if __name__ == '__main__':
	main()
