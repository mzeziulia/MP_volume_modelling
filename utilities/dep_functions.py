import numpy as np

"""Voltage and acidity dependence functions (nonlinear) and turn-on of proton pump"""

'''def pH_dependence(h_prime, k1 = 7.63*1e4, hprime_half = 3.2 * 1e-5):
   return 1.0 / (1.0 + np.exp(-k1*(h_prime - hprime_half)))

   Equations for pH- and V- dependency functions:
   f(pH) = 1 / (1 + e(k1*(pH-pH1/2)) 
   f(U) = 1 / (1 + e(k2*(U-U1/2))
'''   

# ASOR pH dependency function 

def pH_dependence_ASOR(pH, alpha=3.0, pH_offset=5.4):
    """
    When simulating wild-type ASOR pH dependency function, alpha = 3.0, pH_offset = 5.4
    When simulating ASOR alkaline shifted mutant pH dependency function channel, alpha = 1.0, pH_offset = 7.4
    """
    return 1.0 / (1.0 + np.exp(alpha*(pH-pH_offset)))

# ASOR voltage dependency function
def v_dependence_ASOR(U, k2=80, U_half = -40*1e-3):
    return 1.0 / (1.0 + np.exp(k2*(U - U_half)))

# ClC pH dependency function
def pH_dependence_ClC(pH):
    return 1.0 / (1.0 + np.exp(1.5*(5.5-pH)))

# ClC voltage dependency function
def v_dependence_ClC(U, k2=80, U_half = -40*1e-3):
    return 1.0 / (1.0 + np.exp(k2*(U - U_half)))

# V-ATPase insertion function
def g_VATP_dependence(t, k=0, t_half=0):
    return 1.0 / (1.0 + np.exp(k*(t_half - t)))