import numpy as np

"""Voltage and acidity dependence functions (nonlinear) and turn-on of proton pump"""

'''def pH_dependence(h_prime, k1 = 7.63*1e4, hprime_half = 3.2 * 1e-5):
   return 1.0 / (1.0 + np.exp(-k1*(h_prime - hprime_half)))
'''   

#def pH_dependence_ASOR(pH):
#   return 1.0 / (1.0 + np.exp(1.5*(pH-5.4)))


# steeper pH-depedence THIS ONE normal
def pH_dependence_ASOR(pH):
    return 1.0 / (1.0 + np.exp(3.0*(pH-5.4)))

# # No pH dependence ASOR
# def pH_dependence_ASOR(pH):
#   return 0.5

# # alkaline shifted and wider pH dependence THIS ONE for mutant
# def pH_dependence_ASOR(pH):
#     return 1.0 / (1.0 + np.exp(1.0*(pH-7.4)))


# alkaline shifted equally steep pH dependence no use
#def pH_dependence_ASOR(pH):
#  return 1.0 / (1.0 + np.exp(3.0*(pH-7.4)))


def v_dependence_ASOR(U, k2=80, U_half = -40*1e-3):
    return 1.0 / (1.0 + np.exp(k2*(U - U_half)))

# # No v dependence ASOR
# def v_dependence_ASOR(U, k2=80, U_half = -40*1e-3):
#    return 0.5

def pH_dependence_ClC(pH):
    return 1.0 / (1.0 + np.exp(1.5*(5.5-pH)))

# # No pH dependence CLC
# def pH_dependence_ClC(pH):
#   return 0.5

def v_dependence_ClC(U, k2=80, U_half = -40*1e-3):
    return 1.0 / (1.0 + np.exp(k2*(U - U_half)))

# # No V dependence CLC
# def v_dependence_ClC(U, k2=80, U_half = -40*1e-3):
#     return 0.5

# function to enable late insertion of H+-ATPase
#def g_VATP_dependence(t, k=0.01, t_half=600):
#    return 1.0 / (1.0 + np.exp(k*(t_half - t)))
# without insertion, always active
def g_VATP_dependence(t, k=0, t_half=0):
    return 1.0 / (1.0 + np.exp(k*(t_half - t)))