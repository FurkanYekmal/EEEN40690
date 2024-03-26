# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:00:38 2024

@author: Furka
"""
import numpy as np

#matrices

X = np.array([[0, 1],[1, 0]])

H = (1/(np.sqrt(2)))*np.array([[1, 1],[1, -1]])

Z = np.array([[1, 0], [0, -1]])

#We show HXH = Z

g = np.dot(H,X)

f = np.dot(g,H)

#And HZH = X

r = np.dot(H,Z)

h = np.dot(r,H)

print(f)
print(h)
