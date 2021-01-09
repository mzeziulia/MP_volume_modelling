import numpy as np
from .dependence_functions import v_dependence, pH_dependence

def Cl_ASOR(n_potential_cl, g_asor, U, hprime, A):
    return n_potential_cl * g_asor * v_dependence(U) * pH_dependence(hprime) * A

def Na_TPC(n_potential_na, g_tpc, A):
    return n_potential_na * g_tpc * A

def K(n_potential_k, g_k, A):
    return n_potential_k * g_k * A

def Cl_CLC(n_potential, g_clc, U, A):
    return 2.0 * n_potential * g_clc * v_dependence(U) * A

def H_CLC(n_potential, g_clc, U, A):
    return -n_potential * g_clc * v_dependence(U) * A

def Na_NHE(nhe_potential, g_nhe, A):
    return nhe_potential * g_nhe * A

def H_NHE(nhe_potential, g_nhe, A):
    return -nhe_potential * g_nhe * A