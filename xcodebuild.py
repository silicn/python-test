#!/usr/bin/env python
# -*- coding:utf-8 -*-

#./autobuild.py -p youproject.xcodeproj -t youproject -o ~/Desktop/youproject.ipa
#./autobuild.py -w youproject.xcworkspace -s youproject -o ~/Desktop/youproject.ipa

from optparse import OptionParser
import subprocess
import requests

#configuration for iOS build setting
CODE_SIGN_IDENTITY = "iPhone Developer: xueren lin (S&7FVLSU4CQ)"
PROVISIONING_PROFILE = "53caf766-611a-45fe-9e99-71fa6b084dbe"
CONFIGURATION = "Debug"
SDK = "iphoneos"

# configuration for pgyer
PGYER_UPLOAD_URL = "http://fir.im/81e3"
DOWNLOAD_BASE_URL = "http://fir.im"
#USER_KEY = "15d6xxxxxxxxxxxxxxxxxx"
API_KEY = "454213ff6ed0b48cdd56fdc751977cdc"

def cleanBuildDir(buildDir):
	cleanCmd = "rm -r %s" %(buildDir)
	process = subprocess.Popen(cleanCmd, shell = True)
	process.wait()
	print "cleaned buildDir: %s" %(buildDir)


def parserUploadResult(jsonResult):
	resultCode = jsonResult['code']
	if resultCode == 0:
		downUrl = DOWNLOAD_BASE_URL +"/"+jsonResult['data']['appShortcutUrl']
		print "Upload Success"
		print "DownUrl is:" + downUrl
	else:
		print "Upload Fail!"
		print "Reason:"+jsonResult['message']

def uploadIpaToPgyer(ipaPath):
    print "ipaPath:"+ipaPath
    files = {'file': open(ipaPath, 'rb')}
    headers = {'enctype':'multipart/form-data'}
    payload = {'uKey':USER_KEY,'_api_key':API_KEY,'publishRange':'2','isPublishToPublic':'2', 'password':'DanluTest'}
    print "uploading...."
    r = requests.post(PGYER_UPLOAD_URL, data = payload ,files=files,headers=headers)
    if r.status_code == requests.codes.ok:
         result = r.json()
         parserUploadResult(result)
    else:
        print 'HTTPError,Code:'+r.status_code

def buildProject(project, target, output):
	buildCmd = 'xcodebuild -project %s -target %s -sdk %s -configuration %s build CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE="%s"' %(project, target, SDK, CONFIGURATION, CODE_SIGN_IDENTITY, PROVISIONING_PROFILE)
	process = subprocess.Popen(buildCmd, shell = True)
	process.wait()

	signApp = "./build/%s-iphoneos/%s.app" %(CONFIGURATION, target)
	signCmd = "xcrun -sdk %s -v PackageApplication %s -o %s" %(SDK, signApp, output)
	process = subprocess.Popen(signCmd, shell=True)
	(stdoutdata, stderrdata) = process.communicate()

	uploadIpaToPgyer(output)
	cleanBuildDir("./build")

def buildWorkspace(workspace, scheme, output):
	process = subprocess.Popen("pwd", stdout=subprocess.PIPE)
	(stdoutdata, stderrdata) = process.communicate()
	buildDir = stdoutdata.strip() + '/build'
	print "buildDir: " + buildDir
	buildCmd = 'xcodebuild -workspace %s -scheme %s -sdk %s -configuration %s build CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE="%s" SYMROOT=%s' %(workspace, scheme, SDK, CONFIGURATION, CODE_SIGN_IDENTITY, PROVISIONING_PROFILE, buildDir)
	process = subprocess.Popen(buildCmd, shell = True)
	process.wait()

	signApp = "./build/%s-iphoneos/%s.app" %(CONFIGURATION, scheme)
	signCmd = "xcrun -sdk %s -v PackageApplication %s -o %s" %(SDK, signApp, output)
	process = subprocess.Popen(signCmd, shell=True)
	(stdoutdata, stderrdata) = process.communicate()

	uploadIpaToPgyer(output)
	cleanBuildDir(buildDir)

def xcbuild(options):
	project = options.project
	workspace = options.workspace
	target = options.target
	scheme = options.scheme
	output = options.output

	if project is None and workspace is None:
		pass
	elif project is not None:
		buildProject(project, target, output)
	elif workspace is not None:
		buildWorkspace(workspace, scheme, output)

def main():

	parser = OptionParser()
	parser.add_option("-w", "--workspace", help="Build the workspace name.xcworkspace.", metavar="name.xcworkspace")
	parser.add_option("-p", "--project", help="Build the project name.xcodeproj.", metavar="name.xcodeproj")
	parser.add_option("-s", "--scheme", help="Build the scheme specified by schemename. Required if building a workspace.", metavar="schemename")
	parser.add_option("-t", "--target", help="Build the target specified by targetname. Required if building a project.", metavar="targetname")
	parser.add_option("-o", "--output", help="specify output filename", metavar="output_filename")

	(options, args) = parser.parse_args()

	print "options: %s, args: %s" % (options, args)

	xcbuild(options)

if __name__ == '__main__':
	main()
