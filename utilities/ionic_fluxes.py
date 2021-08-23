import numpy as np
from . import dep_functions as F
# import dep_functions as F

"""Ionic fluxes"""

def J_cl_asor(n_potential_cl, g_asor, U, pH, Ar):
    return n_potential_cl * g_asor * F.v_dependence_ASOR(U) * F.pH_dependence_ASOR(pH) * Ar

def J_na_tpc(n_potential_na, g_tpc, Ar):
    return n_potential_na * g_tpc * Ar

def J_k(n_potential_k, g_k, Ar):
    return n_potential_k * g_k * Ar

def J_Cl_CLC(n_potential, g_clc, U, pH, Ar ):
    return 2.0 * n_potential * g_clc * F.v_dependence_ClC(U) * F.pH_dependence_ClC(pH) * Ar

def J_H_CLC(n_potential, g_clc, U, pH, Ar ):
    return -n_potential * g_clc * F.v_dependence_ClC(U) * F.pH_dependence_ClC(pH) * Ar

def J_Na_NHE(nhe_potential, g_nhe, Ar):
    return nhe_potential * g_nhe * Ar

def J_H_NHE(nhe_potential, g_nhe, Ar):
    return -nhe_potential * g_nhe * Ar

def J_VATPase(VATPase_potential, g_VATPase, time, Ar):
    return -VATPase_potential * g_VATPase * F.g_VATP_dependence(time) * Ar

def J_H_leak(n_potential_H, g_H_leak, Ar):
    return n_potential_H * g_H_leak * Ar
