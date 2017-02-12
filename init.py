# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:55:12 2017

@author: David
"""
import ctypes
def init():
        i = ctypes.c_char('a')
        j = ctypes.pointer(i)
        c = 0
        while True:
                j[c] = 'a'
                c += 1
        j
init()