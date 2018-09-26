# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:08:04 2018

@author: Administrator
"""

#setup.py
from distutils.core import setup
import py2exe

setup(console=["capture.py"],options = { "py2exe":{"dll_excludes":["api-ms-win-downlevel-shlwapi-l1-1-0.dll"]}})
