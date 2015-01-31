# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os, sys
import re, codecs
import shutil, glob

def _find(pathname, matchFunc=os.path.isfile):
    for dirname in sys.path:
        candidate = os.path.join(dirname, pathname)
        if matchFunc(candidate):
            return candidate

def find_file(pathname):
    return _find(pathname)

def find_dir(path):
    return _find(path, matchFunc=os.path.isdir)

def find_glob_path(filepath):
    return glob.glob(filepath)