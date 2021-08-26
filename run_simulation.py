from config import dt, T, external_ions_concentrations, A_from_V_const, X_amount, buffer_capacity_t0, V0, c_spec, pH_i, U0, A0, C0, Sum_initial_amounts, internal_ions_amounts
import matplotlib.pyplot as plt
import numpy as np

from utilities import dep_functions as F
from utilities import ionic_fluxes as i_flux
from utilities import nernst_potentials as potentials
from utilities import simulation_tools as simtools
# from plotting import display_simulation_results

# user_inputs = parse_user_inputs()

G={}
G['ASOR'] = float(input("G ASOR"))
G['TPC'] = float(input("G TPC"))
G['K'] = float(input("G K"))
G['CLC'] = float(input("G CLC"))
G['NHE'] = float(input("G NHE"))
G['vATPase'] = float(input("G vATPase"))
G['H_leak'] = float(input("G H_leak"))

 #### FROM CONFIG FILE - WILL IT WORK?
parameters = {
    'dt': dt,
    'T': T,
    'G': G,
    'external_ions_concentrations': external_ions_concentrations,
    'A_from_V_const': A_from_V_const,
    'X_amount': X_amount,
    'buffer_capacity_t0': buffer_capacity_t0, 
    'V_t0': V0, 
    'c_spec': c_spec, 
    'RT': 2578.5871, 
    'F': 96485.0,
    'pH_i': pH_i,
    'U0': U0,
    'A0': A0,
    'C0': C0,
    'Sum_initial_amounts': Sum_initial_amounts
   }


results = simtools.run_simulation(internal_ions_amounts, parameters) # I removed ** in front of parameters

# results['concentrations']['Cl']
# results['volumes']['Cl']

# display_simulation_results(results)
