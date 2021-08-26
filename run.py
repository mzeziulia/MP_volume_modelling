from config import dt, T, A_from_V_const, buffer_capacity_t0, V0, c_spec, pH_i, U0, A0, C0, initialize_internal_concentrations
import matplotlib.pyplot as plt
import numpy as np

from utilities import simulation_tools as simtools
from utilities import parse_user_input
# from plotting import display_simulation_results

G, ASOR_args, Cl_i_concentration = parse_user_input()

X_amount, external_ions_concentrations, internal_ions_amounts, internal_ions_concentrations, Sum_initial_amounts = initialize_internal_concentrations(Cl_i_concentration)

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
    'Sum_initial_amounts': Sum_initial_amounts,
    'alpha': ASOR_args['alpha'],
    'pH_offset': ASOR_args['pH_offset']
   }


results = simtools.run_simulation(internal_ions_amounts, parameters) # I removed ** in front of parameters

# results['concentrations']['Cl']
# results['volumes']['Cl']

# display_simulation_results(results)
