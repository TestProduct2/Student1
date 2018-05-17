# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:31:23 2018

@author: aparnami
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

