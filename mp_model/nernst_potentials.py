import numpy as np

RT = 2477.572 # gas constant x temperature in K
F = 96485.0 # Faraday's constant

def Cl_ASOR(U, ion_outside, ion_inside):
    # Nernst potential for ASOR
    return U + ( (RT / F) * np.log( ion_outside / ion_inside ))

def Na_K(U, ion_outside, ion_inside):
    # Nernst potential for channels that pass sodium / potassium
    return -U + ( (RT / F) * np.log( ion_outside / ion_inside ))

def CLC(U, Cl_i, Cl_o, hprime_i, hprime_o):
    # Nernst potential for CLC
    return U + ( (RT / (3*F) ) * np.log( ( (Cl_o**2) / (Cl_i**2) ) * (hprime_i / hprime_o) ))

def NHE(Na_o, Na_i, hprime_i, hprime_o):
    # Nernst potential for NHE
    return  np.log( (Na_o / Na_i) * ( hprime_i / hprime_o ) )