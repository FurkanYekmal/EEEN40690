# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:30:35 2024

@author: Furka
"""

#Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy.constants import physical_constants
from scipy.integrate import solve_ivp
#Constants
energy_zero = -0.5*physical_constants['Bohr magneton'][0]
energy_one = +0.5*physical_constants['Bohr magneton'][0]
tunnel_energy = 0
relaxation_gamma = 1/(111e-9)
#Basis States
basis_states = [np.array([[1],[0]]), np.array([[0],[1]])]
#Hamiltonian of electron spin in magnetic field
hamiltonian = np.array([[energy_zero, tunnel_energy],[tunnel_energy,energy_one]])
# Create density matrix with initial conditions
# - Create as vector for using solve_ivp
density_matrix_init = np.array([0, 0, 0, 1.0]).astype(complex)
def dagger(state):
    return np.transpose(np.conj(state))
def commutator(matA, matB):
    return (np.matmul(matA, matB) - np.matmul(matB, matA))
def anticommutator(matA, matB):
    return (np.matmul(matA, matB) + np.matmul(matB, matA))
def dissipator(gamma, density_matrix):
    rho = density_matrix.reshape((2,2))
    jump_op = basis_states[0]@basis_states[1].T
    dissipation_term = gamma*(jump_op@rho@dagger(jump_op))
    dissipation_term -= gamma*(0.5)*anticommutator(dagger(jump_op)@jump_op, rho)
    return dissipation_term
def density_dot(time, density_matrix):
    # Von Neumann Contribution
    density_reshape = density_matrix.reshape((2,2))
    current_density_dot = (-1j/const.hbar)*commutator(hamiltonian, density_reshape)
    # Dissispator Contribution
    current_density_dot += dissipator(relaxation_gamma, density_matrix)
    return (current_density_dot.reshape((1,-1)))
# Time Parameters
T_MIN = 0
T_MAX = 600e-9
# Solve the initial value problem
sol = solve_ivp(density_dot, [T_MIN, T_MAX], density_matrix_init, max_step=T_MAX/100)
# Extract Pppulations
density_matrix_00 = sol.y[0]
density_matrix_11 = sol.y[3]
# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(sol.t*1e9, density_matrix_00.real, label=r"$\rho_{00}$", color='b')
ax1.plot(sol.t*1e9, density_matrix_11.real, label=r"$\rho_{11}$", color='r')
# Legend Placement
ax1.legend(fontsize=14, frameon=False, loc='center left', bbox_to_anchor=(0.7,0.5))
ax1.set_xlabel('Time [ns]', fontsize=14)
ax1.set_ylabel('Density Matrix Diagonal Entries', fontsize=14)
plt.show()