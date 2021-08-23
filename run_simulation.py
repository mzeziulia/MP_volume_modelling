from config import A0
import matplotlib.pyplot as plt
import numpy as np

from utilities import dep_functions as F
from utilities import ionic_fluxes as i_flux
from utilities import nernst_potentials as potentials
from utilities import simulation_tools as simtools
from plotting import display_simulation_results




user_inputs = parse_user_inputs()

G['ASOR'] = user_input['g_ASOR']



 #### FROM CONFIG FILE - WILL IT WORK?
parameters = {
    'dt' = dt,
    'T' = T
    'G' = G,
    'external_ions_concentrations' = external_ions_concentrations,
    'A_from_V_const' = A_from_V_const,
    'X_amount' = X_amount,
    'buffer_capacity_t0' = buffer_capacity_t0, 
    'V_t0' = V0, 
    'c_spec' = c_spec, 
    'RT' = 2578.5871, 
    'F' = 96485.0,
    'pH_i'= pH_i,
    'U0' = U0,
    'A0' = A0,
    'C0' = C0,
    'Sum_initial_amounts' = Sum_initial_amounts
   }

results = simtools.run_simulation(T, initial_state, **parameters)

results['concentrations']['Cl']
results['volumes']['Cl']

display_simulation_results(results)
