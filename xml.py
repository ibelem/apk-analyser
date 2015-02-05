#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: belem

import os, sys
from datetime import *
from lxml import etree as et
import comm

def insert_xml_result(pathname, apkfile, apksize, appname, packagename,
                      launchableactivity, versioncode, versionname, sdkversion, targetsdkversion,
                      mode, architecture,
                      crosswalk, webview, chromium, coreinternal, cordova, isintelxdk, xwalklist, chromiumlist, cordovalist, smalilist, assetlist, note):
    print apkfile, apksize, appname, packagename, launchableactivity, versioncode, versionname, sdkversion, targetsdkversion, mode, architecture, crosswalk, coreinternal, cordova, isintelxdk, webview, note

    parser = et.XMLParser(remove_blank_text=True)
    tree = et.parse(pathname, parser)
    xroot = tree.getroot()
    xapk = et.SubElement(xroot, 'apk')
    xapk.attrib['id'] = packagename
    xcrosswalk = et.SubElement(xapk, 'crosswalk')
    xcrosswalk.attrib['iscrosswalk'] = crosswalk
    xcrosswalk.attrib['mode'] = mode
    xcrosswalk.attrib['architecture'] = architecture
    xcrosswalk.attrib['webview'] = webview
    xcrosswalk.attrib['chromium'] = chromium
    xcrosswalk.attrib['coreinternal'] = coreinternal
    xcrosswalk.attrib['cordova'] = cordova
    xcrosswalk.attrib['intelxdk'] = isintelxdk
    xcrosswalk.attrib['note'] = note

    xapp = et.SubElement(xapk, 'app')
    xapp.attrib['name'] = appname
    xapp.attrib['file'] = apkfile
    xapp.attrib['size'] = apksize
    xapp.attrib['launchableactivity'] = launchableactivity
    xapp.attrib['versioncode'] = versioncode
    xapp.attrib['versionname'] = versionname
    xapp.attrib['sdkversion'] = sdkversion
    xapp.attrib['targetsdkversion'] = targetsdkversion

    for list in xwalklist:
        if list.strip():
            xxwalk = et.SubElement(xapk, 'xwalk')
            xxwalk.text = list.strip()

    for list in chromiumlist:
        if list.strip():
            xchromium = et.SubElement(xapk, 'chromium')
            xchromium.text = list.strip()

    for list in cordovalist:
        if list.strip():
            xcordova = et.SubElement(xapk, 'cordova')
            xcordova.text = list.strip()

    for list in smalilist:
        if list.strip():
            xsmali = et.SubElement(xapk, 'smali')
            xsmali.text = list.strip()

    for list in assetlist:
        if list.strip():
            xasset = et.SubElement(xapk, 'asset')
            xasset.text = list.strip()
    tree.write(pathname, pretty_print=True, xml_declaration=True, encoding='utf-8')

def generate_xml_report(pathname):
    tmp = pathname.split('/')[-1]
    dirname = pathname.replace('/' + tmp, '')
    comm.mk_dir(dirname)
    print 'Save result into:' + pathname

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    root = et.Element('apks')
    root.addprevious(et.PI('xml-stylesheet', 'type="text/xsl" href="apk-analyser-result.xsl"'))
    root.attrib['datetime'] = date
    file = et.ElementTree(root)
    file.write(pathname, pretty_print=True, xml_declaration=True, encoding='utf-8')

