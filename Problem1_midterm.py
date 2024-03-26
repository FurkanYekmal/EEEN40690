# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:13:18 2024

@author: Furka
"""

import numpy as np

# Define the Pauli-Z matrices
Z0 = np.array([[1, 0], [0, -1]])
Z1 = np.array([[1, 0], [0, -1]])

# Tensor product of the two matrices
H = np.kron(Z0, Z1)

# Define the state vector for |0> tensor product |1>
psi = np.array([0, 1, 0, 0]).reshape(4, 1)

# Compute the expectation value of H with respect to psi
expectation_value = np.vdot(psi, np.dot(H, psi))

print(expectation_value)
