#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://bitbucket.org/iBotPeaches/apktool/downloads
# Install and set apktool: https://code.google.com/p/android-apktool/wiki/Install

import os, sys
import shutil
import subprocess
from optparse import OptionParser
import comm

workpath = os.getcwd()
toolpath = os.path.join(workpath, 'tools')
apkpath = os.path.join(workpath, 'apks')

def aaptdump(path):

    try:
        aaptdump = 'aapt d badging ' + path + ' AndroidManifest.xml'
        content = subprocess.check_output(aaptdump, shell=True)

        appname = ''
        packagename = ''
        launchableactivity = ''
        versioncode = ''
        versionname = ''
        sdkversion = ''
        targetsdkversion = ''

        if content.find('ERROR') == -1:
            lines = content.splitlines()
            for index, line in enumerate(lines):
                #print line
                if line.startswith('package:'):
                    info = line.split("'")
                    packagename = info[1]
                    versioncode = info[3]
                    versionname = info[5]

                if line.startswith('application-label:'):
                    appname = line.replace('\'','').replace('application-label:','').decode('utf-8')

                if line.startswith('launchable-activity'):
                    launchableactivity = line.split("'")[1]

                if line.startswith('sdkVersion'):
                    sdkversion = line.replace('\'','').replace('sdkVersion:','')

                if line.startswith('targetSdkVersion'):
                    targetsdkversion = line.replace('\'','').replace('targetSdkVersion:','')

        print appname, packagename, launchableactivity, versioncode, versionname, sdkversion, targetsdkversion

    except Exception, ex:
        print ex

def aaptanalyser(path):

    apkdedecompiled = os.path.join(workpath, path.split('/')[-1].replace('.apk',''))
    xwalkcoreviewsmali = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'core', 'XWalkView.smali')

    try:
        aaptlist = 'aapt list -a ' + path
        r = subprocess.check_output(aaptlist, shell=True)

        if r.find('libxwalkcore.so') > -1:
            print 'embedded mode'
        elif comm.find_file(xwalkcoreviewsmali):
            print 'shared mode'

        if r.find('lib/armeabi-v7a/libxwalkcore.so') >-1 and r.find('lib/x86/libxwalkcore.so') >-1:
                print 'ARM + x86'
        elif r.find('lib/armeabi-v7a/libxwalkcore.so') >-1:
                print 'ARM'
        elif r.find('lib/x86/libxwalkcore.so') >-1:
                print 'x86'
    except Exception, ex:
        print ex

def apktoolanalyser(path):

    apkname = path.split('/')[-1]
    apkdedecompiled = os.path.join(workpath, apkname.replace('.apk',''))

    xwalkcoreviewsmali = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'core', 'XWalkView.smali')
    apachecordova = os.path.join(apkdedecompiled, 'smali', 'org', 'apache', 'cordova')
    xwalkappruntime = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'app', 'runtime')
    xwalkcoreinternal = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'core', 'internal')
    intelxdk = os.path.join(apkdedecompiled, 'smali', 'com', 'intel', 'xdk')
    intelxdkjs = os.path.join(apkdedecompiled, 'assets', 'www', 'intelxdk.js')

    try:
        apktoolcmd = 'apktool d -f ' + path
        t = subprocess.check_output(apktoolcmd, shell=True)
        if comm.find_dir(apkdedecompiled):
            if comm.find_file(xwalkcoreviewsmali):
                print 'crosswalk app'
                print 'xwalk/core'
                if comm.find_dir(xwalkappruntime):
                    print 'xwalk/app/runtime'
                if comm.find_dir(xwalkcoreinternal):
                    print 'xwalk/core/internal'
            elif comm.find_dir(xwalkcoreinternal):
                print 'RuntimeLib.apk'
            else:
                print 'not a crosswalk app'

            if comm.find_dir(apachecordova):
                print 'org/apache/cordova'

            if comm.find_dir(intelxdk) or comm.find_file(intelxdkjs):
                print 'com/intel/xdk or intelxdk.js'

            dirlist = []
            smalipath = os.path.join(apkdedecompiled, 'smali')

            for dirname, dirnames, filenames in os.walk(smalipath):
                dirlist.append(dirname.replace(smalipath + '/', ''))
            print dirlist

        else:
            print 'Decompile failed: ' + apkname
        shutil.rmtree(apkdedecompiled)

    except Exception, ex:
        print ex

def analyser(path):
    print path
    aaptdump(path)
    aaptanalyser(path)
    apktoolanalyser(path)
    print '_________________________________________________________________________________________________'

def run(path):
    if path.lower().endswith('.apk'):
        analyser(path)
    else:
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith('apk'):
                    analyser(os.path.join(path, name))

def option_check(path):
    if path:
        run(path)
    else:
        print 'Path option is not defined, use default value: ' + apkpath
        run(apkpath)

def main():
    parser = OptionParser()
    parser.add_option('-p', '--path', dest='path',
                  help = '(mandatory) The path of apk or apks.')
    (options, args) = parser.parse_args()
    option_check(options.path)

if __name__ == '__main__':
    sys.exit(main())
    #python main.py
    #python main.py -p <apk file or folder>
    #python main.py -p /home/belem/github/apk-checker/apks/Test_0.0.1_arm_embedded.apk