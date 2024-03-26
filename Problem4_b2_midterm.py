# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:49:45 2024

@author: Furka
"""
import numpy as np

X = np.array([[0, 1],[1, 0]])
Y = np.array([[0,-1j],[1j,0]])
I = np.array([[1, 0],[0, 1]])
Z = np.array([[1, 0], [0, -1]])

a = np.dot(Y,X)
b = np.dot(a,X)
c = np.dot(b,Y)

print(c)

d = np.dot(Z,Z)
e = np.dot(d,Z)
f = np.dot(e,Z)

print(f)