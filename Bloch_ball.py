# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:24:05 2024

@author: Furka
"""

import qutip as qt
import numpy as np

# Create a Bloch sphere
b = qt.Bloch()

# Define Bloch vectors
bloch_vector_PlusY = np.array([0, 1, 0])
bloch_vector_MinusX = np.array([-1, 0, 0])
bloch_vector_mixed = 0.3 * bloch_vector_MinusX + 0.7 * bloch_vector_PlusY

# Add vectors to the Bloch sphere
b.add_vectors(vectors=[bloch_vector_MinusX, bloch_vector_PlusY, bloch_vector_mixed])

# Show the plotted Bloch sphere
b.show()

