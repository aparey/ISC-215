#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:10:36 2023

@author: parey69
"""

def convertTemp(temp,scale):
    if scale == "c":
        return (temp -32) * (5.0/9.0)
    elif scale == "f":
        return temp * 9.0/5.0 + 32
    
    