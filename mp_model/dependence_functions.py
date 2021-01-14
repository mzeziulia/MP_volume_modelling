import numpy as np

# k1 = 7.63*1e4 # steepness of pH dependence
# hprime_half = 3.2 * 1e-5 # half maximum pH for pH dependence function

# k2 = -55.0 # steepness of voltage dependence function
# U_half = -50*1e-3 # half maximum voltage for voltage dependence function

# def pH_dependence(h_prime):
#     return 1.0 / (1.0 + np.exp(-k1*(h_prime - hprime_half)))

# def v_dependence(U):
#     return 1.0 / (1.0 + np.exp(k2*(U - U_half)))

### NEW DEPENDENCY FUNCTIONS ###
def pH_dependence(h_prime):
  pH=-np.log10(h_prime)
  return 1.0 / (1.0 + np.exp(1.5*(pH-5.5)))

def v_dependence(U, k2=80, U_half = -40*1e-3):
    return 1.0 / (1.0 + np.exp(k2*(U - U_half)))